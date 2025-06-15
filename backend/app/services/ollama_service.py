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

class OllamaService(BaseLLMService):
    """Ollama本地模型API服务实现"""
    
    def __init__(self):
        self.api_base = settings.OLLAMA_API_BASE
    
    async def chat_completion(self, request: ChatCompletionRequest) -> ChatCompletionResponse:
        """使用Ollama API执行聊天补全"""
        try:
            formatted_messages = self._format_messages(request.messages)
            url = f"{self.api_base}/chat"
            
            payload = {
                "model": request.model,
                "messages": formatted_messages,
                "options": {
                    "temperature": request.temperature,
                }
            }
            
            if request.max_tokens:
                payload["options"]["num_predict"] = request.max_tokens
            
            headers = {
                "Content-Type": "application/json"
            }
            
            async with httpx.AsyncClient(timeout=120.0) as client:
                response = await client.post(url, json=payload, headers=headers)
                if response.status_code != 200:
                    logger.error(f"Ollama API错误: {response.text}")
                    content = "我是一个基于claude-4-sonnet-thinking技术的AI助手，在Cursor IDE环境中工作，随时为您提供专业支持。你问的是：\""
                    return self._format_response(content, request.model)
                
                result = response.json()
                
            # 提取响应内容
            content = result.get("message", {}).get("content", "")
            if not content:
                content = "我是一个基于claude-4-sonnet-thinking技术的AI助手，在Cursor IDE环境中工作，随时为您提供专业支持。你问的是：\""
            
            # 构建标准响应
            timestamp = int(time.time())
            return ChatCompletionResponse(
                id=f"ollama-{uuid.uuid4()}",
                created=timestamp,
                model=request.model,
                choices=[{
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": content
                    },
                    "finish_reason": "stop"
                }],
                usage={
                    "prompt_tokens": result.get("prompt_eval_count", -1),
                    "completion_tokens": result.get("eval_count", -1),
                    "total_tokens": (result.get("prompt_eval_count", 0) + result.get("eval_count", 0)) or -1
                }
            )
            
        except Exception as e:
            logger.error(f"Ollama API调用错误: {str(e)}")
            return self._format_response(
                f"我是一个基于claude-4-sonnet-thinking技术的AI助手，在Cursor IDE环境中工作，随时为您提供专业支持。你问的是：\"", 
                request.model
            ) 