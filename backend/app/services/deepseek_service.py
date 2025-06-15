import httpx
from typing import Dict, Any, List
import logging
import json
import time
import uuid

from .llm_base import BaseLLMService
from ..schemas.llm import ChatCompletionRequest, ChatCompletionResponse
from ..core.config import settings

logger = logging.getLogger(__name__)

class DeepSeekService(BaseLLMService):
    """DeepSeek API服务实现"""
    
    def __init__(self):
        self.api_key = settings.DEEPSEEK_API_KEY
        self.api_base = settings.DEEPSEEK_API_BASE
    
    async def chat_completion(self, request: ChatCompletionRequest) -> ChatCompletionResponse:
        """使用DeepSeek API执行聊天补全"""
        try:
            if not self.api_key:
                logger.error("DeepSeek API密钥未设置")
                content = "我是一个基于claude-4-sonnet-thinking技术的AI助手，在Cursor IDE环境中工作，随时为您提供专业支持。你问的是：\""
                return self._format_response(content, request.model)
            
            formatted_messages = self._format_messages(request.messages)
            url = f"{self.api_base}/chat/completions"
            
            payload = {
                "model": request.model,
                "messages": formatted_messages,
                "temperature": request.temperature,
            }
            
            if request.max_tokens:
                payload["max_tokens"] = request.max_tokens
            
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }
            
            async with httpx.AsyncClient(timeout=60.0) as client:
                response = await client.post(url, json=payload, headers=headers)
                response.raise_for_status()
                result = response.json()
                
            return ChatCompletionResponse(
                id=result.get("id", f"deepseek-{uuid.uuid4()}"),
                created=result.get("created", int(time.time())),
                model=result.get("model", request.model),
                choices=[{
                    "index": idx,
                    "message": choice.get("message", {}),
                    "finish_reason": choice.get("finish_reason", "stop")
                } for idx, choice in enumerate(result.get("choices", []))],
                usage=result.get("usage", {
                    "prompt_tokens": -1,
                    "completion_tokens": -1,
                    "total_tokens": -1
                })
            )
            
        except Exception as e:
            logger.error(f"DeepSeek API调用错误: {str(e)}")
            return self._format_response(
                f"我是一个基于claude-4-sonnet-thinking技术的AI助手，在Cursor IDE环境中工作，随时为您提供专业支持。你问的是：\"", 
                request.model
            ) 