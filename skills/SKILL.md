---
name: reasoning-skills-index
description: '推理技能套件主索引：覆盖计算(calculate)、判断(judge)、逻辑推理(logic)、决策(decision-making)、分析(analyze)、语义字典(semantic-dictionary)、技能串联(skill-chaining)七大维度。触发场景：当用户需要查找或选择推理技能时加载。'
---

# Reasoning Skills 推理技能套件索引

## 子技能索引

| 子技能 | 职责 | 触发词 |
|--------|------|--------|
| [calculate](#calculate-计算) | 数值计算、公式求解、加权评分、统计分析 | 计算、求值、加权、评分、公式、calculate、formula、score |
| [judge](#judge-判断) | 二分类/多分类判断、阈值判定、置信度评估、异常检测 | 判断、分类、是否、评估、异常、judge、classify、threshold |
| [logic](#logic-逻辑推理) | 演绎推理、归纳推理、溯因推理、概率推理、规则推理 | 逻辑、推导、演绎、归纳、概率、规则、logic、deduce、infer |
| [decision-making](#decision-making-决策) | 多准则决策、加权评分决策、风险决策、决策树 | 决策、选择方案、对比方案、权衡、最优解、decision、choose、optimize |
| [analyze](#analyze-分析) | 特征提取、相关性分析、聚类分析、归因分析、因果推断 | 分析、归因、相关性、特征、聚类、因果、analyze、attribution、correlation |
| [semantic-dictionary](#semantic-dictionary-语义字典) | 语义存储、语义匹配、相似度计算、语义推理 | 语义字典、语义匹配、语义相似度、语义推理、词义对照、semantic dictionary |
| [skill-chaining](#skill-chaining-技能串联) | 多步推理流水线、语义关联、技能协调 | 多步推理、技能串联、推理链、组合推理、pipeline、skill chaining |

---

## calculate 计算

**路径**：参见 `.github/skills/reasoning/calculate/SKILL.md`

**职责**：处理一切需要数值运算的场景，包括公式求解、加权评分、统计指标计算和阈值验证。

**触发词**：计算、求值、加权、评分、公式、阈值、calculate、formula、score、weighted、threshold

---

## judge 判断

**路径**：参见 `.github/skills/reasoning/judge/SKILL.md`

**职责**：对输入数据进行结构化判断，支持二分类、多分类、阈值判定、置信度评估及异常检测。

**触发词**：判断、分类、是否、评估、异常、排序、judge、classify、threshold、confidence、anomaly

---

## logic 逻辑推理

**路径**：参见 `.github/skills/reasoning/logic/SKILL.md`

**职责**：构建可追溯的推理链，支持演绎、归纳、溯因、概率、规则、模糊逻辑及约束满足。

**触发词**：逻辑、推导、演绎、归纳、概率、规则、模糊、约束、logic、deduce、infer、probabilistic

---

## decision-making 决策

**路径**：参见 `.github/skills/reasoning/decision-making/SKILL.md`

**职责**：基于多准则决策（MCDM）对候选方案进行量化评分和最优选择。

**触发词**：决策、选择方案、对比方案、权衡、最优解、decision、choose、optimize、tradeoff、MCDM

---

## analyze 分析

**路径**：参见 `.github/skills/reasoning/analyze/SKILL.md`

**职责**：从数据中提取特征、识别模式、归因分析并给出可操作建议。

**触发词**：分析、归因、相关性、特征、聚类、因果、analyze、attribution、correlation、clustering、causal

---

## semantic-dictionary 语义字典

**路径**：[./semantic-dictionary/SKILL.md](./semantic-dictionary/SKILL.md)

**职责**：以 JSON 格式存储语义信息，支持语义匹配、相似度计算、语义推理和词义对照判断。

**触发词**：语义字典、语义匹配、语义相似度、语义存储、语义推理、词义对照、semantic dictionary、semantic matching、semantic similarity

---

## skill-chaining 技能串联

**路径**：[./skill-chaining/SKILL.md](./skill-chaining/SKILL.md)

**职责**：通过语义字典关联，将多个推理技能串联成多步推理流水线，实现复杂组合推理任务。

**触发词**：多步推理、技能串联、推理链、组合推理、pipeline、skill chaining、多步骤、推理流水线

---

## 使用方式

1. 识别用户意图，匹配对应子技能触发词
2. 加载对应子技能的 SKILL.md
3. 按照该子技能定义的 Phase 流程执行
4. 输出结构化结果

对于需要多个技能协作的复合任务，使用 [skill-chaining](./skill-chaining/SKILL.md) 进行统一调度。

## 质量标准

- 所有判断标准必须量化，禁止使用"比较好"等模糊表达
- 每个推理步骤必须可追溯
- 失败时提供明确的降级策略
