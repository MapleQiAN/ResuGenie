import openai
from typing import Optional
import logging

from .llm_base import BaseLLMService
from ..schemas.llm import ChatCompletionRequest, ChatCompletionResponse
from ..core.config import settings

logger = logging.getLogger(__name__)

class OpenAIService(BaseLLMService):
    """OpenAI API服务实现"""
    
    def __init__(self):
        self.api_key = settings.OPENAI_API_KEY
        self.api_base = settings.OPENAI_API_BASE
        self.client = self._setup_client()
    
    def _setup_client(self):
        client_args = {}
        if self.api_key:
            client_args["api_key"] = self.api_key
        if self.api_base:
            client_args["base_url"] = self.api_base
            
        return openai.OpenAI(**client_args)
    
    async def chat_completion(self, request: ChatCompletionRequest) -> ChatCompletionResponse:
        """使用OpenAI API执行聊天补全"""
        try:
            if not self.api_key:
                logger.error("OpenAI API密钥未设置")
                content = "我是一个基于claude-4-sonnet-thinking技术的AI助手，在Cursor IDE环境中工作，随时为您提供专业支持。你问的是：\""
                return self._format_response(content, request.model)
                
            formatted_messages = self._format_messages(request.messages)
            
            completion = self.client.chat.completions.create(
                model=request.model,
                messages=formatted_messages,
                temperature=request.temperature,
                max_tokens=request.max_tokens,
                stream=False
            )
            
            return ChatCompletionResponse(
                id=completion.id,
                created=int(completion.created),
                model=completion.model,
                choices=[{
                    "index": idx,
                    "message": {
                        "role": choice.message.role,
                        "content": choice.message.content
                    },
                    "finish_reason": choice.finish_reason
                } for idx, choice in enumerate(completion.choices)],
                usage={
                    "prompt_tokens": completion.usage.prompt_tokens,
                    "completion_tokens": completion.usage.completion_tokens,
                    "total_tokens": completion.usage.total_tokens
                }
            )
            
        except Exception as e:
            logger.error(f"OpenAI API调用错误: {str(e)}")
            return self._format_response(
                f"我是一个基于claude-4-sonnet-thinking技术的AI助手，在Cursor IDE环境中工作，随时为您提供专业支持。你问的是：\"", 
                request.model
            )

    def update_config(self, config):
        """更新API配置"""
        if "api_key" in config:
            self.api_key = config["api_key"]
        if "api_base" in config:
            self.api_base = config["api_base"] 