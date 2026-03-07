# 生物医药合规文档 Agent（赛道六）全流程记录

## 1. 项目目标
构建一个面向生物医药文档审查场景的 AI Agent MVP，实现：
1. 自动识别关键合规条款是否覆盖；
2. 对缺失项进行风险分级（高/中/低）；
3. 给出可执行的整改建议；
4. 输出可审计的报告材料，支持路演展示与后续人工复核。

## 2. 需求完善与边界讨论
### 2.1 用户问题
- 研发/注册文档审查靠人工逐页检查，成本高、效率低、容易漏项。

### 2.2 目标用户
- 高校创新团队（初创药械项目）
- 生物医药企业的 RA/QA 支持角色

### 2.3 非目标（本版明确不做）
- 不直接替代法务、伦理委员会或注册专家最终判断；
- 不做 PDF/Word 的复杂版式解析；
- 不接入外部知识库和商业 API（保持离线可跑）。

## 3. 技术方案
采用“规则引擎 + Agent 工作流”的最小可交付架构：
- 输入：UTF-8 文本文档；
- Agent 核心：
  - Rule Scanner：按规则检查关键条款；
  - Risk Scorer：按等级加权计算风险分；
  - Suggestion Writer：生成整改建议；
  - Report Builder：输出 Markdown 审查报告；
- 输出：可读、可追溯的报告文档。

## 4. 实现过程
1. 建立数据模型：`Finding`、`ComplianceReport`；
2. 建立规则集合（5条）：伦理审批、知情同意、不良事件、数据隐私、版本追溯；
3. 实现 `BioComplianceAgent`：文档审查、风险分计算、摘要生成；
4. 实现 CLI：支持 `python main.py <input> --output <report>`；
5. 提供样例输入文档，方便路演时稳定复现。

## 5. 测试与验证
### 5.1 单元测试
- `test_low_risk_document`：覆盖完整条款，期望低风险；
- `test_high_risk_document`：缺失关键条款，期望高风险。

### 5.2 端到端验证
- 使用 `samples/clinical_protocol_sample.txt` 生成报告文件，确认：
  - 报告可输出；
  - 风险分合理；
  - 每条规则均附证据和建议。

## 6. 当前结果
- 已形成可运行的 MVP 原型；
- 已具备“输入-分析-评分-建议-报告”闭环；
- 可直接作为初赛 demo 基础。

## 7. 风险与后续优化
1. 规则覆盖有限：后续应扩展至 GCP/NMPA/ICH 常见条款库；
2. 文本匹配能力有限：后续可引入检索增强和语义判定；
3. 文档解析有限：后续增加 PDF/Word 解析与表格识别；
4. 缺少真实业务数据评估：后续应与行业导师共同构建标注集。

## 8. 交付材料清单
- 技术方案：`docs/competition/technical_solution.md`
- 全流程记录：`docs/competition/full_process.md`
- 路演讲稿：`docs/competition/demo_script.md`
- 可运行原型代码：`src/` + `main.py`
- 测试代码：`tests/test_agent.py`
- Demo 输入样例：`samples/clinical_protocol_sample.txt`
- Demo 输出报告：`deliverables/compliance_report.md`（运行后生成）
