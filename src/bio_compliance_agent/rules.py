from dataclasses import dataclass
from typing import Callable, List

from .models import Finding


@dataclass
class Rule:
    rule_id: str
    title: str
    checker: Callable[[str], Finding]


def _contains_any(text: str, keywords: List[str]) -> bool:
    lower = text.lower()
    return any(k.lower() in lower for k in keywords)


def check_ethics_approval(text: str) -> Finding:
    ok = _contains_any(text, ["伦理", "IRB", "ethics approval", "伦理审批"])
    if ok:
        return Finding("R001", "伦理审批声明", "PASS", "检测到伦理审批相关描述", "保持伦理审批编号与日期可追溯")
    return Finding(
        "R001",
        "伦理审批声明",
        "HIGH",
        "未检测到伦理审批或IRB声明",
        "补充伦理审批机构、审批编号、审批日期与适用研究范围",
    )


def check_informed_consent(text: str) -> Finding:
    ok = _contains_any(text, ["知情同意", "informed consent", "受试者同意"])
    if ok:
        return Finding("R002", "知情同意", "PASS", "检测到知情同意相关描述", "补充同意书版本号和签署流程")
    return Finding(
        "R002",
        "知情同意",
        "HIGH",
        "未检测到知情同意流程描述",
        "补充受试者招募、告知、签署与撤回机制",
    )


def check_adverse_event(text: str) -> Finding:
    ok = _contains_any(text, ["不良事件", "adverse event", "AE", "SAE"])
    if ok:
        return Finding("R003", "不良事件处理机制", "PASS", "检测到AE/SAE处理描述", "补充报告时限与上报责任人")
    return Finding(
        "R003",
        "不良事件处理机制",
        "MEDIUM",
        "未检测到AE/SAE响应流程",
        "增加不良事件分级、处置时限、上报路径与追踪闭环",
    )


def check_data_privacy(text: str) -> Finding:
    ok = _contains_any(text, ["脱敏", "匿名化", "个人信息", "隐私", "privacy", "数据最小化"])
    if ok:
        return Finding("R004", "数据隐私与脱敏", "PASS", "检测到隐私保护相关描述", "补充数据保留周期与访问控制")
    return Finding(
        "R004",
        "数据隐私与脱敏",
        "MEDIUM",
        "未检测到明确的数据隐私和脱敏策略",
        "说明数据分类分级、脱敏方案、留存策略和权限控制",
    )


def check_traceability(text: str) -> Finding:
    ok = _contains_any(text, ["版本", "revision", "变更记录", "traceability", "追溯"])
    if ok:
        return Finding("R005", "文档版本追溯", "PASS", "检测到版本/变更追溯信息", "确保版本号、作者与审批链一致")
    return Finding(
        "R005",
        "文档版本追溯",
        "LOW",
        "未检测到版本管理与变更追溯机制",
        "增加文档版本号、变更日志、审批记录",
    )


def default_rules() -> List[Rule]:
    return [
        Rule("R001", "伦理审批声明", check_ethics_approval),
        Rule("R002", "知情同意", check_informed_consent),
        Rule("R003", "不良事件处理机制", check_adverse_event),
        Rule("R004", "数据隐私与脱敏", check_data_privacy),
        Rule("R005", "文档版本追溯", check_traceability),
    ]
