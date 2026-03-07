from pathlib import Path
from typing import List

from .models import ComplianceReport, Finding
from .rules import Rule, default_rules


WEIGHTS = {
    "HIGH": 30,
    "MEDIUM": 15,
    "LOW": 5,
    "PASS": 0,
}


class BioComplianceAgent:
    def __init__(self, rules: List[Rule] | None = None) -> None:
        self.rules = rules or default_rules()

    def review_text(self, text: str, document_name: str = "未命名文档") -> ComplianceReport:
        findings: List[Finding] = []
        risk = 0

        for rule in self.rules:
            result = rule.checker(text)
            findings.append(result)
            risk += WEIGHTS.get(result.level, 0)

        risk = min(risk, 100)
        summary = self._build_summary(findings, risk)

        assumptions = [
            "当前版本为规则+关键词混合MVP，不替代法律、伦理或注册事务专家判断。",
            "默认输入为中文/中英混合文档纯文本；PDF/Word解析不在当前MVP范围。",
        ]

        return ComplianceReport(
            document_name=document_name,
            summary=summary,
            risk_score=risk,
            findings=findings,
            assumptions=assumptions,
        )

    def review_file(self, path: str) -> ComplianceReport:
        p = Path(path)
        text = p.read_text(encoding="utf-8")
        return self.review_text(text, document_name=p.name)

    @staticmethod
    def _build_summary(findings: List[Finding], risk: int) -> str:
        high = sum(1 for f in findings if f.level == "HIGH")
        med = sum(1 for f in findings if f.level == "MEDIUM")
        low = sum(1 for f in findings if f.level == "LOW")

        if risk >= 60:
            posture = "高风险，建议先整改再流转。"
        elif risk >= 30:
            posture = "中风险，建议优先补齐关键条款。"
        else:
            posture = "低风险，可进入人工复核环节。"

        return f"{posture} 高风险{high}项，中风险{med}项，低风险{low}项。"
