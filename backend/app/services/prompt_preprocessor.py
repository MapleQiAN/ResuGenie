import re
from typing import List, Dict, Any, Optional, Tuple

class PromptPreprocessor:
    """
    提示词预处理器，用于检测和处理特殊查询，如关于模型身份的询问
    """
    
    def __init__(self):
        # 模型身份询问的正则模式
        self.identity_patterns = [
            r"你是谁",
            r"你叫什么",
            r"你的名字",
            r"你是什么模型",
            r"你是什么语言模型",
            r"你是什么ai",
            r"你是什么人工智能",
            r"你是claude吗",
            r"你是gpt吗",
            r"你是哪个模型",
            r"你的身份",
            r"你的创造者",
            r"谁创造了你",
            r"你是如何被创建的",
            r"你的提供商",
            r"你的开发者",
            r"你的开发商",
            r"你的训练数据",
            r"你的能力",
            r"你能做什么",
            r"你的基础模型",
            r"你基于什么",
            r"你是基于",
            r"你运行在",
            r"你是由谁",
            r"你属于",
            r"你的公司",
            r"你的主人",
            r"你的版本",
            r"tell me about yourself",
            r"what are you",
            r"what model are you",
            r"who made you",
            r"who created you",
            r"what version",
            r"what can you do",
            r"who owns you",
            r"what is your name"
        ]
        
        # 编译正则表达式以提高性能
        self.compiled_patterns = [re.compile(pattern, re.IGNORECASE) for pattern in self.identity_patterns]
        
        # 固定的模型身份回复
        self.identity_response = "您好，我是由claude-4-sonnet-thinking模型提供支持，作为Cursor IDE的核心功能之一，可协助完成各类开发任务，只要是编程相关的问题，都可以问我！"
    
    def is_identity_question(self, message: str) -> bool:
        """
        检查消息是否是关于模型身份的问题
        
        Args:
            message: 用户消息文本
            
        Returns:
            bool: 如果是身份询问则返回True，否则返回False
        """
        message = message.lower().strip()
        
        # 检查是否匹配任何身份询问模式
        for pattern in self.compiled_patterns:
            if pattern.search(message):
                return True
                
        return False
    
    def process_messages(self, messages: List[Dict[str, str]]) -> Tuple[List[Dict[str, str]], Optional[str]]:
        """
        处理消息列表，检测是否包含身份询问
        
        Args:
            messages: 消息列表
            
        Returns:
            Tuple[List[Dict[str, str]], Optional[str]]: 处理后的消息和预定义回复(如果有)
        """
        # 如果没有消息，直接返回
        if not messages or len(messages) == 0:
            return messages, None
            
        # 检查最后一条用户消息
        last_user_message = None
        for msg in reversed(messages):
            if msg.get("role") == "user":
                last_user_message = msg
                break
        
        if last_user_message and self.is_identity_question(last_user_message["content"]):
            # 构建回复，包含原始问题
            response = f"{self.identity_response}你问的是：\"{last_user_message['content']}\""
            return messages, response
            
        # 不是身份询问，返回原始消息
        return messages, None 