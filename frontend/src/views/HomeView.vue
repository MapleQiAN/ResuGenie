<template>
  <div class="home-view">
    <!-- 英雄区 -->
    <section class="hero">
      <div class="container">
        <div class="hero-content">
          <div class="hero-text">
            <h1 class="hero-title animate-fade-in">
              <n-gradient-text type="success" size="48">
                简历撰写，<span class="text-highlight">由 AI 驱动</span>
              </n-gradient-text>
            </h1>
            <p class="hero-subtitle animate-fade-in-delay-1">
              ResuGenie 是一个基于 AI 的简历生成与优化平台<br>
              帮助你高效构建、分析和完善简历，让求职之路更加顺畅
            </p>
            <div class="hero-actions animate-fade-in-delay-2">
              <n-button type="primary" size="large" class="btn-animated" round @click="handleCreateResume">
                <n-icon class="icon-margin-right"><rocket-icon /></n-icon>
                开始创建简历
              </n-button>
              <n-button size="large" class="btn-animated" round @click="handleOptimizeResume">
                <n-icon class="icon-margin-right"><sparkles-icon /></n-icon>
                优化现有简历
              </n-button>
            </div>
          </div>
          <div class="hero-image animate-float">
            <img src="@/assets/images/hero-image.svg" alt="ResuGenie - AI简历助手" />
          </div>
        </div>
      </div>
      <!-- 装饰元素 -->
      <div class="shape-divider">
        <svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
          <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z" class="shape-fill"></path>
        </svg>
      </div>
    </section>

    <!-- 功能特点 -->
    <section class="features">
      <div class="container">
        <n-space vertical size="large">
          <div class="section-header text-center animate-fade-in">
            <div class="badge-wrapper">
              <span class="section-badge">核心功能</span>
            </div>
            <h2 class="section-title">简历制作从未如此简单</h2>
            <p class="section-description">ResuGenie 提供全方位的简历创建与优化功能</p>
          </div>

          <n-grid cols="1 s:2 m:4" x-gap="20" y-gap="20" responsive="screen">
            <n-gi>
              <div class="feature-card card-hover animate-fade-in-delay-1">
                <div class="feature-icon pulse">
                  <n-icon size="36" color="var(--primary-color)">
                    <file-text-icon />
                  </n-icon>
                </div>
                <h3 class="feature-title">智能生成简历</h3>
                <p class="feature-description">填写基本信息，AI 自动生成专业简历内容</p>
              </div>
            </n-gi>
            
            <n-gi>
              <div class="feature-card card-hover animate-fade-in-delay-2">
                <div class="feature-icon pulse">
                  <n-icon size="36" color="var(--secondary-color)">
                    <bulb-icon />
                  </n-icon>
                </div>
                <h3 class="feature-title">简历优化建议</h3>
                <p class="feature-description">AI 分析简历内容，提供专业改进建议</p>
              </div>
            </n-gi>
            
            <n-gi>
              <div class="feature-card card-hover animate-fade-in-delay-3">
                <div class="feature-icon pulse">
                  <n-icon size="36" color="var(--accent-color)">
                    <chat-bubble-icon />
                  </n-icon>
                </div>
                <h3 class="feature-title">智能改写助手</h3>
                <p class="feature-description">通过对话方式，针对性修改简历内容</p>
              </div>
            </n-gi>
            
            <n-gi>
              <div class="feature-card card-hover animate-fade-in-delay-4">
                <div class="feature-icon pulse">
                  <n-icon size="36" color="var(--info-color)">
                    <document-icon />
                  </n-icon>
                </div>
                <h3 class="feature-title">专业简历模板</h3>
                <p class="feature-description">多种精美模板，导出高质量 PDF 简历</p>
              </div>
            </n-gi>
          </n-grid>
        </n-space>
      </div>
    </section>

    <!-- 使用步骤 -->
    <section class="how-it-works">
      <div class="container">
        <n-space vertical size="large">
          <div class="section-header text-center animate-fade-in">
            <div class="badge-wrapper">
              <span class="section-badge">简单易用</span>
            </div>
            <h2 class="section-title">三步创建完美简历</h2>
            <p class="section-description">简单快速，省时省力</p>
          </div>

          <div class="steps-container animate-fade-in-delay-1">
            <n-steps vertical size="large">
              <n-step title="填写个人信息" description="输入您的基本信息、教育背景、工作经历等">
                <template #icon>
                  <n-icon class="step-icon"><edit-icon /></n-icon>
                </template>
              </n-step>
              <n-step title="选择简历模板" description="从多种专业设计的模板中选择您喜欢的风格">
                <template #icon>
                  <n-icon class="step-icon"><template-icon /></n-icon>
                </template>
              </n-step>
              <n-step title="生成并优化" description="AI 生成简历内容，提供优化建议并导出 PDF">
                <template #icon>
                  <n-icon class="step-icon"><download-icon /></n-icon>
                </template>
              </n-step>
            </n-steps>
          </div>
        </n-space>
      </div>
    </section>

    <!-- 号召性用语 -->
    <section class="cta">
      <div class="container">
        <div class="cta-content animate-fade-in">
          <h2 class="cta-title">现在就开始创建您的专业简历</h2>
          <p class="cta-description">加入数千名求职者，使用 ResuGenie 获得面试机会</p>
          <div class="cta-actions">
            <n-button type="primary" size="large" class="btn-animated" round @click="handleCreateResume">
              <n-icon class="icon-margin-right"><rocket-icon /></n-icon>
              免费开始使用
            </n-button>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { 
  NButton,
  NGrid,
  NGi,
  NSpace,
  NCard,
  NText,
  NIcon,
  NSteps,
  NStep,
  NGradientText
} from 'naive-ui'
import { 
  DocumentText as FileTextIcon,
  Bulb as BulbIcon,
  ChatbubbleEllipses as ChatBubbleIcon,
  Document as DocumentIcon,
  Create as EditIcon,
  GridOutline as TemplateIcon,
  Download as DownloadIcon,
  Rocket as RocketIcon,
  Sparkles as SparklesIcon
} from '@vicons/ionicons5'

