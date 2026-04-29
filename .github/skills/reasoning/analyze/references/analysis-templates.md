# 分析类型结构化报告模板
# Analysis Report Templates

本文档为 `analyze` 子技能在 Phase 4（解释分析结果）提供六种分析类型的结构化输出报告模板，包含字段说明和示例值。

---

## 1. 特征提取（Feature Extraction）报告模板

```yaml
analysis_type: feature_extraction
target_description: "<分析对象，如：用户行为日志>"
data_summary:
  total_samples: <总样本数>
  feature_count_raw: <原始特征数>
  feature_count_extracted: <提取后特征数>

top_features:
  - rank: 1
    feature_name: "<特征名称>"
    feature_type: "numerical | categorical | text | temporal"
    importance_score: <0-1 之间的重要性分数>
    description: "<该特征含义>"
  - rank: 2
    feature_name: "<特征名称>"
    importance_score: <分数>
    description: "<含义>"

extraction_method: "statistical | frequency | embedding | domain_specific"
quality_notes:
  - "<注意事项，如：特征 X 存在 15% 缺失值>"

actionable_insight: "<可操作洞察，如：特征 A、B、C 可用于构建分类模型>"
```

**示例**：

```yaml
analysis_type: feature_extraction
target_description: "电商用户购买行为"
data_summary:
  total_samples: 50000
  feature_count_raw: 42
  feature_count_extracted: 12
top_features:
  - rank: 1
    feature_name: "purchase_frequency_30d"
    feature_type: "numerical"
    importance_score: 0.87
    description: "近 30 天购买频次"
  - rank: 2
    feature_name: "avg_order_value"
    feature_type: "numerical"
    importance_score: 0.74
    description: "平均订单金额"
extraction_method: "statistical"
actionable_insight: "高频次+高客单价用户(top 10%)贡献 55% 收入，优先运营"
```

---

## 2. 相关性分析（Correlation Analysis）报告模板

```yaml
analysis_type: correlation
variables:
  - name: "<变量名1>"
    type: "continuous | ordinal | categorical"
  - name: "<变量名2>"
    type: "<类型>"

correlation_method: "pearson | spearman | kendall | chi-square"
results:
  - var_pair: ["<变量1>", "<变量2>"]
    coefficient: <相关系数，-1 到 1>
    p_value: <显著性 p 值>
    significant: <true/false，p < 0.05 为 true>
    strength: "strong(|r|≥0.7) | moderate(0.4≤|r|<0.7) | weak(|r|<0.4)"
    direction: "positive | negative"

key_findings:
  - "<主要发现，如：变量 A 与 B 强正相关，r=0.82，p<0.001>"

caveats:
  - "相关不代表因果"
  - "<其他注意事项>"
```

**示例**：

```yaml
analysis_type: correlation
variables:
  - name: "ad_spend"
    type: "continuous"
  - name: "revenue"
    type: "continuous"
correlation_method: "pearson"
results:
  - var_pair: ["ad_spend", "revenue"]
    coefficient: 0.83
    p_value: 0.0002
    significant: true
    strength: "strong"
    direction: "positive"
key_findings:
  - "广告支出与收入强正相关（r=0.83，p<0.001），每增加 1 万元广告支出，收入平均增加 3.2 万元"
caveats:
  - "相关不代表因果，可能存在第三变量（如季节性）影响"
```

---

## 3. 聚类分析（Clustering Analysis）报告模板

```yaml
analysis_type: clustering
algorithm: "k-means | hierarchical | dbscan"
optimal_k: <最优簇数>
k_selection_method: "elbow | silhouette | gap_statistic"

cluster_quality:
  silhouette_score: <0-1，> 0.5 为良好>
  wcss: <簇内平方和（K-Means）>

clusters:
  - cluster_id: 0
    size: <该簇样本数>
    proportion: <占比，如 "32%">
    centroid_features:
      - feature: "<特征名>"
        mean_value: <均值>
    label: "<业务含义标签，如：高价值用户>"
    characteristics: "<描述该簇特征>"
  - cluster_id: 1
    ...

key_findings:
  - "<主要聚类洞察>"

recommendations:
  - cluster_id: 0
    action: "<针对该簇的运营建议>"
```

**示例**：

```yaml
analysis_type: clustering
algorithm: "k-means"
optimal_k: 3
silhouette_score: 0.62
clusters:
  - cluster_id: 0
    size: 1200
    proportion: "24%"
    label: "高价值活跃用户"
    characteristics: "月均消费 > 500 元，登录频次 > 15 次/月"
  - cluster_id: 1
    size: 2800
    proportion: "56%"
    label: "普通用户"
    characteristics: "月均消费 50-200 元，登录频次 3-8 次/月"
  - cluster_id: 2
    size: 1000
    proportion: "20%"
    label: "沉睡用户"
    characteristics: "近 60 天无登录，历史消费 < 50 元"
key_findings:
  - "高价值用户仅占 24% 但贡献 61% 收入"
recommendations:
  - cluster_id: 2
    action: "发送专属唤醒优惠券（面值 20 元，消费满 100 元使用）"
```

