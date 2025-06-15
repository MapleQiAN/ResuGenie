from fastapi import APIRouter, HTTPException, Body
from typing import Dict, Any, List
import logging

from ...schemas.llm import ChatCompletionRequest, ChatCompletionResponse, ErrorResponse
from ...services.resume_ai_service import ResumeAIService

router = APIRouter()
logger = logging.getLogger(__name__)

# 创建简历AI服务实例
resume_ai_service = ResumeAIService()

@router.post("/completions", response_model=ChatCompletionResponse)
async def resume_chat_completion(request: ChatCompletionRequest):
    """
    简历生成和优化专用的聊天补全API端点
    """
    try:
        # 使用专门的简历AI服务处理请求
        response = await resume_ai_service.chat_completion(request)
        return response
    except Exception as e:
        logger.error(f"简历聊天API错误: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"处理请求时发生错误: {str(e)}"
        )

@router.post("/optimize", response_model=Dict[str, Any])
async def optimize_resume_content(data: Dict[str, Any] = Body(...)):
    """
    优化简历内容，用于简历优化页面
    """
    try:
        content = data.get("content", "")
        job_position = data.get("jobPosition", "")
        
        if not content:
            raise HTTPException(status_code=400, detail="简历内容不能为空")
        
        # 构建消息
        messages = [
            {"role": "system", "content": resume_ai_service.resume_system_prompt},
            {"role": "user", "content": f"请帮我优化以下简历内容，使其更专业、更有竞争力。目标职位: {job_position}\n\n{content}"}
        ]
        
        # 创建请求
        request = ChatCompletionRequest(
            model=data.get("model", "gpt-3.5-turbo"),
            messages=[ChatCompletionRequest.ChatMessage(**msg) for msg in messages],
            temperature=0.7
        )
        
        # 发送聊天请求
        response = await resume_ai_service.chat_completion(request)
        
        # 提取AI回复内容
        optimized_content = ""
        if response and response.choices and len(response.choices) > 0:
            optimized_content = response.choices[0]["message"]["content"]
        
        return {
            "original": content,
            "optimized": optimized_content,
            "success": True
        }
        
    except Exception as e:
        logger.error(f"简历优化错误: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"优化简历内容时发生错误: {str(e)}"
        )

@router.post("/generate", response_model=Dict[str, Any])
async def generate_resume_content(data: Dict[str, Any] = Body(...)):
    """
    根据用户提供的基本信息生成简历内容，用于简历创建页面
    """
    try:
        resume_data = data.get("resumeData", {})
        
        if not resume_data:
            raise HTTPException(status_code=400, detail="简历数据不能为空")
            
        # 构建系统消息
        system_message = resume_ai_service.resume_system_prompt
        
        # 构建用户消息
        user_message = "请根据以下信息生成一份专业的简历内容：\n\n"
        
        # 基本信息
        basics = resume_data.get("basics", {})
        if basics:
            user_message += "## 基本信息\n"
            user_message += f"姓名: {basics.get('name', '')}\n"
            user_message += f"职位: {basics.get('label', '')}\n"
            user_message += f"邮箱: {basics.get('email', '')}\n"
            user_message += f"电话: {basics.get('phone', '')}\n"
            user_message += f"所在地: {basics.get('location', '')}\n"
            user_message += f"个人概述: {basics.get('summary', '')}\n\n"
            
        # 工作经历
        work_list = resume_data.get("work", [])
        if work_list:
            user_message += "## 工作经历\n"
            for i, work in enumerate(work_list):
                user_message += f"{i+1}. {work.get('company', '')} - {work.get('position', '')}\n"
                user_message += f"   时间: {work.get('startDate', '')} 至 {work.get('endDate', '')}\n"
                user_message += f"   职责: {work.get('summary', '')}\n\n"
                
        # 教育经历
        edu_list = resume_data.get("education", [])
        if edu_list:
            user_message += "## 教育经历\n"
            for i, edu in enumerate(edu_list):
                user_message += f"{i+1}. {edu.get('institution', '')} - {edu.get('area', '')}\n"
                user_message += f"   学历: {edu.get('studyType', '')}\n"
                user_message += f"   时间: {edu.get('startDate', '')} 至 {edu.get('endDate', '')}\n\n"
                
        # 技能
        skills = resume_data.get("skills", [])
        if skills:
            user_message += "## 技能\n"
            for i, skill in enumerate(skills):
                keywords = ", ".join(skill.get("keywords", []))
                user_message += f"{i+1}. {skill.get('name', '')} (熟练度: {skill.get('level', 0)}/5)\n"
                if keywords:
                    user_message += f"   关键词: {keywords}\n\n"
                    
        # 获取目标职位或行业
        target_position = data.get("targetPosition", "")
        if target_position:
            user_message += f"\n请为申请{target_position}岗位优化简历内容，使其更专业、更有竞争力。"
        else:
            user_message += "\n请根据以上信息生成专业的简历内容，使其更具竞争力。"
        
        # 构建消息列表
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ]
        
        # 创建请求
        request = ChatCompletionRequest(
            model=data.get("model", "gpt-3.5-turbo"),
            messages=[ChatCompletionRequest.ChatMessage(**msg) for msg in messages],
            temperature=0.7
        )
        
        # 发送聊天请求
        response = await resume_ai_service.chat_completion(request)
        
        # 提取AI生成的内容
        generated_content = ""
        if response and response.choices and len(response.choices) > 0:
            generated_content = response.choices[0]["message"]["content"]
        
        return {
            "content": generated_content,
            "success": True
        }
        
    except Exception as e:
        logger.error(f"简历生成错误: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"生成简历内容时发生错误: {str(e)}"
        ) 