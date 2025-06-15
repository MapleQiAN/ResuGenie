<template>
  <div class="model-selector">
    <n-select
      v-model:value="currentModel"
      :options="modelOptions"
      placeholder="请选择语言模型"
      :disabled="loading"
      @update:value="handleModelChange"
    />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useMessage } from 'naive-ui'
import { useLlmStore } from '../../store/llm'

// 组件属性
const props = defineProps({
  disabled: {
    type: Boolean,
    default: false
  }
})

// 组件事件
const emit = defineEmits(['change'])

const message = useMessage()
const llmStore = useLlmStore()

// 当前选中的模型
const currentModel = computed({
  get: () => llmStore.selectedModel,
  set: (value) => {
    llmStore.setModel(value)
  }
})

// 模型选项列表
const modelOptions = computed(() => {
  return llmStore.models.map(model => {
    // 确定模型类别图标 - 可以根据模型名称添加不同图标
    let providerTag = '默认'
    if (model.includes('gpt')) {
      providerTag = 'OpenAI'
    } else if (model.includes('deepseek')) {
      providerTag = 'DeepSeek'
    } else if (['llama2', 'mistral', 'gemma'].some(name => model.includes(name))) {
      providerTag = 'Ollama'
    }
    
    return {
      label: `${model} (${providerTag})`,
      value: model
    }
  })
})

// 加载状态
const loading = computed(() => llmStore.loading || props.disabled)

// 模型变更处理函数
const handleModelChange = (value) => {
  emit('change', value)
}

// 组件挂载时获取模型列表
onMounted(async () => {
  try {
    await llmStore.fetchModels()
    if (llmStore.models.length === 0) {
      message.warning('没有可用的模型')
    }
  } catch (error) {
    message.error(`获取模型列表失败: ${error.message || '未知错误'}`)
  }
})
</script>

<style scoped>
.model-selector {
  width: 100%;
  margin-bottom: 16px;
}
</style> 