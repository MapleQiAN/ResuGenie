import { defineStore } from 'pinia'
import llmApi from '../api/llm'

export const useLlmStore = defineStore('llm', {
  state: () => ({
    models: [],
    selectedModel: '',
    loading: false,
    error: null,
    messages: [],
  }),
  
  getters: {
    availableModels: (state) => state.models,
    currentModel: (state) => state.selectedModel,
    isLoading: (state) => state.loading,
    getMessages: (state) => state.messages,
  },
  
  actions: {
    // 获取可用模型列表
    async fetchModels() {
      try {
        this.loading = true
        const response = await llmApi.getModels()
        if (response && response.models) {
          this.models = response.models
          // 默认选择第一个模型
          if (this.models.length > 0 && !this.selectedModel) {
            this.selectedModel = this.models[0]
          }
        }
        this.loading = false
      } catch (error) {
        this.error = error.message || '获取模型列表失败'
        this.loading = false
      }
    },
    
    // 设置当前选中的模型
    setModel(model) {
      this.selectedModel = model
    },
    
    // 添加消息
    addMessage(message) {
      this.messages.push(message)
    },
    
    // 清空消息历史
    clearMessages() {
      this.messages = []
    },
    
    // 发送消息并获取回复
    async sendMessage(content) {
      if (!content.trim() || !this.selectedModel) return
      
      // 添加用户消息
      const userMessage = {
        role: 'user',
        content: content
      }
      this.addMessage(userMessage)
      
      // 准备发送请求
      try {
        this.loading = true
        
        const requestData = {
          model: this.selectedModel,
          messages: this.messages,
          temperature: 0.7
        }
        
        const response = await llmApi.chatCompletion(requestData)
        
        // 添加AI回复
        if (response && response.choices && response.choices.length > 0) {
          const assistantMessage = response.choices[0].message
          this.addMessage(assistantMessage)
        }
        
        this.loading = false
        return response
      } catch (error) {
        this.error = error.message || '发送消息失败'
        this.loading = false
        
        // 添加错误消息
        const errorMessage = {
          role: 'assistant',
          content: `抱歉，发生错误：${this.error}`
        }
        this.addMessage(errorMessage)
      }
    }
  }
}) 