#!/usr/bin/env python3
"""
技能包主入口脚本
Skill Pack Main Entry Point

用法 / Usage:
  python main.py --pack <pack> [options]
  python main.py --list
  python main.py --help

可用技能包 / Available skill packs:
  reasoning   推理技能套件（计算、判断、逻辑、决策、分析）
"""

import argparse
import sys
import os
import subprocess

SKILL_PACKS = {
    "reasoning": {
        "name": "推理技能套件 (Reasoning)",
        "description": "覆盖计算(calculate)、判断(judge)、逻辑推理(logic)、决策(decision-making)、分析(analyze)五大维度",
        "entry": os.path.join(os.path.dirname(__file__), "reasoning", "main.py"),
    },
}


def list_packs():
    """列出所有可用技能包"""
    print("可用技能包 / Available skill packs:\n")
    for pack_key, info in SKILL_PACKS.items():
        print(f"  {pack_key:<14} {info['name']}")
        print(f"                 {info['description']}\n")


def route_to_pack(pack_name: str, extra_args: list) -> None:
    """路由到对应技能包的入口脚本"""
    info = SKILL_PACKS[pack_name]
    entry_path = os.path.abspath(info["entry"])

    if not os.path.exists(entry_path):
        print(f"[错误] 技能包入口文件未找到: {entry_path}")
        sys.exit(1)

    print(f"[技能包] 加载: {info['name']}")
    print(f"[技能包] 入口: {entry_path}\n")

    cmd = [sys.executable, entry_path] + extra_args
    result = subprocess.run(cmd)
    sys.exit(result.returncode)


def main():
    parser = argparse.ArgumentParser(
        prog="skill-pack",
        description="技能包主入口 / Skill Pack Main Entry Point",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--pack",
        choices=list(SKILL_PACKS.keys()),
        metavar="PACK",
        help=f"技能包名称，可选: {', '.join(SKILL_PACKS.keys())}",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="列出所有可用技能包",
    )

    # 解析已知参数，剩余参数转发给对应技能包
    args, remaining = parser.parse_known_args()

    if args.list:
        list_packs()
        return

    if not args.pack:
        print("[错误] 请指定技能包 --pack\n")
        list_packs_hint = "  " + "\n  ".join(SKILL_PACKS.keys())
        print(f"可用技能包:\n{list_packs_hint}\n")
        print("使用 --help 查看完整帮助，使用 --list 查看技能包详情")
        sys.exit(1)

    route_to_pack(args.pack, remaining)


if __name__ == "__main__":
    main()
