import argparse
from pathlib import Path

from .agent import BioComplianceAgent


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="生物医药合规文档 Agent（MVP）")
    parser.add_argument("input", help="输入文档路径（UTF-8 文本）")
    parser.add_argument("--output", default="deliverables/compliance_report.md", help="报告输出路径")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    agent = BioComplianceAgent()
    report = agent.review_file(args.input)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report.to_markdown(), encoding="utf-8")
    print(f"已生成报告：{output_path}")
    print(f"风险分：{report.risk_score}/100")


if __name__ == "__main__":
    main()
