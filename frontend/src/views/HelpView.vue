<template>
  <div class="help-view">
    <div class="container">
      <n-space vertical size="large">
        <div class="page-header">
          <h1 class="page-title">帮助中心</h1>
          <p class="page-description">了解如何使用ResuGenie构建和优化您的简历</p>
        </div>
        
        <n-card>
          <n-tabs v-model:value="activeTab" type="line" animated>
            <n-tab-pane name="guide" tab="使用指南">
              <n-space vertical size="large" class="guide-content">
                <div class="guide-section">
                  <h2>新用户指南</h2>
                  <p>欢迎使用 ResuGenie！本指南将帮助您快速了解如何使用我们的平台来创建和优化您的简历。</p>
                  
                  <n-divider />
                  
                  <h3>创建简历</h3>
                  <p>ResuGenie 提供两种方式来获取您的专业简历：</p>
                  
                  <h4>方法一：从头创建</h4>
                  <n-ol>
                    <n-list-item>点击顶部导航栏的<strong>创建简历</strong></n-list-item>
                    <n-list-item>在表单中填写您的个人信息、教育背景、工作经历等</n-list-item>
                    <n-list-item>选择一个适合您行业的简历模板</n-list-item>
                    <n-list-item>点击<strong>生成简历</strong></n-list-item>
                    <n-list-item>预览和下载您的专业简历PDF文件</n-list-item>
                  </n-ol>
                  
                  <h4>方法二：优化现有简历</h4>
                  <n-ol>
                    <n-list-item>点击顶部导航栏的<strong>优化简历</strong></n-list-item>
                    <n-list-item>上传您现有的简历文件（支持PDF和Word格式）</n-list-item>
                    <n-list-item>等待AI分析完成</n-list-item>
                    <n-list-item>查看并应用优化建议</n-list-item>
                    <n-list-item>导出优化后的简历</n-list-item>
                  </n-ol>
                </div>
                
                <div class="guide-section">
                  <h3>关于简历模板</h3>
                  <p>ResuGenie 提供多种专业设计的简历模板，包括：</p>
                  <n-ul>
                    <n-list-item><strong>现代简约风格</strong> - 适合大多数行业的清晰简洁设计</n-list-item>
                    <n-list-item><strong>专业商务风格</strong> - 适合金融、法律、咨询等传统行业</n-list-item>
                    <n-list-item><strong>创意设计风格</strong> - 适合设计、市场营销、媒体等创意行业</n-list-item>
                    <n-list-item><strong>技术简约风格</strong> - 专为IT、软件工程等技术岗位设计</n-list-item>
                  </n-ul>
                  <p>每个模板都经过精心设计，符合ATS（申请跟踪系统）友好标准，提高您的简历被筛选通过的概率。</p>
                </div>
                
                <div class="guide-section">
                  <h3>如何写出引人注目的简历</h3>
                  <n-collapse>
                    <n-collapse-item title="1. 个人概述怎么写？" name="summary">
                      <p>个人概述是简历的"开场白"，应该简洁有力地概括您的专业背景和核心优势。建议：</p>
                      <n-ul>
                        <n-list-item>控制在3-5句话以内</n-list-item>
                        <n-list-item>突出您的专业身份和年资</n-list-item>
                        <n-list-item>强调与目标职位相关的技能和成就</n-list-item>
                        <n-list-item>可以提及您的职业目标</n-list-item>
                      </n-ul>
                    </n-collapse-item>
                    
                    <n-collapse-item title="2. 工作经历如何描述更有说服力？" name="work">
                      <p>描述工作经历时，应该强调成果而非职责。建议：</p>
                      <n-ul>
                        <n-list-item>使用行动导向的动词开头（如"领导"、"开发"、"实施"）</n-list-item>
                        <n-list-item>尽可能量化您的成就（数字、百分比、金额等）</n-list-item>
                        <n-list-item>突出您解决的问题和带来的价值</n-list-item>
                        <n-list-item>使用行业关键词，提高ATS匹配度</n-list-item>
                      </n-ul>
                    </n-collapse-item>
                    
                    <n-collapse-item title="3. 技能部分该如何安排？" name="skills">
                      <p>技能部分应当针对目标职位进行调整。建议：</p>
                      <n-ul>
                        <n-list-item>将最相关的硬技能放在前面</n-list-item>
                        <n-list-item>为技能分类（如技术技能、语言技能、软技能等）</n-list-item>
                        <n-list-item>只列出与目标职位相关的技能</n-list-item>
                        <n-list-item>可以标注技能熟练度，但请诚实评估</n-list-item>
                      </n-ul>
                    </n-collapse-item>
                  </n-collapse>
                </div>
              </n-space>
            </n-tab-pane>
            
            <n-tab-pane name="faq" tab="常见问题">
              <div class="faq-content">
                <n-collapse>
                  <n-collapse-item title="ResuGenie是免费使用的吗？" name="pricing">
                    <p>目前ResuGenie处于公测阶段，所有基础功能均可免费使用。未来我们将推出高级功能，可能会采用订阅制模式，基础功能将保持免费。</p>
                  </n-collapse-item>
                  
                  <n-collapse-item title="我的简历数据安全吗？" name="security">
                    <p>ResuGenie高度重视用户隐私和数据安全。我们：</p>
                    <n-ul>
                      <n-list-item>不会永久存储您的简历内容</n-list-item>
                      <n-list-item>使用加密技术保护数据传输</n-list-item>
                      <n-list-item>不会将您的个人信息分享给第三方</n-list-item>
                    </n-ul>
                    <p>您可以随时删除您的账户数据。更多详情请查看我们的隐私政策。</p>
                  </n-collapse-item>
                  
                  <n-collapse-item title="如何导出我的简历？" name="export">
                    <p>在完成简历创建或优化后，您可以：</p>
                    <n-ol>
                      <n-list-item>在预览页面点击"导出PDF"按钮</n-list-item>
                      <n-list-item>文件将自动下载到您的设备上</n-list-item>
                    </n-ol>
                    <p>目前我们支持PDF格式导出，未来将支持更多格式。</p>
                  </n-collapse-item>
                  
                  <n-collapse-item title="AI优化建议的可靠性如何？" name="ai">
                    <p>ResuGenie的AI建议基于大量专业简历样本和招聘最佳实践。虽然AI可以提供有价值的建议，但它并不能完全替代人工判断。我们建议：</p>
                    <n-ul>
                      <n-list-item>批判性地评估每个建议</n-list-item>
                      <n-list-item>考虑您的具体情况和目标职位需求</n-list-item>
                      <n-list-item>保持简历内容的真实性</n-list-item>
                    </n-ul>
                  </n-collapse-item>
                  
                  <n-collapse-item title="上传简历后无法识别内容怎么办？" name="parsing">
                    <p>如果系统无法正确提取您的简历内容，可能是因为：</p>
                    <n-ul>
                      <n-list-item>文件格式不受支持（目前支持PDF和DOC/DOCX）</n-list-item>
                      <n-list-item>简历使用了复杂的排版或表格</n-list-item>
                      <n-list-item>文件可能已损坏</n-list-item>
                    </n-ul>
                    <p>建议尝试：</p>
                    <n-ul>
                      <n-list-item>将文件转换为纯文本格式后重试</n-list-item>
                      <n-list-item>使用"从头创建"功能手动输入内容</n-list-item>
                      <n-list-item>联系我们的支持团队获取帮助</n-list-item>
                    </n-ul>
                  </n-collapse-item>
                </n-collapse>
              </div>
            </n-tab-pane>
            
            <n-tab-pane name="contact" tab="联系我们">
              <div class="contact-content">
                <p>如果您有任何问题、建议或意见，欢迎随时与我们联系。我们的支持团队将竭诚为您服务。</p>
                
                <div class="contact-methods">
                  <n-card title="电子邮件" class="contact-card">
                    <template #icon>
                      <n-icon><mail-icon /></n-icon>
                    </template>
                    <a href="mailto:support@resugenie.com">support@resugenie.com</a>
                  </n-card>
                  
                  <n-card title="社交媒体" class="contact-card">
                    <template #icon>
                      <n-icon><logo-github-icon /></n-icon>
                    </template>
                    <p>GitHub: @ResuGenie</p>
                    <p>Twitter: @ResuGenie_AI</p>
                  </n-card>
                </div>
                
                <div class="feedback-form">
                  <h3>意见反馈</h3>
                  <p>我们非常重视用户的反馈，它将帮助我们不断改进产品。</p>
                  
                  <n-alert title="功能开发中" type="info">
                    <template #icon>
                      <n-icon><construct-icon /></n-icon>
                    </template>
                    <p>反馈表单功能正在开发中，即将推出。您可以通过上方邮箱联系我们。</p>
                  </n-alert>
                </div>
              </div>
            </n-tab-pane>
          </n-tabs>
        </n-card>
      </n-space>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { 
  NSpace, 
  NCard, 
  NTabs, 
  NTabPane, 
  NCollapse, 
  NCollapseItem,
  NDivider,
  NAlert,
  NIcon,
  NOl,
  NUl,
  NListItem
} from 'naive-ui'
import { 
  Mail as MailIcon, 
  LogoGithub as LogoGithubIcon,
  Construct as ConstructIcon
} from '@vicons/ionicons5'

