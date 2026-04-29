#!/usr/bin/env python3
"""
推理技能主入口脚本
Reasoning Skill Main Entry Point

用法 / Usage:
  python main.py --type <type> --input <input>
  python main.py --help

支持的推理类型 / Supported reasoning types:
  calculate   数值计算、公式求解、加权评分、统计分析
  judge       二分类/多分类判断、阈值判定、置信度评估
  logic       演绎推理、归纳推理、溯因推理、概率推理
  decision    多准则决策、加权评分决策、决策树
  analyze     特征提取、相关性分析、归因分析、因果推断
"""

import argparse
import sys
import os

SKILL_TYPES = {
    "calculate": {
        "name": "推理计算 (Calculate)",
        "description": "数值计算、公式求解、加权评分、统计分析、阈值计算",
        "skill_path": os.path.join(os.path.dirname(__file__), "..", "..", "skills", "reasoning", "calculate", "SKILL.md"),
    },
    "judge": {
        "name": "推理判断 (Judge)",
        "description": "二分类/多分类判断、阈值判定、置信度评估、异常检测",
        "skill_path": os.path.join(os.path.dirname(__file__), "..", "..", "skills", "reasoning", "judge", "SKILL.md"),
    },
    "logic": {
        "name": "逻辑推理 (Logic)",
        "description": "演绎推理、归纳推理、溯因推理、概率推理、规则推理",
        "skill_path": os.path.join(os.path.dirname(__file__), "..", "..", "skills", "reasoning", "logic", "SKILL.md"),
    },
    "decision": {
        "name": "推理决策 (Decision-Making)",
        "description": "多准则决策(MCDM)、加权评分决策、风险决策、决策树",
        "skill_path": os.path.join(os.path.dirname(__file__), "..", "..", "skills", "reasoning", "decision-making", "SKILL.md"),
    },
    "analyze": {
        "name": "推理分析 (Analyze)",
        "description": "特征提取、相关性分析、聚类分析、归因分析、因果推断",
        "skill_path": os.path.join(os.path.dirname(__file__), "..", "..", "skills", "reasoning", "analyze", "SKILL.md"),
    },
}


def list_types():
    """列出所有支持的推理类型"""
    print("可用推理类型 / Available reasoning types:\n")
    for type_key, info in SKILL_TYPES.items():
        print(f"  {type_key:<12} {info['name']}")
        print(f"               {info['description']}\n")


def load_skill(skill_type: str) -> str:
    """加载对应技能的 SKILL.md 内容"""
    info = SKILL_TYPES[skill_type]
    skill_path = os.path.abspath(info["skill_path"])
    if not os.path.exists(skill_path):
        raise FileNotFoundError(f"技能文件未找到: {skill_path}")
    with open(skill_path, "r", encoding="utf-8") as f:
        return f.read()


def route(skill_type: str, input_data: str) -> None:
    """根据类型路由到对应子模块并输出处理提示"""
    info = SKILL_TYPES[skill_type]
    print(f"[推理技能] 类型: {info['name']}")
    print(f"[推理技能] 输入: {input_data}\n")

    try:
        skill_content = load_skill(skill_type)
        print("=" * 60)
        print(f"已加载技能文件: {info['name']}")
        print("=" * 60)
        # 仅输出 frontmatter 之后的内容摘要（前 20 行正文）
        lines = skill_content.split("\n")
        body_lines = []
        in_frontmatter = False
        frontmatter_count = 0
        for line in lines:
            if line.strip() == "---":
                frontmatter_count += 1
                in_frontmatter = frontmatter_count < 2
                continue
            if not in_frontmatter:
                body_lines.append(line)
        print("\n".join(body_lines[:20]))
        if len(body_lines) > 20:
            print(f"\n... (共 {len(body_lines)} 行，请查阅完整技能文件)")
    except FileNotFoundError as e:
        print(f"[警告] {e}")
        print(f"[提示] 请确认技能文件已正确部署，或查阅文档: ./skills/reasoning/{skill_type}/SKILL.md")


def main():
    parser = argparse.ArgumentParser(
        prog="reasoning",
        description="推理技能主入口 / Reasoning Skill Entry Point",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--type",
        choices=list(SKILL_TYPES.keys()),
        metavar="TYPE",
        help=f"推理类型，可选: {', '.join(SKILL_TYPES.keys())}",
    )
    parser.add_argument(
        "--input",
        metavar="INPUT",
        help="输入数据或描述（字符串）",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="列出所有可用推理类型",
    )

    args = parser.parse_args()

    if args.list:
        list_types()
        return

    if not args.type:
        print("[错误] 请指定推理类型 --type\n")
        list_types()
        print("使用 --help 查看完整帮助信息")
        sys.exit(1)

    if not args.input:
        print(f"[错误] 请通过 --input 提供输入数据\n")
        parser.print_help()
        sys.exit(1)

    route(args.type, args.input)


if __name__ == "__main__":
    main()
