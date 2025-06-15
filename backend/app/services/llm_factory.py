from typing import Dict, Optional
import logging

from .llm_base import BaseLLMService
from .openai_service import OpenAIService
from .deepseek_service import DeepSeekService
from .ollama_service import OllamaService
from ..core.config import settings

logger = logging.getLogger(__name__)

class LLMServiceFactory:
    """LLM服务工厂，根据模型名选择对应的服务"""
    
    _instance = None
    _services: Dict[str, BaseLLMService] = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LLMServiceFactory, cls).__new__(cls)
            cls._instance._initialize_services()
        return cls._instance
    
    def _initialize_services(self):
        """初始化所有可用的LLM服务"""
        self._services["openai"] = OpenAIService()
        self._services["deepseek"] = DeepSeekService()
        self._services["ollama"] = OllamaService()
    
    def get_service(self, model: str) -> BaseLLMService:
        """根据模型名称获取对应的服务"""
        provider = settings.MODEL_PROVIDERS.get(model)
        
        if not provider:
            logger.warning(f"未知的模型: {model}，默认使用OpenAI服务")
            return self._services["openai"]
        
        service = self._services.get(provider)
        if not service:
            logger.warning(f"未找到服务提供商: {provider}，默认使用OpenAI服务")
            return self._services["openai"]
        
        return service 