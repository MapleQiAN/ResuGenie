from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
import os

from .api.router import api_router
from .core.config import settings

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

app = FastAPI(title=settings.PROJECT_NAME)

# 配置CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
    "*",  # 在生产环境中应该替换为实际域名
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 包含API路由
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    return {"message": "ResuGenie API 服务正在运行"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
