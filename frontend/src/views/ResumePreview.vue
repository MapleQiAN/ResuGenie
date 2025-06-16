<template>
  <div class="resume-preview-page">
    <div class="page-container">
      <!-- 左侧简历预览区域 -->
      <div class="resume-section">
        <n-card title="简历预览" class="resume-card">
          <template #header>
            <div class="card-header">
              <div class="card-title">
                <n-icon size="20" class="header-icon">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><path fill="none" d="M0 0h24v24H0z"/><path d="M20 22H4a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1h16a1 1 0 0 1 1 1v18a1 1 0 0 1-1 1zm-1-2V4H5v16h14zM8 7h8v2H8V7zm0 4h8v2H8v-2zm0 4h5v2H8v-2z" fill="currentColor"/></svg>
                </n-icon>
                <span>简历预览</span>
              </div>
            </div>
          </template>
          <template #header-extra>
            <n-button-group class="action-group">
              <n-button size="small" @click="exportPDF" class="action-btn">
                <template #icon>
                  <n-icon><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16" height="16"><path fill="none" d="M0 0h24v24H0z"/><path d="M12 16H8V8h4v8zm2 0V8h4v8h-4zm5-12H5v16h14V4zM3 2.992C3 2.444 3.447 2 3.999 2H16l5 5v13.993A1 1 0 0 1 20.007 22H3.993A1 1 0 0 1 3 21.008V2.992z" fill="currentColor"/></svg></n-icon>
                </template>
                导出PDF
              </n-button>
              <n-button size="small" @click="optimizeResume" :loading="optimizing" class="action-btn">
                <template #icon>
                  <n-icon><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16" height="16"><path fill="none" d="M0 0h24v24H0z"/><path d="M18.364 5.636L16.95 7.05A7 7 0 1 0 19 12h2a9 9 0 1 1-2.636-6.364z" fill="currentColor"/><path d="M15 12h-2V7h-2v7h4v-2z" fill="currentColor"/></svg></n-icon>
                </template>
                一键优化
              </n-button>
              <n-button size="small" @click="editMode = !editMode" class="action-btn">
                <template #icon>
                  <n-icon><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16" height="16"><path fill="none" d="M0 0h24v24H0z"/><path d="M16.757 3l-7.466 7.466.008 4.247 4.238-.007L21 7.243V20a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h12.757zm3.728-.9L21.9 3.516l-9.192 9.192-1.412.003-.002-1.417 9.192-9.194z" fill="currentColor"/></svg></n-icon>
                </template>
                {{ editMode ? '预览模式' : '编辑模式' }}
              </n-button>
            </n-button-group>
          </template>
          
          <div v-if="!resumeContent" class="empty-state">
            <n-empty description="暂无简历内容" class="empty-content">
              <template #icon>
                <n-icon size="48" class="empty-icon">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="48" height="48"><path fill="none" d="M0 0h24v24H0z"/><path d="M20 22H4a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1h16a1 1 0 0 1 1 1v18a1 1 0 0 1-1 1zm-1-2V4H5v16h14zM8 7h8v2H8V7zm0 4h8v2H8v-2zm0 4h8v2H8v-2z" fill="currentColor"/></svg>
                </n-icon>
              </template>
              <template #extra>
                <n-button @click="generateSampleResume" :loading="generatingSample" type="primary" class="generate-btn">
                  <template #icon>
                    <n-icon><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16" height="16"><path fill="none" d="M0 0h24v24H0z"/><path d="M24 12l-5.657 5.657-1.414-1.414L21.172 12l-4.243-4.243 1.414-1.414L24 12zM2.828 12l4.243 4.243-1.414 1.414L0 12l5.657-5.657L7.07 7.757 2.828 12zm6.96 9H7.66l6.552-18h2.128L9.788 21z" fill="currentColor"/></svg></n-icon>
                  </template>
                  生成示例简历
                </n-button>
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
                class="resume-editor"
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
          <template #header>
            <div class="card-header">
              <div class="card-title">
                <n-icon size="20" class="header-icon">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><path fill="none" d="M0 0h24v24H0z"/><path d="M2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10H2l2.929-2.929A9.969 9.969 0 0 1 2 12zm4.828 8H12a8 8 0 1 0-8-8c0 2.152.851 4.165 2.343 5.657l1.414 1.414-.929.929zM8 13h8a4 4 0 1 1-8 0z" fill="currentColor"/></svg>
                </n-icon>
                <span>AI优化助手</span>
              </div>
            </div>
          </template>
          <template #header-extra>
            <div class="model-selector-wrapper">
              <model-selector @change="handleModelChange" />
            </div>
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
                  <span class="loading-text">AI思考中</span>
                  <span class="loading-dots"><span>.</span><span>.</span><span>.</span></span>
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
                class="chat-input"
              />
              
              <div class="action-buttons">
                <n-tooltip trigger="hover" placement="top">
                  <template #trigger>
                    <n-button :disabled="isLoading || messages.length === 0" @click="clearChat" class="clear-btn">
                      <template #icon>
                        <n-icon><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16" height="16"><path fill="none" d="M0 0h24v24H0z"/><path d="M17 6h5v2h-2v13a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V8H2V6h5V3a1 1 0 0 1 1-1h8a1 1 0 0 1 1 1v3zm1 2H6v12h12V8zm-9 3h2v6H9v-6zm4 0h2v6h-2v-6zM9 4v2h6V4H9z" fill="currentColor"/></svg></n-icon>
                      </template>
                    </n-button>
                  </template>
                  清空对话
                </n-tooltip>
                
                <n-button type="primary" :disabled="isLoading || !userInput.trim()" @click="sendMessage" class="send-btn">
                  <template #icon>
                    <n-icon><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="16" height="16"><path fill="none" d="M0 0h24v24H0z"/><path d="M3 13h6v-2H3V1.846a.5.5 0 0 1 .741-.438l18.462 10.154a.5.5 0 0 1 0 .876L3.741 22.592A.5.5 0 0 1 3 22.154V13z" fill="currentColor"/></svg></n-icon>
                  </template>
                  发送
                </n-button>
              </div>
            </div>
          </div>
        </n-card>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch, onMounted, nextTick } from 'vue'
