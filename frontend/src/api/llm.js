import api from './index'

// LLM模型相关API
const llmApi = {
  // 获取可用模型列表
  getModels: () => api.get('/v1/chat/models'),
  
  // 进行聊天补全
  chatCompletion: (data) => api.post('/v1/chat/completions', data),
}

export default llmApi 