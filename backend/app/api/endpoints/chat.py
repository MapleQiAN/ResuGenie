from fastapi import APIRouter, HTTPException, Depends
from typing import List, Dict, Any
import logging

from ...schemas.llm import ChatCompletionRequest, ChatCompletionResponse, ErrorResponse
from ...services.llm_factory import LLMServiceFactory

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/completions", response_model=ChatCompletionResponse)
async def chat_completion(request: ChatCompletionRequest):
    """
    聊天补全API端点
    """
    try:
        factory = LLMServiceFactory()
        service = factory.get_service(request.model)
        response = await service.chat_completion(request)
        return response
    except Exception as e:
        logger.error(f"聊天API错误: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"处理请求时发生错误: {str(e)}"
        )

@router.get("/models")
async def get_available_models():
    """
    获取可用的模型列表
    """
    from ...core.config import settings
    
    models = list(settings.MODEL_PROVIDERS.keys())
    return {"models": models} 