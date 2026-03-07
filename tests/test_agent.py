import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from bio_compliance_agent import BioComplianceAgent


GOOD_TEXT = """
已完成伦理审批，IRB编号可追溯。
受试者签署知情同意。
发生AE/SAE将按流程上报。
涉及个人信息将匿名化与脱敏处理。
文档包含版本号与变更记录。
"""

BAD_TEXT = """
本研究计划在多中心进行，后续再补充管理细则。
"""


class AgentTestCase(unittest.TestCase):
    def test_low_risk_document(self) -> None:
        report = BioComplianceAgent().review_text(GOOD_TEXT, "good.txt")
        self.assertLessEqual(report.risk_score, 20)
        self.assertTrue(all(f.level == "PASS" for f in report.findings))

    def test_high_risk_document(self) -> None:
        report = BioComplianceAgent().review_text(BAD_TEXT, "bad.txt")
        self.assertGreaterEqual(report.risk_score, 80)
        high_count = sum(1 for f in report.findings if f.level == "HIGH")
        self.assertGreaterEqual(high_count, 2)


if __name__ == "__main__":
    unittest.main()