import { useMessage, createDiscreteApi } from 'naive-ui'
import { marked } from 'marked'
import { useLlmStore } from '../store/llm'
import { resumeApi } from '../api'
import ModelSelector from '../components/common/ModelSelector.vue'

const message = useMessage()
const llmStore = useLlmStore()

// 使用createDiscreteApi创建对话框API
const { dialog } = createDiscreteApi(['dialog'])

// 简历内容
const resumeContent = ref('')
const editMode = ref(false)
const optimizing = ref(false)
const generatingSample = ref(false)

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
  scrollToBottom()
})

// 滚动到消息底部的函数
const scrollToBottom = () => {
  if (messagesContainer.value) {
    const container = messagesContainer.value
    // 使用平滑滚动效果
    container.scrollTo({
      top: container.scrollHeight,
      behavior: 'smooth'
    })
  }
}

// 处理模型变更
const handleModelChange = (model) => {
  message.info(`已选择模型: ${model}`)
}

// 格式化消息内容（处理换行和链接等）
const formatMessage = (content) => {
  if (!content) return ''
  // 使用marked将Markdown转换为HTML
  try {
    const html = marked(content)
    return html
  } catch (e) {
    // 降级处理：如果marked解析失败，至少处理基本换行
    console.error('Markdown解析失败:', e)
    return content.replace(/\n/g, '<br>')
  }
}

