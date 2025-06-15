from fastapi import APIRouter, Depends, HTTPException, Body, UploadFile, File
from typing import List, Dict, Any, Optional
import uuid
import json

router = APIRouter()

# 模拟数据存储
resume_templates = [
    {
        "id": "modern",
        "name": "现代简约",
        "preview": "https://img.icons8.com/clouds/344/resume.png"
    },
    {
        "id": "professional",
        "name": "专业商务",
        "preview": "https://img.icons8.com/clouds/344/business-report.png"
    },
    {
        "id": "creative",
        "name": "创意设计",
        "preview": "https://img.icons8.com/clouds/344/web-design.png"
    },
    {
        "id": "minimal",
        "name": "极简风格",
        "preview": "https://img.icons8.com/clouds/344/document.png"
    }
]

# 存储简历数据
resumes_data = {}

@router.get("/resume-templates", response_model=List[Dict[str, Any]])
async def get_templates():
    """获取简历模板列表"""
    return resume_templates

@router.post("/resumes")
async def create_resume(resume_data: Dict[str, Any] = Body(...)):
    """创建简历"""
    try:
        # 生成唯一ID
        resume_id = str(uuid.uuid4())
        
        # 获取简历数据和模板ID
        data = resume_data.get("resumeData", {})
        template_id = resume_data.get("templateId", "modern")
        
        # 模拟简历生成逻辑
        # 在实际应用中，这里可能会涉及到更复杂的处理，例如使用LLM生成内容
        
        # 生成简历HTML （简单示例）
        html_content = f"""
        <h1>{data.get('basics', {}).get('name', '未知姓名')}</h1>
        <p>{data.get('basics', {}).get('label', '')}</p>
        <p>邮箱: {data.get('basics', {}).get('email', '')}</p>
        <p>电话: {data.get('basics', {}).get('phone', '')}</p>
        <p>地址: {data.get('basics', {}).get('location', '')}</p>
        
        <h2>个人概述</h2>
        <p>{data.get('basics', {}).get('summary', '无')}</p>
        
        <h2>工作经历</h2>
        <ul>
        """
        
        # 添加工作经历
        for work in data.get('work', []):
            html_content += f"""
            <li>
                <h3>{work.get('company')} - {work.get('position')}</h3>
                <p>{work.get('startDate', '')} 至 {work.get('endDate', '至今')}</p>
                <p>{work.get('summary', '')}</p>
            </li>
            """
        
        html_content += "</ul>"
        
        # 添加教育经历
        html_content += "<h2>教育经历</h2><ul>"
        for edu in data.get('education', []):
            html_content += f"""
            <li>
                <h3>{edu.get('institution')} - {edu.get('area')}</h3>
                <p>{edu.get('studyType', '')}</p>
                <p>{edu.get('startDate', '')} 至 {edu.get('endDate', '至今')}</p>
            </li>
            """
        
        html_content += "</ul>"
        
        # 添加技能
        html_content += "<h2>技能特长</h2><ul>"
        for skill in data.get('skills', []):
            keywords = ", ".join(skill.get('keywords', []))
            html_content += f"""
            <li>
                <h3>{skill.get('name')}</h3>
                <p>熟练度: {skill.get('level')}/5</p>
                <p>关键词: {keywords}</p>
            </li>
            """
        
        html_content += "</ul>"
        
        # 保存简历数据
        resumes_data[resume_id] = {
            "id": resume_id,
            "data": data,
            "template_id": template_id,
            "html": html_content
        }
        
        return {"resumeId": resume_id, "data": html_content}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"创建简历失败: {str(e)}")

@router.get("/resumes/{resume_id}/suggestions")
async def get_optimization_suggestions(resume_id: str):
    """获取简历优化建议"""
    if resume_id not in resumes_data:
        raise HTTPException(status_code=404, detail="简历未找到")
    
    # 模拟优化建议
    suggestions = [
        {
            "id": "1",
            "section": "basics",
            "field": "summary",
            "original": resumes_data[resume_id]["data"].get("basics", {}).get("summary", ""),
            "suggestion": "添加更多关于您专业技能和成就的具体细节，使用数字和具体例子突出您的贡献。",
            "applied": False
        },
        {
            "id": "2",
            "section": "work",
            "field": "summary",
            "original": "",
            "suggestion": "在工作描述中使用行动导向的动词开头，例如'领导'、'开发'、'实施'，并突出成果。",
            "applied": False
        }
    ]
    
    return {"suggestions": suggestions}

@router.post("/resumes/{resume_id}/suggestions/{suggestion_id}/apply")
async def apply_optimization_suggestion(resume_id: str, suggestion_id: str):
    """应用优化建议"""
    if resume_id not in resumes_data:
        raise HTTPException(status_code=404, detail="简历未找到")
    
    # 在实际应用中，这里应该根据建议ID实际修改简历内容
    # 这里只是简单模拟
    
    return {"data": resumes_data[resume_id]["html"], "message": "已应用优化建议"}

@router.get("/resumes/{resume_id}/export/pdf")
async def export_resume_pdf(resume_id: str):
    """导出简历为PDF"""
    if resume_id not in resumes_data:
        raise HTTPException(status_code=404, detail="简历未找到")
    
    # 实际应用中，这里应该生成PDF文件并返回
    # 这里简单返回HTML内容
    
    return {"content": resumes_data[resume_id]["html"], "message": "PDF生成功能尚未实现"}

@router.post("/resumes/upload")
async def upload_resume(file: UploadFile = File(...)):
    """上传简历文件进行优化"""
    try:
        # 生成唯一ID
        resume_id = str(uuid.uuid4())
        
        # 读取文件内容
        contents = await file.read()
        
        # 模拟简历解析
        html_content = f"""
        <h1>已上传的简历</h1>
        <p>文件名: {file.filename}</p>
        <p>文件大小: {len(contents)} 字节</p>
        <p>简历内容解析功能尚未实现</p>
        """
        
        # 保存简历数据
        resumes_data[resume_id] = {
            "id": resume_id,
            "file_name": file.filename,
            "html": html_content,
            "data": {}
        }
        
        return {"resumeId": resume_id, "data": html_content}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"上传简历失败: {str(e)}") 