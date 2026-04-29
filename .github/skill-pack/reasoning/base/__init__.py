"""
skill-pack/reasoning/base 包初始化
从 paths.py 导出所有公共路径常量，方便其他子模块直接 from base import SKILLS_ROOT 等。
"""

from .paths import (  # noqa: F401
    GITHUB_ROOT,
    SKILL_PACK_ROOT,
    SKILL_PACK_REASONING_ROOT,
    SKILLS_ROOT,
    SKILLS_REASONING_ROOT,
    SKILL_PATHS,
)
