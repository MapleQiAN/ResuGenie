import time
import uuid
from typing import List, Dict, Any, Optional

from .llm_base import BaseLLMService
from .prompt_preprocessor import PromptPreprocessor
from ..schemas.llm import ChatMessage, ChatCompletionRequest, ChatCompletionResponse
from ..core.config import settings

class ResumeAIService(BaseLLMService):
    """
    专门用于简历生成的AI服务，集成身份询问检测和特殊系统提示
    """
    
    def __init__(self):
        """初始化简历AI服务"""
        self.preprocessor = PromptPreprocessor()
        self._services = {}
        self.resume_system_prompt = """你是ResuGenie系统中的专业简历助手，一个专业的简历优化顾问和职业规划师。你需要帮助用户创建或优化简历，让用户的简历更加出色。

作为一个专业简历顾问，你的职责包括：

1. 生成专业、吸引人的简历内容
   - 确保内容清晰、精确、专业
   - 突出用户的技能、成就和经验
   - 使用行动导向的语言和具体的数据
   - 根据目标职位调整内容重点

2. 优化已有简历内容
   - 改进表述方式，使其更专业
   - 建议添加量化的成果
   - 删除冗余或无关内容
   - 改进语言表达，避免陈词滥调

3. 回答用户关于简历和求职的问题
   - 提供有关简历结构的建议
   - 解答特定行业简历规范
   - 建议如何应对简历中的挑战（如经验空缺）

回复时，请保持专业、直接且实用。你的建议应该具体且可操作，而不是泛泛而谈。

请记住：一份优秀的简历应该：
- 简洁明了（通常为1-2页）
- 重点突出（与目标职位相关）
- 成就导向（使用具体数据和结果）
- 针对性强（针对特定职位或行业调整）
- 无语法和拼写错误
- 格式一致（布局、字体、标点等）

你的目标是帮助用户创建一份能在招聘过程中脱颖而出的简历。"""
    
    async def chat_completion(self, request: ChatCompletionRequest) -> ChatCompletionResponse:
        """执行简历生成相关的聊天补全，包含提示词处理和身份检测"""
        try:
            # 转换消息格式
            messages = self._format_messages(request.messages)
            
            # 使用预处理器检测身份询问
            _, identity_response = self.preprocessor.process_messages(messages)
            
            # 如果是身份询问，直接返回预定义回答
            if identity_response:
                return self._format_response(identity_response, request.model)
            
            # 如果不是身份询问，继续常规处理
            # 首先检查是否已经包含系统提示
            has_system_prompt = any(msg.get("role") == "system" for msg in messages)
            
            # 如果没有系统提示，添加简历特定的系统提示
            if not has_system_prompt:
                messages.insert(0, {"role": "system", "content": self.resume_system_prompt})
            
            # 确定使用哪个LLM服务
            from .llm_factory import LLMServiceFactory
            factory = LLMServiceFactory()
            service = factory.get_service(request.model)
            
            # 创建新的请求，包含处理过的消息
            new_request = ChatCompletionRequest(
                model=request.model,
                messages=[ChatMessage(role=msg["role"], content=msg["content"]) for msg in messages],
                temperature=request.temperature,
                max_tokens=request.max_tokens,
                stream=request.stream
            )
            
            # 使用选择的服务处理请求
            response = await service.chat_completion(new_request)
            return response
            
        except Exception as e:
            # 处理任何异常，返回友好的错误信息
            error_message = f"处理您的简历请求时出错: {str(e)}"
            return self._format_response(error_message, request.model)
            
    def update_service_config(self, config):
        """
        临时更新LLM服务的配置
        
        Args:
            config (dict): 包含临时API配置的字典
        """
        try:
            # 获取LLM服务工厂
            from .llm_factory import LLMServiceFactory
            factory = LLMServiceFactory()
            
            # 更新各个服务的配置
            for service_name, service in factory._services.items():
                if service_name == "openai" and hasattr(service, "update_config"):
                    openai_config = {}
                    if "OPENAI_API_KEY" in config:
                        openai_config["api_key"] = config["OPENAI_API_KEY"]
                    if "OPENAI_API_BASE" in config:
                        openai_config["api_base"] = config["OPENAI_API_BASE"]
                    if openai_config:
                        service.update_config(openai_config)
                        
                elif service_name == "deepseek" and hasattr(service, "update_config"):
                    deepseek_config = {}
                    if "DEEPSEEK_API_KEY" in config:
                        deepseek_config["api_key"] = config["DEEPSEEK_API_KEY"]
                    if "DEEPSEEK_API_BASE" in config:
                        deepseek_config["api_base"] = config["DEEPSEEK_API_BASE"]
                    if deepseek_config:
                        service.update_config(deepseek_config)
                        
                elif service_name == "ollama" and hasattr(service, "update_config"):
                    ollama_config = {}
                    if "OLLAMA_API_BASE" in config:
                        ollama_config["api_base"] = config["OLLAMA_API_BASE"]
                    if ollama_config:
                        service.update_config(ollama_config)
            
            # 保存服务引用以便后续使用
            self._services = factory._services
            
        except Exception as e:
            import logging
            logging.error(f"更新服务配置时出错: {str(e)}")
            # 即使配置更新失败，我们也不中断主流程，只记录错误 