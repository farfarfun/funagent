# funagent

farfarfun 组织内共享的 Claude Code / Codex 子智能体（subagent）定义集合，每个 `agent/*.md` 是一个可直接被智能体编排工具调用的角色定义（PRD、技术设计、后端实现、前端实现、项目 Owner 编排等）。

## 安装

克隆或下载后，把需要的 `agent/*.md` 文件复制到你项目的 `.claude/agents/`（或对应工具的 agent 定义目录）下即可：

```bash
git clone https://github.com/farfarfun/funagent.git
cp funagent/agent/product-prd-agent.md your-project/.claude/agents/
```

## 最小示例

以 `product-prd-agent` 为例，在支持 subagent 的工具里按名字调用：

```
> 使用 product-prd-agent，把下面的业务需求整理成 PRD：...
```

## 目录说明

| 文件 | 角色 |
| --- | --- |
| `agent/product-prd-agent.md` | 产品需求文档专家 |
| `agent/tech-design-agent.md` | 技术设计专家 |
| `agent/backend-engineer-agent.md` | 后端工程师专家 |
| `agent/frontend-engineer-agent.md` | 前端工程师专家（内容待补充） |
| `agent/frontend-spec-agent.md` | 前端规格专家（内容待补充） |
| `agent/project-owner-agent.md` | 项目 Owner 编排专家 |

## 关于 farfarfun

[farfarfun](https://github.com/farfarfun) 是一个专注于实用工具库的开源组织，
涵盖云存储、数据处理、AI、多媒体与开发工具链等方向。

- 🏠 组织主页：<https://github.com/farfarfun>
- 📧 联系：farfarfun@qq.com

本项目基于 [MIT](LICENSE) 协议开源。
