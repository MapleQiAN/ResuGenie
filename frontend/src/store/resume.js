import { defineStore } from 'pinia'
import { resumeApi } from '@/api'

export const useResumeStore = defineStore('resume', {
  state: () => ({
    // 简历表单数据
    resumeForm: {
      // 基本信息
      basics: {
        name: '',
        label: '',
        email: '',
        phone: '',
        location: '',
        profiles: [],
        summary: ''
      },
      // 工作经历
      work: [],
      // 教育经历
      education: [],
      // 项目经历
      projects: [],
      // 技能
      skills: [],
      // 证书与奖项
      certificates: [],
      // 语言能力
      languages: []
    },
    // 当前选择的简历模板
    selectedTemplate: null,
    // 可用的简历模板
    templates: [],
    // 简历预览数据
    resumePreview: null,
    // 简历优化建议
    optimizationSuggestions: [],
    // 文件上传状态
    fileUpload: {
      loading: false,
      progress: 0,
      file: null
    },
    // 简历生成状态
    generating: false,
    // 优化状态
    optimizing: false,
    // 当前处理的简历ID
    currentResumeId: null,
    // AI模型配置
    aiModel: {
      selectedModel: 'gpt-3.5-turbo',
      temperature: 0.7,
      maxTokens: 2000,
      customPrompt: '',
      focusAreas: [],
      apiConfig: {
        openaiKey: '',
        openaiBase: 'https://api.openai.com/v1',
        deepseekKey: '',
        deepseekBase: 'https://api.deepseek.com/v1',
        ollamaBase: 'http://localhost:11434/api',
        useCustomApi: false
      }
    }
  }),
  
  getters: {
    // 判断简历表单是否为空
    isResumeFormEmpty: (state) => {
      return !state.resumeForm.basics.name && 
             state.resumeForm.work.length === 0 && 
             state.resumeForm.education.length === 0
    },
    
    // 获取简历预览状态
    hasResumePreview: (state) => {
      return state.resumePreview !== null
    }
  },
  
  actions: {
    // 重置简历表单
    resetResumeForm() {
      this.resumeForm = {
        basics: {
          name: '',
          label: '',
          email: '',
          phone: '',
          location: '',
          profiles: [],
          summary: ''
        },
        work: [],
        education: [],
        projects: [],
        skills: [],
        certificates: [],
        languages: []
      }
    },
    
    // 设置简历表单数据
    setResumeForm(data) {
      this.resumeForm = { ...data }
    },
    
    // 加载简历模板
    async loadTemplates() {
      try {
        this.templates = await resumeApi.getTemplates()
        if (this.templates.length > 0 && !this.selectedTemplate) {
          this.selectedTemplate = this.templates[0].id
        }
        return this.templates
      } catch (error) {
        console.error('加载简历模板失败:', error)
        throw error
      }
    },
    
    // 选择简历模板
    selectTemplate(templateId) {
      this.selectedTemplate = templateId
    },
    
    // 设置AI模型配置
    setAiModel(modelConfig) {
      this.aiModel = { ...this.aiModel, ...modelConfig }
    },
    
    // 创建简历
    async createResume() {
      try {
        this.generating = true
        
        const response = await resumeApi.createResume({
          resumeData: this.resumeForm,
          templateId: this.selectedTemplate
        })
        
        this.resumePreview = response.data
        this.currentResumeId = response.resumeId
        
        return response
      } catch (error) {
        console.error('创建简历失败:', error)
        throw error
      } finally {
        this.generating = false
      }
    },
    
    // 上传简历文件进行优化
    async uploadResumeFile(file) {
      try {
        this.fileUpload.loading = true
        this.fileUpload.file = file
        
        const response = await resumeApi.uploadResume(file)
        
        this.resumePreview = response.data
        this.currentResumeId = response.resumeId
        
        return response
      } catch (error) {
        console.error('上传简历文件失败:', error)
        throw error
      } finally {
        this.fileUpload.loading = false
      }
    },
    
    // 获取简历优化建议
    async getOptimizationSuggestions() {
      try {
        if (!this.currentResumeId) {
          throw new Error('没有找到当前简历ID')
        }
        
        this.optimizing = true
        
        const response = await resumeApi.getOptimizationSuggestions(this.currentResumeId)
        this.optimizationSuggestions = response.suggestions
        
        return this.optimizationSuggestions
      } catch (error) {
        console.error('获取简历优化建议失败:', error)
        throw error
      } finally {
        this.optimizing = false
      }
    },
    
    // 应用优化建议
    async applyOptimizationSuggestion(suggestionId) {
      try {
        if (!this.currentResumeId) {
          throw new Error('没有找到当前简历ID')
        }
        
        const response = await resumeApi.applyOptimizationSuggestion(
          this.currentResumeId,
          suggestionId
        )
        
        // 更新简历预览
        this.resumePreview = response.data
        
        // 更新优化建议列表
        const index = this.optimizationSuggestions.findIndex(s => s.id === suggestionId)
        if (index !== -1) {
          this.optimizationSuggestions[index].applied = true
        }
        
        return response
      } catch (error) {
        console.error('应用优化建议失败:', error)
        throw error
      }
    },
    
    // 导出简历为PDF
    async exportResumePDF() {
      try {
        if (!this.currentResumeId) {
          throw new Error('没有找到当前简历ID')
        }
        
        const response = await resumeApi.exportResumePDF(this.currentResumeId)
        return response
      } catch (error) {
        console.error('导出简历失败:', error)
        throw error
      }
    }
  }
}) 