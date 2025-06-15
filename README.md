# 🧞 ResuGenie · AI简历生成与优化助手

ResuGenie 是一个基于 AI 的简历生成与优化平台，帮助用户高效地构建、分析和完善自己的简历内容，适用于应届生、求职者、职场进阶人群等所有打工人。

✨ 像神灯一样，只需许个愿，ResuGenie 就能让你的求职之路焕发光芒！

---

## ✨ 功能特色

### 1. ✍️ 智能生成简历
- 用户可通过表单输入个人信息
- 提供多种专业简历模板供用户选择
- 一键生成 PDF 简历，颜值与内容齐飞

### 2. 📤 简历优化建议
- 支持上传 PDF/DOCX 简历
- AI分析内容完整性、逻辑性、表达风格与美观度
- 返回结构化优化建议，帮你对症下药

### 3. 💬 智能改写助手
- 支持自然语言指令，如“强化项目经历”、“换个英文表达”等
- ResuGenie 自动修改并输出更新后的简历文本

### 4. 📚 优秀简历案例（可选）
- 内置精选行业优秀简历模板，帮助你借鉴提升

---

## 🛠️ 技术栈

| 技术 | 描述 |
|------|------|
| `Vue 3 + Vite` | 前端框架 |
| `Naive UI` | 优雅且美观的 UI 组件库 |
| `Pinia` | 状态管理 |
| `FastAPI` | 后端服务框架 |
| `OpenAI GPT-4o API` | 简历优化与改写逻辑核心 |
| `WeasyPrint` / `pdfkit` | 简历 PDF 渲染引擎 |
| `PyMuPDF` | 简历文本解析工具 |
| `Docker`（可选） | 打包与部署 |

---

## 📦 快速启动

### 1. 克隆项目

```bash
git clone https://github.com/MapleQiAN/ResuGenie.git
cd resugenie
```

### 2. 安装前端依赖并运行

```bash
cd frontend
npm install
npm run dev
```

### 3. 启动后端服务

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

确保 `.env` 中已配置 OpenAI API 密钥：

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
```

------

## 📌 路线图（Roadmap）

-  简历生成器 MVP
-  GPT 分析优化建议
-  ChatGPT风格改写简历内容
-  多语言支持（中/英）
-  支持导入/导出 JSON Resume
-  用户账号系统（保存历史简历）
-  本地化部署（支持 Ollama/LM Studio）
-  移动端适配优化

------

## 🙌 致开发者

欢迎参与贡献！你可以提交 Pull Request、提 Issue 或加入我们一同打造打工人最强辅助神器！🛠️

📧 联系方式：`your-email@example.com`
 🧠 项目灵感来源：[OpenAI GPT 系列](https://openai.com/)

------

## 🧞‍♂️ ResuGenie，让你的简历说人话。

> “每一个职业梦想，都值得被好好书写。”
