---
name: reasoning
description: 'AI推理技能套件：覆盖计算(calculate)、判断(judge)、逻辑推理(logic)、决策(decision-making)、分析(analyze)五大维度。触发场景：当用户提到"推理"、"计算"、"判断"、"逻辑"、"决策"、"分析"、"reasoning"、"calculate"、"judge"、"logic"、"decision"、"analyze"时加载。'
---

# Reasoning 推理技能套件

## 概述

本技能套件涵盖五大推理维度，提供结构化、可追溯的推理流程。

## 子技能索引

| 子技能 | 职责 | 触发词 |
|--------|------|--------|
| [calculate](#calculate-计算) | 数值计算、公式求解、加权评分、统计分析 | 计算、求值、加权、评分、公式、calculate、formula、score |
| [judge](#judge-判断) | 二分类/多分类判断、阈值判定、置信度评估、异常检测 | 判断、分类、是否、评估、异常、judge、classify、threshold |
| [logic](#logic-逻辑推理) | 演绎推理、归纳推理、溯因推理、概率推理、规则推理 | 逻辑、推导、演绎、归纳、概率、规则、logic、deduce、infer |
| [decision-making](#decision-making-决策) | 多准则决策、加权评分决策、风险决策、决策树 | 决策、选择方案、对比方案、权衡、最优解、decision、choose、optimize |
| [analyze](#analyze-分析) | 特征提取、相关性分析、聚类分析、归因分析、因果推断 | 分析、归因、相关性、特征、聚类、因果、analyze、attribution、correlation |

---

## calculate 计算

**路径**：`./calculate/SKILL.md`

**职责**：处理一切需要数值运算的场景，包括公式求解、加权评分、统计指标计算和阈值验证。

**触发词**：计算、求值、加权、评分、公式、阈值、calculate、formula、score、weighted、threshold

---

## judge 判断

**路径**：`./judge/SKILL.md`

**职责**：对输入数据进行结构化判断，支持二分类、多分类、阈值判定、置信度评估及异常检测。

**触发词**：判断、分类、是否、评估、异常、排序、judge、classify、threshold、confidence、anomaly

---

## logic 逻辑推理

**路径**：`./logic/SKILL.md`

**职责**：构建可追溯的推理链，支持演绎、归纳、溯因、概率、规则、模糊逻辑及约束满足。

**触发词**：逻辑、推导、演绎、归纳、概率、规则、模糊、约束、logic、deduce、infer、probabilistic

---

## decision-making 决策

**路径**：`./decision-making/SKILL.md`

**职责**：基于多准则决策（MCDM）对候选方案进行量化评分和最优选择。

**触发词**：决策、选择方案、对比方案、权衡、最优解、decision、choose、optimize、tradeoff、MCDM

---

## analyze 分析

**路径**：`./analyze/SKILL.md`

**职责**：从数据中提取特征、识别模式、归因分析并给出可操作建议。

**触发词**：分析、归因、相关性、特征、聚类、因果、analyze、attribution、correlation、clustering、causal

---

## 使用方式

1. 识别用户意图，匹配对应子技能触发词
2. 加载对应子技能的 SKILL.md
3. 按照该子技能定义的 Phase 流程执行
4. 输出结构化结果

## 质量标准

- 所有判断标准必须量化，禁止使用"比较好"等模糊表达
- 每个推理步骤必须可追溯
- 失败时提供明确的降级策略