const router = useRouter()

// 处理创建简历按钮点击
const handleCreateResume = () => {
  router.push('/create')
}

// 处理优化简历按钮点击
const handleOptimizeResume = () => {
  router.push('/optimize')
}
</script>

<style scoped>
/* 英雄区样式 */
.hero {
  padding: 6rem 0 8rem;
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(20, 184, 166, 0.1) 100%);
  position: relative;
  overflow: hidden;
}

.hero-content {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.hero-text {
  flex: 1;
}

.hero-title {
  font-size: 3rem;
  font-weight: 800;
  margin-bottom: 1.5rem;
  line-height: 1.1;
}

.text-highlight {
  position: relative;
  display: inline-block;
}

.text-highlight::after {
  content: "";
  position: absolute;
  bottom: 8px;
  left: 0;
  width: 100%;
  height: 8px;
  background-color: rgba(79, 70, 229, 0.3);
  border-radius: 4px;
  z-index: -1;
}

.hero-subtitle {
  font-size: 1.25rem;
  color: var(--text-secondary);
  margin-bottom: 2rem;
  line-height: 1.6;
}

.hero-actions {
  display: flex;
  gap: 1rem;
}

.icon-margin-right {
  margin-right: 8px;
}

.hero-image {
  flex: 1;
  display: flex;
  justify-content: flex-end;
}

.hero-image img {
  max-width: 100%;
  height: auto;
  filter: drop-shadow(0 10px 15px rgba(0, 0, 0, 0.1));
}

/* 装饰形状分隔符 */
.shape-divider {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  overflow: hidden;
  line-height: 0;
}

.shape-divider svg {
  position: relative;
  display: block;
  width: calc(100% + 1.3px);
  height: 80px;
}

.shape-divider .shape-fill {
  fill: var(--bg-color);
  opacity: 1;
}

/* 特点区域样式 */
.features {
  padding: 5rem 0;
  background-color: var(--bg-color);
}

.badge-wrapper {
  display: flex;
  justify-content: center;
  margin-bottom: 1rem;
}

.section-badge {
  display: inline-block;
  background: var(--gradient-primary);
  color: white;
  padding: 0.5rem 1rem;
  border-radius: var(--border-radius-full);
  font-weight: 600;
  font-size: 0.875rem;
}

.section-header {
  margin-bottom: 3rem;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
  color: var(--text-primary);
}

.section-description {
  font-size: 1.25rem;
  color: var(--text-secondary);
  max-width: 700px;
  margin: 0 auto;
}

.feature-card {
  padding: 2rem;
  border-radius: var(--border-radius-lg);
  background-color: var(--card-bg);
  box-shadow: var(--shadow);
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  border: 1px solid rgba(0, 0, 0, 0.05);
}

.feature-icon {
  margin-bottom: 1.5rem;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background-color: rgba(99, 102, 241, 0.1);
}

.feature-title {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 0.75rem;
  color: var(--text-primary);
}

.feature-description {
  color: var(--text-secondary);
  font-size: 1rem;
  line-height: 1.6;
}

/* 使用步骤样式 */
.how-it-works {
  padding: 6rem 0;
  background-color: var(--card-bg);
  position: relative;
  border-top: 1px solid var(--border-color);
  border-bottom: 1px solid var(--border-color);
}

.steps-container {
  max-width: 800px;
  margin: 0 auto;
}

.step-icon {
  font-size: 1.5rem;
}

/* 号召性用语样式 */
.cta {
  padding: 6rem 0;
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.9) 0%, rgba(20, 184, 166, 0.9) 100%);
  color: white;
  text-align: center;
  position: relative;
  overflow: hidden;
}

