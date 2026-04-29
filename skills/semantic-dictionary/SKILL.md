---
name: semantic-dictionary
description: '语义字典技能：JSON格式语义信息存储、语义匹配、相似度计算、语义推理、语义对照判断。触发场景：当用户提到"语义字典"、"语义匹配"、"semantic dictionary"、"语义相似度"、"语义存储"、"语义推理"、"词义对照"时加载。'
---

# Semantic Dictionary 语义字典技能

## Schema 参考

详见：[语义字典 JSON Schema 定义](./references/semantic-schema.json)

示例字典：[示例语义字典](./references/example-dictionary.json)

---

## Phase 1：语义字典加载与校验

**输入**：JSON 语义字典文件路径或内联 JSON 字符串

**输出**：已校验的语义字典对象 + 索引结构

### 步骤

1. 读取 JSON（文件路径 → 读取文件内容；内联 JSON → 直接解析）
2. 校验 JSON 格式合法性（符合 RFC 8259 标准）
3. 校验 schema 完整性：顶层字段必须包含 `version`、`domain`、`terms`；每个 term 条目必须包含 `term`、`definition`、`synonyms`、`related_terms`、`domain`
4. 构建索引：
   - 主索引：`term` → 条目对象（用于精确查找，O(1)）
   - 同义词反向索引：`synonym` → 原始 `term`（用于同义词匹配）
   - 领域索引：`domain` → 条目列表（用于领域过滤）

**判断节点**：

- ✅ JSON 合法且 schema 完整 → 进入 Phase 2
- ❌ JSON 解析失败 → **失败处理**：报告失败行号和列号，停止执行
- ❌ schema 不完整 → **失败处理**：列出所有缺失字段（格式：`缺失字段: [field1, field2, ...]`），停止执行

---

## Phase 2：语义匹配（Semantic Matching）

**输入**：查询词（字符串）+ 已加载字典对象

**输出**：匹配结果列表，每项包含 `{ term, score, match_type }`

### 步骤

1. **精确匹配**：在主索引中查找查询词（大小写不敏感）
   - 命中 → score = 1.0，match_type = `exact`
2. **同义词匹配**：在同义词反向索引中查找查询词
   - 命中 → score = 0.85，match_type = `synonym`
3. **相关词扩展匹配**：遍历所有条目的 `related_terms`，计算 weight 加权得分
   - 命中 → score = `related_term.weight × 0.75`，match_type = `related`
4. 按 score 降序排列结果列表

**判断节点**：

- score ≥ 0.9 → 精确匹配（exact match），直接返回该条目
- 0.6 ≤ score < 0.9 → 模糊匹配（fuzzy match），返回候选列表
- score < 0.6 → 无匹配，返回空列表并提示"未找到匹配词条"

**失败处理**：

- 查询词为空（长度 = 0 或仅含空白字符）→ 提示："查询词不能为空，请输入有效词条"，停止执行
- 字典对象为空（terms 数组长度 = 0）→ 提示："字典为空，请先加载有效字典"，停止执行

---

## Phase 3：语义相似度计算

**输入**：词条 A（字符串）+ 词条 B（字符串）

**输出**：相似度分数 `sim ∈ [0, 1]` + 计算路径说明

### 步骤

1. **Jaccard 相似度**（同义词集合交集）：
   - `jaccard(A, B) = |synonyms_A ∩ synonyms_B| / |synonyms_A ∪ synonyms_B|`
   - 若两个集合均为空 → `jaccard = 0`
2. **路径距离分数**（related_terms 图遍历）：
   - 在 related_terms 图中执行 BFS，找 A 到 B 的最短路径长度 `d`
   - `path_score(A, B) = 1 / (1 + d)`（直接相连 d=1 → score=0.5；d=2 → score=0.33；不可达 → score=0）
   - 路径权重加成：沿路径累加 weight，取均值作为修正因子 `w_avg`，最终 `path_score = path_score × w_avg`
3. **领域权重加成**：
   - `domain_match(A, B) = 1` 若 `domain_A == domain_B`，否则 = 0
4. **综合相似度公式**：
   ```
   sim(A, B) = 0.5 × jaccard(synonyms_A, synonyms_B)
             + 0.3 × path_score(A, B)
             + 0.2 × domain_match(A, B)
   ```
5. 输出计算路径说明（每个分项的得分 + 依据）

**判断节点**：

- ✅ A 和 B 均在字典中存在 → 执行相似度计算
- ❌ A 或 B 任一不存在于字典 → **失败处理**：报告具体哪个词条不存在，建议先通过 Phase 2 匹配，停止计算

---

## Phase 4：语义推理判断

**输入**：命题字符串，格式为：
- `"X 是 Y 的一种"`（is-a 关系）
- `"X 与 Y 相关"`（related-to 关系）
- `"X 是 Y 的一部分"`（part-of 关系）
- `"X 与 Y 相反"`（opposite-of 关系）

**输出**：判断结论（`TRUE` / `FALSE` / `UNCERTAIN`）+ 置信度 `∈ [0, 1]` + 推理路径

### 步骤

1. **解析命题类型**：
   - 识别命题模式，提取 `subject`（X）、`relation`、`object`（Y）
   - 支持的关系类型：`is-a`、`has-a`、`related-to`、`opposite-of`、`part-of`
2. **查字典验证**：
   - 在 X 的 `related_terms` 中查找 Y，检查 `relation` 字段是否与命题关系一致
   - 若直接匹配：置信度 = related_term.weight
   - 若无直接连接：通过 Phase 3 计算 sim(X, Y)，置信度 = sim × 0.8（间接推断折扣系数）
3. **概率推理**：
   - 若 sim(X, Y) ≥ 0.6 且 relation 类型一致 → 结论倾向 `TRUE`
   - 若 sim(X, Y) ≤ 0.3 且存在 opposite-of 链接 → 结论倾向 `FALSE`
   - 其他情况 → 结论倾向 `UNCERTAIN`

**判断节点**：

- 置信度 ≥ 0.8 → 输出 `TRUE` 或 `FALSE`（依据关系方向）
- 0.5 ≤ 置信度 < 0.8 → 输出 `UNCERTAIN`，列出支持和反对证据
- 置信度 < 0.5 → 输出 `UNCERTAIN`，提示"字典证据不足，无法判断"

**输出示例**：

```
命题：judge 是 reasoning 的一种
结论：TRUE
置信度：0.92
推理路径：
  1. 解析命题 → subject=judge, relation=is-a, object=reasoning
  2. 查字典 → judge.related_terms 中存在 {term: reasoning, relation: is-a, weight: 0.92}
  3. 直接匹配，置信度 = 0.92 ≥ 0.8 → TRUE
```