// 发送消息
const sendMessage = async () => {
  if (!userInput.value.trim() || isLoading.value) return
  
  // 添加用户消息
  messages.value.push({
    role: 'user',
    content: userInput.value
  })
  
  const userQuestion = userInput.value
  userInput.value = ''
  
  // 自动滚动到底部
  await nextTick()
  scrollToBottom()
  
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
        content: `以下是用户的简历内容，请基于这些内容提供专业的优化建议：\n\n${resumeContent.value}`
      })
    }
    
    // 添加额外的系统提示，指导AI提供更专业的回答
    chatMessages.unshift({
      role: 'system',
      content: `你是一位专业的简历优化顾问和职业指导专家。你的目标是帮助用户改进简历，使其更具吸引力、更有竞争力。
      请提供具体、可操作的建议，突出用户的优势和成就。回答应专业、有深度，并尽可能提供行业特定的指导。
      如果用户要求优化整个简历，请提供完整的优化后版本，使用Markdown格式。`
    })
    
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
      if (aiResponse.includes('以下是优化后的简历') || 
          aiResponse.includes('以下是修改后的简历') || 
          aiResponse.includes('更新后的简历') ||
          aiResponse.includes('```markdown')) {
        const updatedResume = extractResumeContent(aiResponse)
        if (updatedResume && updatedResume !== resumeContent.value) {
          // 显示确认对话框，询问用户是否要更新简历
          const result = await dialog.info({
            title: '更新简历内容',
            content: '检测到AI回复中包含完整的简历内容，是否要更新当前简历？',
            positiveText: '更新',
            negativeText: '保持原样'
          })
          
          if (result) {
            resumeContent.value = updatedResume
            message.success('简历内容已更新')
          }
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
    scrollToBottom()
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
  // 使用正则表达式提取Markdown代码块内的内容
  const markdownRegex = /```(?:markdown)?\s*([\s\S]*?)```/i
  const markdownMatch = content.match(markdownRegex)
  
  if (markdownMatch && markdownMatch[1]) {
    return markdownMatch[1].trim()
  }
  
  // 如果没有找到Markdown代码块，尝试查找常见的标记
  const startMarkers = [
    '以下是优化后的简历',
    '以下是修改后的简历',
    '更新后的简历：',
    '优化后的完整简历：'
  ]
  
  let extractedContent = content
  let startIdx = -1
  
  // 查找开始标记
  for (const marker of startMarkers) {
    const idx = content.indexOf(marker)
    if (idx !== -1 && (startIdx === -1 || idx < startIdx)) {
      startIdx = idx + marker.length
    }
  }
  
  // 如果找到开始标记
  if (startIdx !== -1) {
    extractedContent = content.substring(startIdx).trim()
    
    // 查找结束位置（下一个明显的标记或问题）
    const endMarkers = [
      '希望这份优化', 
      '如果您有任何', 
      '您觉得如何', 
      '这样的修改'
    ]
    
    for (const marker of endMarkers) {
      const endIdx = extractedContent.indexOf(marker)
      if (endIdx !== -1) {
        extractedContent = extractedContent.substring(0, endIdx).trim()
        break
      }
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
  if (generatingSample.value) return
  
  generatingSample.value = true
  message.loading('正在生成示例简历...')
  
  try {
    // 显示职位选择对话框
    const jobOptions = [
      { label: '前端开发工程师', value: 'frontend' },
      { label: '后端开发工程师', value: 'backend' },
      { label: '全栈开发工程师', value: 'fullstack' },
      { label: '数据分析师', value: 'data_analyst' },
      { label: '产品经理', value: 'product_manager' },
      { label: '用户体验设计师', value: 'ux_designer' }
    ]
    
    let selectedJob = 'frontend'
    
    // 创建职位选择的单选按钮组
    const radioGroup = document.createElement('div')
    radioGroup.style.margin = '10px 0'
    radioGroup.style.display = 'flex'
    radioGroup.style.flexDirection = 'column'
    radioGroup.style.gap = '8px'
    
    jobOptions.forEach(job => {
      const radio = document.createElement('div')
      radio.style.display = 'flex'
      radio.style.alignItems = 'center'
      radio.style.gap = '8px'
      radio.style.padding = '6px'
      radio.style.border = '1px solid transparent'
      radio.style.borderRadius = '4px'
      radio.style.cursor = 'pointer'
      radio.style.transition = 'all 0.2s'
      
      const input = document.createElement('input')
      input.type = 'radio'
      input.name = 'jobType'
      input.value = job.value
      input.id = `job-${job.value}`
      input.checked = job.value === 'frontend'
      input.style.cursor = 'pointer'
      
      const label = document.createElement('label')
      label.htmlFor = `job-${job.value}`
      label.textContent = job.label
      label.style.cursor = 'pointer'
      label.style.flex = '1'
      
      radio.appendChild(input)
      radio.appendChild(label)
      
      // 点击整行选择
      radio.addEventListener('click', () => {
        input.checked = true
        selectedJob = job.value
        
        // 更新所有样式
        radioGroup.querySelectorAll('div').forEach(el => {
          el.style.backgroundColor = 'transparent'
          el.style.borderColor = 'transparent'
        })
        
        // 设置选中项样式
        radio.style.backgroundColor = '#eef4ff'
        radio.style.borderColor = '#d1e0ff'
      })
      
      radioGroup.appendChild(radio)
    })
    
    // 显示确认对话框
    await dialog.info({
      title: '选择简历模板类型',
      content: () => {
        return [
          '请选择要生成的简历类型：',
          radioGroup
        ]
      },
      positiveText: '生成',
      negativeText: '取消',
      onPositiveClick: () => {
        // 获取选择的职位类型
        const selected = document.querySelector('input[name="jobType"]:checked')
        if (selected) {
          selectedJob = selected.value
        }
        return true
      },
      onNegativeClick: () => {
        generatingSample.value = false
        message.info('已取消生成')
        return true
      }
    })
    
    if (!generatingSample.value) {
      return
    }
    
    message.loading('正在生成专业简历，请稍候...')
    
    // 根据选择的职位构建提示
    let jobTitle = jobOptions.find(job => job.value === selectedJob)?.label || '软件工程师'
    
    const prompt = `请帮我创建一份专业的${jobTitle}个人简历，包含以下部分：
    1. 个人信息：姓名、联系方式、专业网站/GitHub等
    2. 职业概述：简短介绍核心能力和经验
    3. 技能列表：相关的专业技能
    4. 工作经历：至少2-3个职位，包含成就和贡献
    5. 教育背景：学历信息
    6. 项目经验：至少2-3个相关项目，描述技术栈和成果
    
    使用Markdown格式，确保内容专业，长度适中，重点突出相关技能和成就。
    请直接输出简历内容，不要有其他解释。`
    
    // 发送到后端API
    const response = await llmStore.sendMessage(prompt)
    
    if (response && response.choices && response.choices.length > 0) {
      const aiResponse = response.choices[0].message.content
      resumeContent.value = aiResponse
      message.success('示例简历生成成功')
      
      // 切换到预览模式
      if (editMode.value) {
        editMode.value = false
      }
    } else {
      message.error('生成示例简历失败')
    }
  } catch (error) {
    console.error('生成示例简历出错：', error)
    message.error(`生成示例简历失败：${error.message || '未知错误'}`)
  } finally {
    generatingSample.value = false
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
    
    // 使用临时变量存储职位名称
    let jobPosition = ''
    
    // 创建并显示输入框
    const input = document.createElement('input')
    input.type = 'text'
    input.placeholder = '如：前端开发工程师'
    input.style.width = '100%'
    input.style.padding = '8px'
    input.style.marginTop = '8px'
    input.style.borderRadius = '4px'
    input.style.border = '1px solid #d9d9d9'
    
    // 显示确认对话框
    const result = await dialog.info({
      title: '优化简历',
      content: () => {
        return [
          '请输入您的目标职位，以便AI更有针对性地优化简历',
          input
        ]
      },
      positiveText: '确定',
      negativeText: '取消',
      onPositiveClick: () => {
        jobPosition = input.value
        return true
      },
      onNegativeClick: () => {
        return true
      }
    })
    
    if (!jobPosition) {
      message.info('已取消优化')
      optimizing.value = false
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
:root {
  --primary-color: #2d6cdf;
  --primary-light: #eef4ff;
  --secondary-color: #6c5ce7;
  --accent-color: #00c9a7;
  --text-primary: #2c3e50;
  --text-secondary: #596275;
  --bg-light: #f8fafc;
  --card-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

.resume-preview-page {
  padding: 24px;
  min-height: calc(100vh - 70px);
  background-color: var(--bg-light);
  background-image: linear-gradient(to bottom right, #f9fafc, #f1f5f9);
}

.page-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
  max-width: 1280px;
  margin: 0 auto;
}

.resume-card, .chat-card {
  height: 100%;
  display: flex;
  flex-direction: column;
  box-shadow: var(--card-shadow);
  border-radius: 12px;
  overflow: hidden;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.resume-card:hover, .chat-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
}

/* 卡片头部样式 */
.card-header {
  display: flex;
  align-items: center;
  padding: 4px 0;
}

.card-title {
  display: flex;
  align-items: center;
  font-weight: 600;
  color: var(--text-primary);
  font-size: 16px;
}

.header-icon {
  margin-right: 8px;
  color: var(--primary-color);
}

.action-group {
  display: flex;
  gap: 4px;
}

.action-btn {
  display: flex;
  align-items: center;
  transition: all 0.2s ease;
}

.action-btn:hover {
  background-color: var(--primary-light);
  color: var(--primary-color);
}

.model-selector-wrapper {
  display: flex;
  align-items: center;
}

.resume-container {
  margin-top: 15px;
  overflow: auto;
  flex: 1;
}

.empty-state {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 350px;
  background-image: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  border-radius: 8px;
}

.empty-content {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.empty-icon {
  color: var(--primary-color);
  opacity: 0.6;
  margin-bottom: 12px;
}

.generate-btn {
  padding: 8px 16px;
  background-color: var(--primary-color);
  transition: all 0.2s ease;
}

.generate-btn:hover {
  background-color: #246acf;
  box-shadow: 0 4px 8px rgba(45, 108, 223, 0.2);
}

.edit-mode {
  height: 100%;
}

.resume-editor {
  border-radius: 8px;
  font-family: 'Inter', 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

.preview-mode {
  padding: 25px;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  background-color: white;
  min-height: 500px;
  max-height: 700px;
  overflow-y: auto;
  box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.05);
}

.resume-content {
  font-family: 'Inter', 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  color: var(--text-primary);
}

:deep(.resume-content h1) {
  font-size: 1.6rem;
  margin-bottom: 1rem;
  border-bottom: 2px solid #e2e8f0;
  padding-bottom: 0.6rem;
  color: var(--primary-color);
  font-weight: 600;
}

:deep(.resume-content h2) {
  font-size: 1.25rem;
  margin-top: 1.4rem;
  margin-bottom: 0.6rem;
  color: var(--secondary-color);
  font-weight: 600;
  border-left: 3px solid var(--accent-color);
  padding-left: 10px;
}

:deep(.resume-content ul) {
  padding-left: 1.5rem;
  margin-bottom: 1rem;
}

:deep(.resume-content li) {
  margin-bottom: 0.4rem;
}

:deep(.resume-content p) {
  margin-bottom: 0.8rem;
  line-height: 1.6;
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
  padding: 15px;
  min-height: 400px;
  max-height: 500px;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  background-color: #f8fafc;
  margin-bottom: 15px;
  box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.03);
  scrollbar-width: thin;
  scrollbar-color: #cbd5e0 #f1f5f9;
}

.messages::-webkit-scrollbar {
  width: 6px;
}

.messages::-webkit-scrollbar-track {
  background: #f1f5f9;
}

.messages::-webkit-scrollbar-thumb {
  background-color: #cbd5e0;
  border-radius: 6px;
}

.message {
  margin-bottom: 18px;
  padding: 12px 16px;
  border-radius: 12px;
  max-width: 85%;
  position: relative;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.message.user {
  background-color: var(--primary-light);
  align-self: flex-end;
  margin-left: auto;
  border-bottom-right-radius: 4px;
  color: var(--text-primary);
}

.message.assistant {
  background-color: white;
  align-self: flex-start;
  border: 1px solid #e2e8f0;
  border-bottom-left-radius: 4px;
}

.message.system {
  background-color: #f7f9fc;
  border: 1px dashed #cbd5e0;
  margin-left: auto;
  margin-right: auto;
  max-width: 95%;
  margin-bottom: 25px;
  border-radius: 14px;
}

.message.loading {
  background-color: transparent;
  border: none;
  box-shadow: none;
}

.message-content {
  word-break: break-word;
  line-height: 1.6;
}

:deep(.message-content a) {
  color: var(--primary-color);
  text-decoration: none;
  border-bottom: 1px dashed var(--primary-color);
  transition: border-bottom 0.2s ease, color 0.2s ease;
}

:deep(.message-content a:hover) {
  border-bottom: 1px solid var(--primary-color);
  color: #1a56db;
}

:deep(.message-content code) {
  background-color: #f1f5f9;
  padding: 2px 6px;
  border-radius: 4px;
  font-family: 'Fira Code', 'Menlo', 'Monaco', 'Courier New', monospace;
  font-size: 0.9em;
  color: #1e293b;
}

:deep(.message-content pre) {
  background-color: #1e293b;
  color: #e2e8f0;
  padding: 12px;
  border-radius: 6px;
  overflow-x: auto;
  margin: 12px 0;
}

:deep(.message-content pre code) {
  background-color: transparent;
  color: inherit;
  padding: 0;
  border-radius: 0;
  font-size: 0.95em;
}

.loading-text {
  margin-left: 10px;
  color: #64748b;
  font-weight: 500;
}

.loading-dots {
  display: inline-block;
}

.loading-dots span {
  animation: dots 1.4s infinite;
  animation-fill-mode: both;
  margin-right: 2px;
  color: var(--primary-color);
  font-weight: bold;
}

.loading-dots span:nth-child(2) {
  animation-delay: 0.2s;
}

.loading-dots span:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes dots {
  0% { opacity: 0.2; }
  20% { opacity: 1; }
  100% { opacity: 0.2; }
}

.input-area {
  margin-top: auto;
  background-color: white;
  border-radius: 10px;
  padding: 10px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
}

.chat-input {
  border-radius: 8px;
  font-family: 'Inter', 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

.action-buttons {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 10px;
}

.clear-btn {
  border: 1px solid #e2e8f0;
  transition: all 0.2s ease;
}

.clear-btn:hover {
  background-color: #f1f5f9;
}

.send-btn {
  background-color: var(--primary-color);
  transition: all 0.2s ease;
}

.send-btn:hover {
  background-color: #246acf;
  box-shadow: 0 2px 5px rgba(45, 108, 223, 0.2);
}

/* 响应式布局 */
@media (max-width: 900px) {
  .page-container {
    grid-template-columns: 1fr;
  }
  
  .resume-card, .chat-card {
    margin-bottom: 20px;
  }
  
  .preview-mode, .messages {
    max-height: 500px;
  }
}

@media (max-width: 600px) {
  .resume-preview-page {
    padding: 12px;
  }
  
  .message {
    max-width: 95%;
  }
}
</style> 