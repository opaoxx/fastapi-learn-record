# FastAPI 学习项目

这是一个从零开始学习 Python FastAPI 的课程型仓库。项目目标不是只堆代码，而是把 FastAPI 的核心知识点、后端 API 设计、测试、前端调用、OpenAPI 契约和 AI 服务接口思维，做成一套可以持续复习、也适合分享给初学者的学习材料。

课程内容由两部分组成：

- 可运行的 FastAPI 示例项目：位于 `first_api/`
- 配套 HTML 课程和速查表：位于 `lessons/` 与 `reference/`

## 学习目标

本项目围绕三个阶段逐步推进：

1. 学会 FastAPI 基础：路由、请求体、路径参数、查询参数、响应模型、错误处理。
2. 学会真实后端项目结构：APIRouter、依赖注入、配置管理、SQLite、SQLModel、测试。
3. 走向 AI 服务接口：后台任务、文件上传、AI 客户端边界、任务状态、OpenAPI 契约和前端调用。

## 项目结构

```text
.
├── assets/              # 课程页面共享样式
├── first_api/           # FastAPI 示例项目
│   ├── main.py          # 应用入口、CORS、静态前端、router 挂载
│   ├── schemas.py       # Pydantic / SQLModel 请求响应模型
│   ├── database.py      # SQLite 与数据库 Session
│   ├── security.py      # X-API-Key 鉴权
│   ├── task_worker.py   # 后台摘要任务执行逻辑
│   ├── routers/         # 路由模块
│   ├── services/        # 业务逻辑和 AI 客户端边界
│   └── frontend/        # 静态浏览器页面
├── lessons/             # 每一节课的完整 HTML 讲义
├── reference/           # 每节课对应的速查表
├── learning-records/    # 学习记录
├── tests/               # pytest 自动化测试
├── COURSE-STANDARD.md   # 后续课程质量标准
├── MISSION.md           # 学习目标
├── RESOURCES.md         # 官方资料和参考资源
└── index.html           # 课程目录入口
```

## 快速开始

建议使用 PowerShell 或 Git Bash 在项目根目录执行。

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt
fastapi dev first_api/main.py
```

启动后打开：

- API 文档：http://127.0.0.1:8000/docs
- OpenAPI 契约：http://127.0.0.1:8000/openapi.json
- 静态前端：http://127.0.0.1:8000/app/

## 配置

复制 `.env.example` 为 `.env` 后可以修改本地配置：

```bash
cp .env.example .env
```

默认 API Key 是：

```text
dev-secret-key
```

调用受保护接口时需要请求头：

```text
X-API-Key: dev-secret-key
```

## 运行测试

```bash
python -m pytest -q
```

当前测试覆盖了：

- 基础 CRUD API
- API Key 鉴权
- 后台摘要任务
- 文件上传
- CORS 与静态前端
- OpenAPI 契约
- 任务列表分页、筛选和响应信封

## 学习方式

推荐顺序：

1. 从 `index.html` 打开课程目录。
2. 阅读一节 `lessons/` 里的完整课程。
3. 打开对应 `reference/` 速查表复习。
4. 回到 `first_api/` 查看真实代码。
5. 运行测试确认自己没有改坏项目行为。

每节课都尽量遵循同一结构：先讲原理，再看机制，再读代码，最后做实验和小测。

## 打开课程 HTML

课程页面是静态 HTML 文件，不需要启动 FastAPI 服务也能阅读。

本地阅读方式：

1. 下载或克隆仓库到电脑。
2. 在文件管理器中打开项目根目录。
3. 双击 `index.html`，或右键选择用浏览器打开。
4. 从课程目录进入 `lessons/` 中的完整讲义，或进入 `reference/` 中的速查表。

也可以直接在浏览器地址栏打开本地文件路径，例如：

```text
F:\teaching_me\index.html
```

如果是在 GitHub 网页上直接点击 HTML 文件，通常会看到源码而不是课程页面。建议把仓库克隆到本地后，用浏览器打开 `index.html` 阅读。
