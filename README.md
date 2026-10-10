# funagent

farfarfun 组织内共享的 Claude Code 子智能体（subagent）定义集合。每个 `agent/*.md` 是一个角色定义，覆盖 PRD、技术设计、后端实现、前端实现和项目 Owner 编排。

## 安装

克隆或下载后，创建 Claude Code 的 agent 目录，再复制需要的 `agent/*.md` 文件：

```bash
git clone https://github.com/farfarfun/funagent.git
mkdir -p your-project/.claude/agents
cp funagent/agent/product-prd-agent.md your-project/.claude/agents/
```

## 测试

```bash
uv run pytest
```

## 最小示例

以 `product-prd-agent` 为例，完成上述安装后进入目标项目并启动 Claude Code：

```bash
cd your-project
claude
```

在 Claude Code 会话中发送下面的请求。它会调用 `product-prd-agent`，并将 PRD 写入 `docs/prd/weekly-meal-planner.md`：

```
使用 product-prd-agent，把下面的业务需求整理成 PRD，并将结果写入 docs/prd/weekly-meal-planner.md：

我们要做一个家庭每周备餐工具。用户可以输入家庭人数、饮食禁忌和预算，工具生成周一到周日的晚餐计划、采购清单和预计花费。用户可以替换某一道菜，替换后采购清单和预算需要同步更新。首版只支持中文和人民币，不需要账号系统。
```

## 目录说明

| 文件 | 角色 |
| --- | --- |
| `agent/product-prd-agent.md` | 产品需求文档专家 |
| `agent/tech-design-agent.md` | 技术设计专家 |
| `agent/backend-engineer-agent.md` | 后端工程师专家 |
| `agent/frontend-engineer-agent.md` | 前端工程师专家 |
| `agent/frontend-spec-agent.md` | 前端规格专家 |
| `agent/project-owner-agent.md` | 项目 Owner 编排专家 |

---

## 关于 farfarfun

[farfarfun](https://github.com/farfarfun) 是一个专注于实用工具库的开源组织，
涵盖云存储、数据处理、AI、多媒体与开发工具链等方向。

- 🏠 组织主页：<https://github.com/farfarfun>
- 📦 PyPI：<https://pypi.org/user/niuliangtao/>
- 📧 联系：farfarfun@qq.com

本项目基于 [MIT](LICENSE) 协议开源。
