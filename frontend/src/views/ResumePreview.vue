<template>
  <div class="resume-preview-page">
    <div class="page-container">
      <!-- 左侧简历预览区域 -->
      <div class="resume-section">
        <n-card title="简历预览" class="resume-card">
          <template #header-extra>
            <n-button-group>
              <n-button size="small" @click="exportPDF">导出PDF</n-button>
              <n-button size="small" @click="optimizeResume" :loading="optimizing">一键优化</n-button>
              <n-button size="small" @click="editMode = !editMode">
                {{ editMode ? '预览模式' : '编辑模式' }}
              </n-button>
            </n-button-group>
          </template>
          
          <div v-if="!resumeContent" class="empty-state">
            <n-empty description="暂无简历内容">
              <template #extra>
                <n-button @click="generateSampleResume">生成示例简历</n-button>
              </template>
            </n-empty>
          </div>
          
          <div v-else class="resume-container">
            <div v-if="editMode" class="edit-mode">
              <n-input
                v-model:value="resumeContent"
                type="textarea"
                :autosize="{ minRows: 15, maxRows: 30 }"
                placeholder="编辑简历内容..."
              />
            </div>
            <div v-else class="preview-mode">
              <div class="resume-content" v-html="resumeContentHtml"></div>
            </div>
          </div>
        </n-card>
      </div>
      
      <!-- 右侧AI聊天区域 -->
      <div class="chat-section">
        <n-card title="AI优化助手" class="chat-card">
          <template #header-extra>
            <model-selector @change="handleModelChange" />
          </template>
          
          <div class="chat-container">
            <div class="messages" ref="messagesContainer">
              <div class="message system">
                <div class="message-content">
                  <p>👋 你好！我是您的简历优化助手。我可以帮您：</p>
                  <ul>
                    <li>润色简历语言和表达</li>
                    <li>优化简历结构和内容</li>
                    <li>提供专业建议和改进方向</li>
                  </ul>
                  <p>请告诉我您需要哪方面的帮助？</p>
                </div>
              </div>
              
              <div v-for="(msg, index) in messages" :key="index" class="message" :class="msg.role">
                <div class="message-content" v-html="formatMessage(msg.content)"></div>
              </div>
              
              <div v-if="isLoading" class="message loading">
                <div class="message-content">
                  <n-spin size="small" />
                  <span class="loading-text">AI思考中...</span>
                </div>
              </div>
            </div>
            
            <div class="input-area">
              <n-input
                v-model:value="userInput"
                type="textarea"
                :autosize="{ minRows: 1, maxRows: 4 }"
                placeholder="输入问题或建议..."
                :disabled="isLoading"
                @keydown.enter.ctrl.prevent="sendMessage"
              />
              
              <div class="action-buttons">
                <n-button type="primary" :disabled="isLoading || !userInput.trim()" @click="sendMessage">
                  发送
                </n-button>
                <n-button :disabled="isLoading || messages.length === 0" @click="clearChat">
                  清空对话
                </n-button>
              </div>
            </div>
          </div>
        </n-card>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted, nextTick, inject } from 'vue'
import { useMessage } from 'naive-ui'
import { marked } from 'marked'
import { useLlmStore } from '../store/llm'
import { resumeApi } from '../api'
import ModelSelector from '../components/common/ModelSelector.vue'

const message = useMessage()
const dialog = inject('dialog') // 注入对话框服务
const llmStore = useLlmStore()

// 简历内容
const resumeContent = ref('')
const editMode = ref(false)
const optimizing = ref(false)

// 聊天相关状态
const userInput = ref('')
const messages = ref([])
const isLoading = ref(false)
const messagesContainer = ref(null)

// 转换Markdown为HTML
const resumeContentHtml = computed(() => {
  if (!resumeContent.value) return ''
  return marked(resumeContent.value)
})

// 监听消息变化，自动滚动到底部
watch(() => messages.value.length, async () => {
  await nextTick()
  if (messagesContainer.value) {
    messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
  }
})

// 处理模型变更
const handleModelChange = (model) => {
  message.info(`已选择模型: ${model}`)
}

// 格式化消息内容（处理换行和链接等）
const formatMessage = (content) => {
  if (!content) return ''
  // 将换行符转换为<br>
  let formatted = content.replace(/\n/g, '<br>')
  // 可以添加更多格式化逻辑，如链接检测等
  return formatted
}

