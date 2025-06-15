from fastapi import APIRouter

from .endpoints import chat, resume

api_router = APIRouter()
api_router.include_router(chat.router, prefix="/chat", tags=["chat"])
api_router.include_router(resume.router, prefix="", tags=["resume"])
