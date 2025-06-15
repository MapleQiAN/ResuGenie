<template>
  <div class="chat-interface">
    <!-- 对话区域 -->
    <div class="messages-container" ref="messagesContainer">
      <template v-if="messages.length === 0">
        <div class="empty-chat">
          <n-empty description="开始聊天">
            <template #extra>
              <p>选择一个模型，开始与AI助手对话</p>
            </template>
          </n-empty>
        </div>
      </template>
      
      <template v-else>
        <div v-for="(msg, index) in messages" :key="index" class="message-wrapper" :class="{'user-message': msg.role === 'user'}">
          <div class="message-bubble" :class="msg.role">
            <div class="message-header">
              <span class="role-label">{{ msg.role === 'user' ? '用户' : 'AI 助手' }}</span>
            </div>
            <div class="message-content">{{ msg.content }}</div>
          </div>
        </div>
      </template>
      
      <div v-if="isLoading" class="loading-indicator">
        <n-spin size="small" />
        <span>AI思考中...</span>
      </div>
    </div>
    
    <!-- 输入区域 -->
    <div class="input-area">
      <n-input
        v-model:value="userInput"
        type="textarea"
        placeholder="请输入您的问题..."
        :disabled="isLoading || !selectedModel"
        :autosize="{ minRows: 1, maxRows: 4 }"
        @keydown.enter.ctrl.prevent="handleSendMessage"
      />
      
      <div class="action-buttons">
        <n-button
          type="primary"
          :disabled="!userInput.trim() || isLoading || !selectedModel"
          @click="handleSendMessage"
        >
          发送
        </n-button>
        
        <n-button
          :disabled="isLoading || messages.length === 0"
          @click="clearChat"
        >
          清空对话
        </n-button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, nextTick } from 'vue'
import { useMessage } from 'naive-ui'
import { useLlmStore } from '../../store/llm'

const props = defineProps({
  modelValue: {
    type: String,
    default: ''
  }
})

const emit = defineEmits(['update:modelValue', 'send'])

const message = useMessage()
const llmStore = useLlmStore()
const messagesContainer = ref(null)
const userInput = ref(props.modelValue)

// 监听输入值变化
watch(() => props.modelValue, (newVal) => {
  userInput.value = newVal
})

// 发送消息后更新输入框
watch(() => userInput.value, (newVal) => {
  emit('update:modelValue', newVal)
})

// 当前选中的模型
const selectedModel = computed(() => llmStore.selectedModel)

// 消息列表
const messages = computed(() => llmStore.messages)

// 加载状态
const isLoading = computed(() => llmStore.loading)

// 发送消息
const handleSendMessage = async () => {
  if (!userInput.value.trim() || !selectedModel.value) return
  
  try {
    const content = userInput.value
    userInput.value = ''  // 清空输入框
    
    await llmStore.sendMessage(content)
    
    // 自动滚动到底部
    await nextTick()
    if (messagesContainer.value) {
      messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
    }
  } catch (error) {
    message.error(`发送消息失败: ${error.message || '未知错误'}`)
  }
}

// 清空对话
const clearChat = () => {
  llmStore.clearMessages()
}

// 监听消息变化，自动滚动到底部
watch(() => messages.value.length, async () => {
  await nextTick()
  if (messagesContainer.value) {
    messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
  }
})
</script>

<style scoped>
.chat-interface {
  display: flex;
  flex-direction: column;
  height: 100%;
  border: 1px solid #eee;
  border-radius: 8px;
  overflow: hidden;
}

.messages-container {
  flex: 1;
  overflow-y: auto;
  padding: 16px;
  background-color: #f9f9f9;
}

.empty-chat {
  display: flex;
  height: 100%;
  align-items: center;
  justify-content: center;
}

.message-wrapper {
  margin-bottom: 16px;
  display: flex;
}

.user-message {
  justify-content: flex-end;
}

.message-bubble {
  max-width: 80%;
  padding: 12px 16px;
  border-radius: 8px;
  background-color: #fff;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.message-bubble.user {
  background-color: #ecf5ff;
}

.message-bubble.assistant {
  background-color: #ffffff;
}

.message-header {
  margin-bottom: 4px;
  font-weight: bold;
  color: #666;
  font-size: 0.85em;
}

.message-content {
  white-space: pre-wrap;
  word-break: break-word;
}

.loading-indicator {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #999;
  margin: 8px 0;
}

.input-area {
  padding: 16px;
  background-color: #fff;
  border-top: 1px solid #eee;
}

.action-buttons {
  display: flex;
  justify-content: flex-end;
  gap: 8px;
  margin-top: 8px;
}
</style> 