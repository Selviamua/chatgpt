# 生物医药合规文档 Agent（赛道六）

## 项目目标
构建一个面向生物医药文档审查场景的 AI Agent MVP，帮助团队在初赛/决赛演示中完成：
- 合规条款自动检查；
- 风险分级（高/中/低）；
- 整改建议生成；
- 报告自动输出。

> 定位：**合规预审助手**，用于提升效率与一致性，不替代专家最终判断。

## 技术栈
- Python 3（标准库）
- 架构：规则引擎 + Agent 工作流（扫描、评分、建议、报告）
- 文档输出：Markdown

## 启动命令
```bash
python main.py samples/clinical_protocol_sample.txt --output deliverables/compliance_report.md
```

## 测试命令
```bash
python -m unittest discover -s tests -p 'test_*.py'
```

## 构建命令
当前 MVP 为脚本型项目，无独立构建步骤。可使用如下命令做基础语法检查：

```bash
python -m compileall src main.py tests
```

## 目录结构
```text
.
├── AGENTS.md
├── README.md
├── main.py
├── src/
│   └── bio_compliance_agent/
│       ├── __init__.py
│       ├── agent.py
│       ├── cli.py
│       ├── models.py
│       └── rules.py
├── tests/
│   └── test_agent.py
├── samples/
│   └── clinical_protocol_sample.txt
├── docs/
│   └── competition/
│       ├── full_process.md
│       ├── technical_solution.md
│       └── demo_script.md
└── deliverables/
    └── compliance_report.md    # 运行后生成
```

## 当前想完成什么
- [x] 定义赛道六项目目标与边界
- [x] 实现可运行的合规文档 Agent MVP
- [x] 提供测试与样例
- [x] 准备初赛可提交材料（技术方案、全流程记录、路演讲稿）
- [ ] 下一步：扩展法规知识库与文档解析能力（PDF/Word）

## 交付材料（初赛）
1. 技术方案文档：`docs/competition/technical_solution.md`
2. 全流程记录：`docs/competition/full_process.md`
3. Demo讲稿：`docs/competition/demo_script.md`
4. 可运行代码与测试：`src/`, `main.py`, `tests/`
