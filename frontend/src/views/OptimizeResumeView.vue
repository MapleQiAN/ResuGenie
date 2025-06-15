<template>
  <div class="optimize-resume-view">
    <div class="container">
      <n-space vertical size="large">
        <div class="page-header">
          <h1 class="page-title">优化您的简历</h1>
          <p class="page-description">上传您现有的简历，AI将为您提供专业的优化建议</p>
        </div>
        
        <n-card>
          <n-tabs type="line" animated>
            <n-tab-pane name="upload" tab="上传简历">
              <div class="upload-section">
                <n-upload
                  ref="uploadRef"
                  accept=".pdf,.doc,.docx"
                  :max="1"
                  :disabled="resumeStore.fileUpload.loading"
                  @change="handleUploadChange"
                >
                  <n-upload-dragger>
                    <div class="upload-content">
                      <n-icon size="48" :depth="3">
                        <cloud-upload-icon />
                      </n-icon>
                      <h3>点击或拖拽文件到此区域上传</h3>
                      <p>支持 PDF、Word 文档格式</p>
                    </div>
                  </n-upload-dragger>
                </n-upload>
                
                <div class="upload-tips">
                  <n-alert title="提示" type="info">
                    <template #icon>
                      <n-icon><information-icon /></n-icon>
                    </template>
                    <p>上传您的简历后，我们的AI将分析内容并提供针对性的优化建议，帮助您提升简历质量。</p>
                    <p>您的个人信息将被严格保密。</p>
                  </n-alert>
                </div>
              </div>
            </n-tab-pane>
            
            <n-tab-pane name="suggestions" tab="优化建议" :disabled="!resumeStore.resumePreview">
              <n-space vertical>
                <n-spin :show="resumeStore.optimizing">
                  <n-card title="AI优化建议">
                    <template #header-extra>
                      <n-button @click="handleRefreshSuggestions" size="small" :loading="resumeStore.optimizing">
                        <template #icon>
                          <n-icon><refresh-icon /></n-icon>
                        </template>
                        刷新建议
                      </n-button>
                    </template>
                    
                    <n-collapse>
                      <n-collapse-item
                        v-for="(suggestion, index) in resumeStore.optimizationSuggestions"
                        :key="index"
                        :title="suggestion.title"
                        :name="index"
                      >
                        <div class="suggestion-content">
                          <p>{{ suggestion.description }}</p>
                          <div v-if="suggestion.before && suggestion.after" class="suggestion-comparison">
                            <div class="suggestion-before">
                              <div class="suggestion-label">当前内容</div>
                              <div class="suggestion-text">{{ suggestion.before }}</div>
                            </div>
                            <div class="suggestion-arrow">
                              <n-icon><arrow-forward-icon /></n-icon>
                            </div>
                            <div class="suggestion-after">
                              <div class="suggestion-label">建议内容</div>
                              <div class="suggestion-text">{{ suggestion.after }}</div>
                            </div>
                          </div>
                          
                          <div class="suggestion-actions">
                            <n-button
                              type="primary"
                              size="small"
                              :disabled="suggestion.applied"
                              @click="handleApplySuggestion(suggestion.id, index)"
                            >
                              {{ suggestion.applied ? '已应用' : '应用此建议' }}
                            </n-button>
                          </div>
                        </div>
                      </n-collapse-item>
                    </n-collapse>
                    
                    <n-empty
                      v-if="resumeStore.optimizationSuggestions.length === 0 && !resumeStore.optimizing"
                      description="暂无优化建议，请先上传简历"
                    />
                  </n-card>
                </n-spin>
              </n-space>
            </n-tab-pane>
            
            <n-tab-pane name="chat" tab="AI改写助手" :disabled="!resumeStore.resumePreview">
              <div class="chat-section">
                <div class="chat-placeholder">
                  <n-empty description="AI改写助手功能即将推出，敬请期待！">
                    <template #icon>
                      <n-icon size="48" color="var(--primary-color)">
                        <chatbox-icon />
                      </n-icon>
                    </template>
                    <template #extra>
                      <p>您可以先使用上方的优化建议功能</p>
                    </template>
                  </n-empty>
                </div>
              </div>
            </n-tab-pane>
          </n-tabs>
        </n-card>
        
        <n-card v-if="resumeStore.resumePreview" title="简历预览">
          <div class="preview-section">
            <div class="preview-actions">
              <n-space>
                <n-button @click="handleExportPDF" :loading="exporting">
                  <template #icon>
                    <n-icon><download-icon /></n-icon>
                  </template>
                  导出PDF
                </n-button>
              </n-space>
            </div>
            
            <div class="resume-preview-content">
              <div v-html="resumeStore.resumePreview" class="resume-html-preview"></div>
            </div>
          </div>
        </n-card>
      </n-space>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useMessage } from 'naive-ui'