// 发送消息
const sendMessage = async () => {
  if (!userInput.value.trim()) return
  
  // 添加用户消息
  messages.value.push({
    role: 'user',
    content: userInput.value
  })
  
  const userQuestion = userInput.value
  userInput.value = ''
  
  // 自动滚动到底部
  await nextTick()
  if (messagesContainer.value) {
    messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
  }
  
  isLoading.value = true
  
  try {
    // 构建消息列表，包含之前的对话历史
    const chatMessages = messages.value.map(msg => ({
      role: msg.role,
      content: msg.content
    }))
    
    // 如果有简历内容但还没有在消息中提供给AI
    if (resumeContent.value && !messagesIncludeResume()) {
      // 在用户问题之前插入系统消息，提供简历内容
      chatMessages.unshift({
        role: 'system',
        content: `以下是用户的简历内容，请基于这些内容提供优化建议：\n\n${resumeContent.value}`
      })
    }
    
    // 使用简历专用API发送请求
    const response = await resumeApi.resumeChatCompletion({
      model: llmStore.currentModel || 'gpt-3.5-turbo',
      messages: chatMessages,
      temperature: 0.7
    })
    
    if (response && response.choices && response.choices.length > 0) {
      const aiResponse = response.choices[0].message.content
      
      // 添加AI回复
      messages.value.push({
        role: 'assistant',
        content: aiResponse
      })
      
      // 如果回复中明确包含了更新后的完整简历，可以自动更新简历内容
      if (aiResponse.includes('以下是优化后的简历') || aiResponse.includes('以下是修改后的简历')) {
        const updatedResume = extractResumeContent(aiResponse)
        if (updatedResume) {
          resumeContent.value = updatedResume
          message.success('简历内容已自动更新')
        }
      }
    }
  } catch (error) {
    console.error('发送消息失败:', error)
    message.error('发送失败: ' + (error.message || '未知错误'))
    
    // 添加错误消息
    messages.value.push({
      role: 'assistant',
      content: '抱歉，我暂时无法回答您的问题，请稍后再试。'
    })
  } finally {
    isLoading.value = false
  }
}

// 检查消息历史中是否已经包含简历内容
const messagesIncludeResume = () => {
  return messages.value.some(msg => 
    msg.role === 'system' && msg.content.includes('以下是用户的简历内容')
  )
}

// 从AI回复中提取更新的简历内容
const extractResumeContent = (content) => {
  // 这里可以添加更复杂的逻辑来提取更新后的简历内容
  // 简单实现：如果包含明确的标记，提取这些标记之间的内容
  const startMarkers = ['以下是优化后的简历', '以下是修改后的简历', '更新后的简历：', '```markdown']
  const endMarkers = ['```']
  
  let extractedContent = content
  
  for (const marker of startMarkers) {
    const startIdx = content.indexOf(marker)
    if (startIdx !== -1) {
      extractedContent = content.substring(startIdx + marker.length).trim()
      break
    }
  }
  
  for (const marker of endMarkers) {
    const endIdx = extractedContent.lastIndexOf(marker)
    if (endIdx !== -1) {
      extractedContent = extractedContent.substring(0, endIdx).trim()
      break
    }
  }
  
  return extractedContent
}

// 清空聊天
const clearChat = () => {
  messages.value = []
}

// 导出PDF
const exportPDF = async () => {
  if (!resumeContent.value) {
    message.warning('没有简历内容可导出')
    return
  }
  
  message.success('简历已导出为PDF（演示）')
  // 实际中应该调用后端API来生成并下载PDF
}

// 生成示例简历
const generateSampleResume = async () => {
  isLoading.value = true
  message.loading('正在生成示例简历...')
  
  try {
    const prompt = `请帮我创建一份专业的软件工程师个人简历，包含个人信息、教育背景、工作经历、技能和项目经历。使用Markdown格式，确保内容专业，长度适中。请直接输出简历内容，不要有其他解释。`
    
    // 发送到后端API
    const response = await llmStore.sendMessage(prompt)
    
    if (response && response.choices && response.choices.length > 0) {
      const aiResponse = response.choices[0].message.content
      resumeContent.value = aiResponse
      message.success('示例简历生成成功')
    } else {
      message.error('生成示例简历失败')
    }
  } catch (error) {
    console.error('生成示例简历出错：', error)
    message.error(`生成示例简历失败：${error.message || '未知错误'}`)
  } finally {
    isLoading.value = false
  }
}