.cta::before {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-image: url("data:image/svg+xml,%3Csvg width='100' height='100' viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M11 18c3.866 0 7-3.134 7-7s-3.134-7-7-7-7 3.134-7 7 3.134 7 7 7zm48 25c3.866 0 7-3.134 7-7s-3.134-7-7-7-7 3.134-7 7 3.134 7 7 7zm-43-7c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zm63 31c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zM34 90c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zm56-76c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zM12 86c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm28-65c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm23-11c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm-6 60c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm29 22c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zM32 63c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm57-13c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm-9-21c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM60 91c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM35 41c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM12 60c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2z' fill='%23ffffff' fill-opacity='0.1' fill-rule='evenodd'/%3E%3C/svg%3E");
  opacity: 0.5;
}

.cta-content {
  max-width: 700px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
}

.cta-title {
  font-size: 3rem;
  font-weight: 800;
  margin-bottom: 1.5rem;
  line-height: 1.2;
}

.cta-description {
  font-size: 1.5rem;
  margin-bottom: 2.5rem;
  opacity: 0.9;
}

.cta-actions {
  display: flex;
  justify-content: center;
}

/* 动画效果 */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-10px); }
  100% { transform: translateY(0px); }
}

@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.05); }
  100% { transform: scale(1); }
}

.animate-fade-in {
  opacity: 0;
  animation: fadeIn 0.8s cubic-bezier(0.19, 1, 0.22, 1) forwards;
}

.animate-fade-in-delay-1 {
  opacity: 0;
  animation: fadeIn 0.8s cubic-bezier(0.19, 1, 0.22, 1) forwards;
  animation-delay: 0.2s;
}

.animate-fade-in-delay-2 {
  opacity: 0;
  animation: fadeIn 0.8s cubic-bezier(0.19, 1, 0.22, 1) forwards;
  animation-delay: 0.4s;
}

.animate-fade-in-delay-3 {
  opacity: 0;
  animation: fadeIn 0.8s cubic-bezier(0.19, 1, 0.22, 1) forwards;
  animation-delay: 0.6s;
}

.animate-fade-in-delay-4 {
  opacity: 0;
  animation: fadeIn 0.8s cubic-bezier(0.19, 1, 0.22, 1) forwards;
  animation-delay: 0.8s;
}

.animate-float {
  animation: float 4s ease-in-out infinite;
}

.pulse {
  animation: pulse 3s ease-in-out infinite;
}

/* 响应式适配 */
@media (max-width: 768px) {
  .hero {
    padding: 4rem 0 6rem;
  }
  
  .hero-content {
    flex-direction: column;
  }
  
  .hero-image {
    order: -1;
    justify-content: center;
    margin-bottom: 2rem;
  }
  
  .hero-title {
    font-size: 2.25rem;
    text-align: center;
  }
  
  .hero-subtitle {
    text-align: center;
  }
  
  .hero-actions {
    flex-direction: column;
    gap: 1rem;
  }
  
  .section-title {
    font-size: 2rem;
  }
  
  .section-description {
    font-size: 1.125rem;
  }
  
  .cta-title {
    font-size: 2.25rem;
  }
  
  .cta-description {
    font-size: 1.25rem;
  }
}
</style> 