---

## 4. 归因分析（Attribution Analysis）报告模板

```yaml
analysis_type: attribution
target_metric: "<被解释的指标，如：用户流失率>"
baseline_value: <基准值，如无干预时的期望值>
actual_value: <实际观测值>
delta: <actual - baseline>

attribution_method: "shap | variance_decomposition | regression_coef | simple_diff"

factors:
  - rank: 1
    factor_name: "<因素名>"
    contribution_value: <该因素贡献的绝对变化量>
    contribution_pct: "<贡献百分比，如 '38%'>"
    direction: "increase | decrease"
    evidence: "<支持该归因的证据描述>"
  - rank: 2
    ...

unexplained_pct: "<未解释部分占比>"

key_findings:
  - "<主要归因发现>"

recommendations:
  - factor: "<因素名>"
    action: "<针对性建议>"
    expected_impact: "<预期改善效果>"
```

**示例**：

```yaml
analysis_type: attribution
target_metric: "月度用户流失率"
baseline_value: 0.05
actual_value: 0.11
delta: +0.06（+120%）
attribution_method: "shap"
factors:
  - rank: 1
    factor_name: "价格上涨（+15%）"
    contribution_pct: "38%"
    direction: "increase"
    evidence: "流失用户中 72% 发生于涨价后 30 天内"
  - rank: 2
    factor_name: "核心功能使用率下降"
    contribution_pct: "29%"
    direction: "increase"
    evidence: "流失用户平均使用功能数从 5.2 降至 2.1"
unexplained_pct: "15%"
recommendations:
  - factor: "价格上涨"
    action: "推出保价锁定方案，允许老用户 3 个月内维持原价"
    expected_impact: "预计可挽回 20-30% 价格敏感流失用户"
```

---

## 5. 因果推断（Causal Inference）报告模板

```yaml
analysis_type: causal_inference
research_question: "<因果问题，如：广告曝光是否导致购买率提升？>"
treatment_variable: "<干预变量>"
outcome_variable: "<结果变量>"
confounders: ["<混淆变量1>", "<混淆变量2>"]

method: "ab_test | did | iv | propensity_score | dag_adjustment"

causal_dag:
  description: "<DAG 描述，如：年龄 → 购买意愿 ← 广告曝光>"

results:
  ate: <平均处理效应（Average Treatment Effect）>
  ate_ci_95: [<下界>, <上界>]
  p_value: <显著性>
  significant: <true/false>

interpretation: "<因果效应的业务解释>"

assumptions:
  - "<因果推断依赖的假设，如：随机分配假设>"

limitations:
  - "<局限性，如：无法排除某混淆变量的影响>"
```

---

## 6. 降维分析（Dimensionality Reduction）报告模板

```yaml
analysis_type: dimensionality_reduction
method: "pca | tsne | umap | lda"
original_dimensions: <原始特征数>
reduced_dimensions: <降维后保留维度数>

variance_explained:
  per_component:
    - component: "PC1"
      explained_variance_ratio: <比例，如 0.45>
      cumulative: <累计，如 0.45>
    - component: "PC2"
      explained_variance_ratio: <比例>
      cumulative: <累计>
  total: <所有保留成分的累计方差解释比，目标 ≥ 0.85>

top_loadings_pc1:
  - feature: "<特征名>"
    loading: <载荷值，绝对值越大越重要>

interpretation:
  - component: "PC1"
    business_meaning: "<主成分业务含义，如：整体规模因子>"

recommendations:
  - "<降维后的使用建议，如：使用 PC1-PC3 替代原始特征输入分类模型>"
```

**示例**：

```yaml
analysis_type: dimensionality_reduction
method: "pca"
original_dimensions: 20
reduced_dimensions: 4
variance_explained:
  total: 0.88
  per_component:
    - component: "PC1"
      explained_variance_ratio: 0.52
      cumulative: 0.52
    - component: "PC2"
      explained_variance_ratio: 0.21
      cumulative: 0.73
    - component: "PC3"
      explained_variance_ratio: 0.09
      cumulative: 0.82
    - component: "PC4"
      explained_variance_ratio: 0.06
      cumulative: 0.88
top_loadings_pc1:
  - feature: "revenue"
    loading: 0.82
  - feature: "order_count"
    loading: 0.79
  - feature: "avg_order_value"
    loading: 0.71
interpretation:
  - component: "PC1"
    business_meaning: "用户价值综合规模因子（收入、订单量、客单价共同驱动）"
recommendations:
  - "使用 PC1-PC4（解释 88% 方差）替代 20 维原始特征，可将模型训练时间减少约 60%"
```