// 一键优化简历
const optimizeResume = async () => {
  if (!resumeContent.value) {
    message.warning('没有可优化的内容，请先生成或输入简历')
    return
  }
  
  try {
    optimizing.value = true
    
    // 弹出对话框询问目标职位
    const jobPosition = await new Promise((resolve) => {
      const d = dialog.warning({
        title: '优化简历',
        content: '请输入您的目标职位，以便AI更有针对性地优化简历',
        positiveText: '确定',
        negativeText: '取消',
        inputProps: {
          value: '',
          placeholder: '如：前端开发工程师',
          onUpdateValue: (val) => {
            d.content = `请输入您的目标职位，以便AI更有针对性地优化简历: ${val}`
          }
        },
        onPositiveClick: () => {
          const inputValue = d.content.split(':')[1]?.trim() || ''
          resolve(inputValue)
          return true
        },
        onNegativeClick: () => {
          resolve('')
          return true
        }
      })
    })
    
    if (!jobPosition) {
      message.info('已取消优化')
      return
    }
    
    // 调用API优化简历内容
    const response = await resumeApi.optimizeResumeContent(
      resumeContent.value,
      jobPosition
    )
    
    if (response && response.optimized) {
      // 更新简历内容
      resumeContent.value = response.optimized
      message.success('简历已成功优化！')
      
      // 添加系统消息到聊天
      messages.value.push({
        role: 'system',
        content: '简历已使用AI进行了优化。有任何问题可以随时向我咨询。'
      })
    } else {
      message.error('优化失败：未能获取优化内容')
    }
  } catch (error) {
    console.error('简历优化错误：', error)
    message.error('优化失败：' + (error.message || '未知错误'))
  } finally {
    optimizing.value = false
  }
}

onMounted(async () => {
  // 初始化模型
  await llmStore.fetchModels()
})
</script>

<style scoped>
.resume-preview-page {
  padding: 20px;
  min-height: calc(100vh - 70px);
  background-color: var(--bg-color-light);
}

.page-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  max-width: 1280px;
  margin: 0 auto;
}

.resume-card, .chat-card {
  height: 100%;
  display: flex;
  flex-direction: column;
}

.resume-container {
  margin-top: 15px;
  overflow: auto;
}

.empty-state {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 300px;
}

.edit-mode {
  height: 100%;
}

.preview-mode {
  padding: 20px;
  border: 1px solid #eee;
  border-radius: 8px;
  background-color: white;
  min-height: 500px;
  max-height: 700px;
  overflow-y: auto;
}

.resume-content {
  font-family: 'Arial', sans-serif;
}

:deep(.resume-content h1) {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  border-bottom: 1px solid #eee;
  padding-bottom: 0.5rem;
}

:deep(.resume-content h2) {
  font-size: 1.2rem;
  margin-top: 1.2rem;
  margin-bottom: 0.5rem;
  color: #444;
}

:deep(.resume-content ul) {
  padding-left: 1.5rem;
  margin-bottom: 1rem;
}

:deep(.resume-content p) {
  margin-bottom: 0.6rem;
  line-height: 1.5;
}

.chat-container {
  display: flex;
  flex-direction: column;
  height: 100%;
  margin-top: 10px;
}

.messages {
  flex-grow: 1;
  overflow-y: auto;
  padding: 10px;
  max-height: 500px;
  border: 1px solid #eee;
  border-radius: 8px;
  background-color: #f9f9f9;
  margin-bottom: 15px;
}

.message {
  margin-bottom: 15px;
  padding: 10px 15px;
  border-radius: 8px;
  max-width: 85%;
  position: relative;
}

.message.user {
  background-color: #e8f4ff;
  align-self: flex-end;
  margin-left: auto;
}

.message.assistant {
  background-color: white;
  align-self: flex-start;
  border: 1px solid #eee;
}

.message.system {
  background-color: #f5f5f5;
  border: 1px dashed #ddd;
  margin-left: auto;
  margin-right: auto;
  max-width: 95%;
  margin-bottom: 25px;
}

.message.loading {
  background-color: transparent;
  border: none;
}

.message-content {
  word-break: break-word;
  line-height: 1.5;
}

.loading-text {
  margin-left: 10px;
  color: #888;
}

.input-area {
  margin-top: auto;
}

.action-buttons {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 10px;
}

/* 响应式布局 */
@media (max-width: 900px) {
  .page-container {
    grid-template-columns: 1fr;
  }
  
  .resume-card, .chat-card {
    margin-bottom: 20px;
  }
}
</style> 