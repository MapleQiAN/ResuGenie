import axios from 'axios'
import { useMessage } from 'naive-ui'

// 读取环境变量中的API基础路径，默认为本地开发地址
const BASE_API_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api'

// 创建axios实例
const api = axios.create({
  baseURL: BASE_API_URL,
  timeout: 30000, // 请求超时时间
  headers: {
    'Content-Type': 'application/json'
  }
})

// 请求拦截器
api.interceptors.request.use(
  config => {
    // 可以在发送请求前做一些处理，例如添加token
    // const token = localStorage.getItem('token')
    // if (token) {
    //   config.headers['Authorization'] = `Bearer ${token}`
    // }
    return config
  },
  error => {
    return Promise.reject(error)
  }
)

// 响应拦截器
api.interceptors.response.use(
  response => {
    // 如果后端返回的是二进制数据，直接返回
    if (response.config.responseType === 'blob' || response.config.responseType === 'arraybuffer') {
      return response
    }
    
    // 正常响应，返回数据
    return response.data
  },
  error => {
    const message = useMessage()
    
    // 处理网络错误
    if (!error.response) {
      message.error('网络错误，请检查您的网络连接')
      return Promise.reject(error)
    }
    
    // 处理HTTP状态错误
    const status = error.response.status
    switch (status) {
      case 400:
        message.error('请求参数错误')
        break
      case 401:
        message.error('未授权，请重新登录')
        // 可以在此处跳转到登录页
        // router.push('/login')
        break
      case 403:
        message.error('拒绝访问')
        break
      case 404:
        message.error('请求的资源不存在')
        break
      case 500:
        message.error('服务器内部错误')
        break
      default:
        message.error(`请求失败: ${error.response.data.message || '未知错误'}`)
    }
    
    return Promise.reject(error)
  }
)

// 简历相关API
export const resumeApi = {
  // 创建简历
  createResume: (data) => api.post('/resumes', data),
  
  // 上传简历文件进行优化
  uploadResume: (file) => {
    const formData = new FormData()
    formData.append('file', file)
    return api.post('/resumes/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
  },
  
  // 获取简历优化建议
  getOptimizationSuggestions: (resumeId) => api.get(`/resumes/${resumeId}/suggestions`),
  
  // 应用优化建议
  applyOptimizationSuggestion: (resumeId, suggestionId) => api.post(`/resumes/${resumeId}/suggestions/${suggestionId}/apply`),
  
  // 导出简历为PDF
  exportResumePDF: (resumeId) => api.get(`/resumes/${resumeId}/export/pdf`, { responseType: 'blob' }),
  
  // 获取简历模板列表
  getTemplates: () => api.get('/resume-templates')
}

export default api 