const route = useRoute()
const activeTab = ref('guide')

// 处理URL查询参数，设置活动标签
onMounted(() => {
  if (route.query.tab) {
    // 检查tab参数是否有效
    const validTabs = ['guide', 'faq', 'contact']
    if (validTabs.includes(route.query.tab)) {
      activeTab.value = route.query.tab
    }
  }
})
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

.guide-content {
  padding: 1rem 0;
}

.guide-section {
  margin-bottom: 2rem;
}

.guide-section h2 {
  font-size: 1.75rem;
  color: var(--text-primary);
  margin-bottom: 1rem;
}

.guide-section h3 {
  font-size: 1.5rem;
  color: var(--text-primary);
  margin-bottom: 1rem;
  margin-top: 1.5rem;
}

.guide-section h4 {
  font-size: 1.25rem;
  color: var(--text-primary);
  margin-bottom: 0.5rem;
  margin-top: 1rem;
}

.guide-section p {
  margin-bottom: 1rem;
  line-height: 1.6;
}

.faq-content {
  padding: 1rem 0;
}

.contact-content {
  padding: 2rem 0;
}

.contact-methods {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.contact-card {
  height: 100%;
}

.feedback-form {
  margin-top: 3rem;
}

.feedback-form h3 {
  font-size: 1.5rem;
  color: var(--text-primary);
  margin-bottom: 1rem;
}
</style> 