import { useResumeStore } from '@/store/resume'
import {
  NButton,
  NUpload,
  NSpace,
  NGrid,
  NGi,
  NCard,
  NTabs,
  NTabPane,
  NSpin,
  NCollapse,
  NCollapseItem,
  NEmpty
} from 'naive-ui'
import {
  CloudUpload as CloudUploadIcon,
  Refresh as RefreshIcon,
  ArrowForward as ArrowForwardIcon,
  Download as DownloadIcon,
  InformationCircle as InformationIcon,
  ChatbubbleEllipses as ChatboxIcon
} from '@vicons/ionicons5'

const resumeStore = useResumeStore()
const message = useMessage()
const router = useRouter()
const uploadRef = ref(null)
const exporting = ref(false)

// 处理文件上传变化
const handleUploadChange = ({ file, fileList }) => {
  if (file.status === 'finished') {
    handleFileUpload(file.file)
  } else if (file.status === 'error') {
    message.error('文件上传失败')
  }
}

// 处理文件上传
const handleFileUpload = async (file) => {
  try {
    await resumeStore.uploadResumeFile(file)
    message.success('简历上传成功')
    
    // 自动获取优化建议
    handleRefreshSuggestions()
  } catch (error) {
    message.error('上传失败：' + (error.message || '未知错误'))
  }
}

// 刷新优化建议
const handleRefreshSuggestions = async () => {
  try {
    await resumeStore.getOptimizationSuggestions()
  } catch (error) {
    message.error('获取优化建议失败：' + (error.message || '未知错误'))
  }
}

// 应用优化建议
const handleApplySuggestion = async (suggestionId, index) => {
  try {
    await resumeStore.applyOptimizationSuggestion(suggestionId)
    message.success('已应用该优化建议')
  } catch (error) {
    message.error('应用建议失败：' + (error.message || '未知错误'))
  }
}

// 导出PDF
const handleExportPDF = async () => {
  exporting.value = true
  try {
    const response = await resumeStore.exportResumePDF()
    
    // 处理文件下载
    const url = window.URL.createObjectURL(new Blob([response.data]))
    const link = document.createElement('a')
    link.href = url
    link.setAttribute('download', '优化后的简历.pdf')
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
    
    message.success('简历已导出')
  } catch (error) {
    message.error('导出失败：' + (error.message || '未知错误'))
  } finally {
    exporting.value = false
  }
}
</script>

<style scoped>
.page-header {
  text-align: center;
  margin-bottom: 2rem;
}

.page-title {
  font-size: 2rem;
  color: var(--text-primary);
  margin-bottom: 0.5rem;
}

.page-description {
  font-size: 1.1rem;
  color: var(--text-secondary);
}

.upload-section {
  padding: 1rem 0;
}

.upload-content {
  padding: 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.upload-content h3 {
  margin: 1rem 0 0.5rem;
  font-size: 1.2rem;
  color: var(--text-primary);
}

.upload-content p {
  margin: 0;
  color: var(--text-secondary);
}

.upload-tips {
  margin-top: 1rem;
}

.suggestion-content {
  padding: 0.5rem 0;
}

.suggestion-comparison {
  display: flex;
  gap: 1rem;
  align-items: center;
  margin: 1rem 0;
}

.suggestion-before, .suggestion-after {
  flex: 1;
  padding: 1rem;
  border-radius: 6px;
}

.suggestion-before {
  background-color: rgba(239, 68, 68, 0.1);
}

.suggestion-after {
  background-color: rgba(16, 185, 129, 0.1);
}

.suggestion-label {
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.suggestion-arrow {
  display: flex;
  align-items: center;
  color: var(--text-secondary);
}

.suggestion-actions {
  margin-top: 1rem;
  display: flex;
  justify-content: flex-end;
}

.preview-section {
  padding: 1rem 0;
}

.preview-actions {
  margin-bottom: 1rem;
  display: flex;
  justify-content: flex-end;
}

.resume-preview-content {
  border: 1px solid var(--border-color);
  border-radius: 6px;
  padding: 1rem;
  min-height: 400px;
  max-height: 600px;
  overflow-y: auto;
  background-color: white;
}

.chat-section {
  padding: 2rem 0;
}

.chat-placeholder {
  display: flex;
  justify-content: center;
  padding: 3rem 0;
}

/* 响应式调整 */
@media (max-width: 768px) {
  .suggestion-comparison {
    flex-direction: column;
  }
  
  .suggestion-arrow {
    transform: rotate(90deg);
    margin: 1rem 0;
  }
}
</style> 