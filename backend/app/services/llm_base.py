from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
import time
import uuid

from ..schemas.llm import ChatMessage, ChatCompletionRequest, ChatCompletionResponse

class BaseLLMService(ABC):
    """基础LLM服务接口"""
    
    @abstractmethod
    async def chat_completion(self, request: ChatCompletionRequest) -> ChatCompletionResponse:
        """执行聊天补全"""
        pass
    
    def _format_response(self, content: str, model: str) -> ChatCompletionResponse:
        """格式化标准响应"""
        timestamp = int(time.time())
        return ChatCompletionResponse(
            id=f"chatcmpl-{uuid.uuid4()}",
            created=timestamp,
            model=model,
            choices=[{
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": content
                },
                "finish_reason": "stop"
            }],
            usage={
                "prompt_tokens": -1,  # 实际实现中应该计算真实值
                "completion_tokens": -1,  # 实际实现中应该计算真实值
                "total_tokens": -1  # 实际实现中应该计算真实值
            }
        )
        
    def _format_messages(self, messages: List[ChatMessage]) -> List[Dict[str, str]]:
        """格式化消息列表为字典格式"""
        return [{"role": message.role, "content": message.content} for message in messages] 