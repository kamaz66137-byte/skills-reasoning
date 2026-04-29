"""
基础路径常量定义模块
Base Path Constants for the Reasoning Skill Pack

提供统一的路径常量，避免各子模块中重复使用 os.path.join(os.path.dirname(__file__), ...) 硬编码。
Provides unified path constants so sub-modules avoid duplicating os.path.join hard-coding.
"""

import os

# 当前文件所在目录：.github/skill-pack/reasoning/base/
_BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# .github/skill-pack/reasoning/
SKILL_PACK_REASONING_ROOT = os.path.dirname(_BASE_DIR)

# .github/skill-pack/
SKILL_PACK_ROOT = os.path.dirname(SKILL_PACK_REASONING_ROOT)

# .github/
GITHUB_ROOT = os.path.dirname(SKILL_PACK_ROOT)

# .github/skills/
SKILLS_ROOT = os.path.join(GITHUB_ROOT, "skills")

# .github/skills/reasoning/
SKILLS_REASONING_ROOT = os.path.join(SKILLS_ROOT, "reasoning")

# 各子技能 SKILL.md 绝对路径
SKILL_PATHS = {
    "calculate": os.path.join(SKILLS_REASONING_ROOT, "calculate", "SKILL.md"),
    "judge":     os.path.join(SKILLS_REASONING_ROOT, "judge",     "SKILL.md"),
    "logic":     os.path.join(SKILLS_REASONING_ROOT, "logic",     "SKILL.md"),
    "decision":  os.path.join(SKILLS_REASONING_ROOT, "decision-making", "SKILL.md"),
    "analyze":   os.path.join(SKILLS_REASONING_ROOT, "analyze",   "SKILL.md"),
}
