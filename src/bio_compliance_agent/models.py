from dataclasses import dataclass, field
from typing import List


@dataclass
class Finding:
    rule_id: str
    title: str
    level: str  # HIGH, MEDIUM, LOW, PASS
    evidence: str
    suggestion: str


@dataclass
class ComplianceReport:
    document_name: str
    summary: str
    risk_score: int
    findings: List[Finding] = field(default_factory=list)
    assumptions: List[str] = field(default_factory=list)

    def to_markdown(self) -> str:
        lines = [
            f"# 合规审查报告：{self.document_name}",
            "",
            f"- 总结：{self.summary}",
            f"- 风险分：{self.risk_score}/100（分数越高风险越高）",
            "",
            "## 逐条发现",
        ]

        for item in self.findings:
            lines.extend(
                [
                    f"### [{item.level}] {item.rule_id} - {item.title}",
                    f"- 证据：{item.evidence}",
                    f"- 建议：{item.suggestion}",
                    "",
                ]
            )

        if self.assumptions:
            lines.append("## 假设与边界")
            for a in self.assumptions:
                lines.append(f"- {a}")

        return "\n".join(lines) + "\n"
