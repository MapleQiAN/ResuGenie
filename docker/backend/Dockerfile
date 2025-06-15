FROM python:3.11-slim

WORKDIR /app

# 复制依赖文件
COPY backend/requirements.txt requirements.txt

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制整个后端代码
COPY backend /app/backend

# 为环境变量设置默认值
ENV PORT=8000
ENV OPENAI_API_KEY=""
ENV OPENAI_API_BASE="https://api.openai.com/v1"
ENV OPENAI_DEFAULT_MODEL="gpt-3.5-turbo"
ENV DEEPSEEK_API_KEY=""
ENV DEEPSEEK_API_BASE="https://api.deepseek.com/v1"
ENV DEEPSEEK_DEFAULT_MODEL="deepseek-chat"
ENV OLLAMA_API_BASE="http://ollama:11434/api"
ENV OLLAMA_DEFAULT_MODEL="llama2"

# 暴露端口
EXPOSE 8000

# 运行应用
CMD ["python", "-m", "backend.app.main"] 