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
              <n-button size="large" class="btn-animated optimize-btn" round @click="handleOptimizeResume">
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

          <div class="steps-container">
            <n-grid cols="1 s:1 m:3" x-gap="24" y-gap="24" responsive="screen">
              <!-- 步骤 1 -->
              <n-gi>
                <div class="step-card animate-step-1">
                  <div class="step-number">1</div>
                  <div class="step-icon-wrapper">
                    <n-icon size="42" class="step-icon">
                      <edit-icon />
                    </n-icon>
                  </div>
                  <h3 class="step-title">填写个人信息</h3>
                  <p class="step-description">输入您的基本信息、教育背景、工作经历等</p>
                  <div class="step-arrow">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M5 12H19M19 12L12 5M19 12L12 19" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                  </div>
                </div>
              </n-gi>
              
              <!-- 步骤 2 -->
              <n-gi>
                <div class="step-card animate-step-2">
                  <div class="step-number">2</div>
                  <div class="step-icon-wrapper">
                    <n-icon size="42" class="step-icon">
                      <template-icon />
                    </n-icon>
                  </div>
                  <h3 class="step-title">选择简历模板</h3>
                  <p class="step-description">从多种专业设计的模板中选择您喜欢的风格</p>
                  <div class="step-arrow">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M5 12H19M19 12L12 5M19 12L12 19" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                  </div>
                </div>
              </n-gi>
              
              <!-- 步骤 3 -->
              <n-gi>
                <div class="step-card animate-step-3">
                  <div class="step-number">3</div>
                  <div class="step-icon-wrapper">
                    <n-icon size="42" class="step-icon">
                      <download-icon />
                    </n-icon>
                  </div>
                  <h3 class="step-title">生成并优化</h3>
                  <p class="step-description">AI 生成简历内容，提供优化建议并导出 PDF</p>
                  <div class="step-success">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M20 6L9 17L4 12" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                  </div>
                </div>
              </n-gi>
            </n-grid>
          </div>

          <!-- <div class="steps-illustration animate-fade-in-delay-3">
            <img src="@/assets/images/resume-steps.svg" alt="简历创建步骤" class="steps-image" />
          </div> -->
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
  padding: 4rem 0 8rem;
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(20, 184, 166, 0.15) 100%);
  position: relative;
  overflow: hidden;
  backdrop-filter: blur(10px);
}

.hero::before {
  content: '';
  position: absolute;
  top: -50%;
  right: -50%;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle, rgba(255,255,255,0.3) 0%, rgba(255,255,255,0) 70%);
  transform: rotate(-45deg);
  animation: lightMove 15s infinite linear;
}

@keyframes lightMove {
  0% { transform: rotate(-45deg) translateX(0); }
  50% { transform: rotate(-45deg) translateX(10%); }
  100% { transform: rotate(-45deg) translateX(0); }
}

.hero-content {
  display: flex;
  align-items: center;
  gap: 3rem;
  max-width: 1200px;
  margin: 0 auto;
}

.hero-text {
  flex: 1;
}

.hero-title {
  font-size: 3rem;
  font-weight: 800;
  margin-bottom: 1.5rem;
  line-height: 1.1;
  position: relative;
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
  background: linear-gradient(90deg, rgba(79, 70, 229, 0.5) 0%, rgba(20, 184, 166, 0.5) 100%);
  border-radius: 4px;
  z-index: -1;
  animation: highlightPulse 2s infinite;
}

@keyframes highlightPulse {
  0% { opacity: 0.6; transform: scaleX(0.96); }
  50% { opacity: 1; transform: scaleX(1.04); }
  100% { opacity: 0.6; transform: scaleX(0.96); }
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
  flex-wrap: wrap; /* 允许按钮换行 */
}

.hero-actions .n-button {
  padding: 0 1.5rem;
  height: 3rem;
  font-size: 1rem;
  position: relative;
  overflow: hidden;
  border-radius: rem;
}

.btn-animated::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, rgba(255,255,255,0) 0%, rgba(255,255,255,0.2) 50%, rgba(255,255,255,0) 100%);
  transform: translateX(-100%);
  transition: transform 0.6s;
}

.btn-animated:hover::before {
  transform: translateX(100%);
}

.optimize-btn {
  border: 2px solid var(--primary-color);
  background: transparent;
  color: var(--primary-color);
  box-shadow: 0 4px 15px rgba(99, 102, 241, 0.1);
  transition: all 0.3s ease;
}

.optimize-btn:hover {
  background: rgba(99, 102, 241, 0.1);
  box-shadow: 0 8px 20px rgba(99, 102, 241, 0.2);
}

.icon-margin-right {
  margin-right: 8px;
  display: inline-flex;
  vertical-align: middle;
  transition: transform 0.3s ease;
}

.btn-animated:hover .icon-margin-right {
  transform: scale(1.2) rotate(10deg);
}

.hero-image {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  max-width: 50%;
  position: relative;
}

.hero-image::after {
  content: '';
  position: absolute;
  width: 140%;
  height: 140%;
  background: radial-gradient(circle, rgba(99, 102, 241, 0.2) 0%, rgba(20, 184, 166, 0.1) 30%, transparent 70%);
  border-radius: 50%;
  z-index: -1;
  animation: pulseGradient 8s infinite alternate;
}

@keyframes pulseGradient {
  0% { transform: scale(0.9); opacity: 0.6; }
  100% { transform: scale(1.1); opacity: 0.8; }
}

.hero-image img {
  width: 100%;
  max-width: 500px;
  height: auto;
  object-fit: contain;
  filter: drop-shadow(0 10px 20px rgba(0, 0, 0, 0.15));
  transition: transform 0.5s ease, filter 0.5s ease;
}

.hero-image:hover img {
  transform: translateY(-10px);
  filter: drop-shadow(0 15px 25px rgba(0, 0, 0, 0.2));
}

/* 装饰形状分隔符 */
.shape-divider {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  overflow: hidden;
  line-height: 0;
  transform: translateY(1px);
}

.shape-divider svg {
  position: relative;
  display: block;
  width: calc(100% + 1.3px);
  height: 60px;
  transform: rotate(180deg);
}

.shape-divider .shape-fill {
  fill: var(--bg-color);
}

/* 特点区域样式 */
.features {
  padding: 5rem 0;
  background-color: var(--bg-color);
  position: relative;
  z-index: 1;
}

.features::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: 
    radial-gradient(circle at 20% 30%, rgba(99, 102, 241, 0.05) 0%, transparent 15%),
    radial-gradient(circle at 80% 70%, rgba(20, 184, 166, 0.05) 0%, transparent 15%);
  z-index: -1;
}

.badge-wrapper {
  display: flex;
  justify-content: center;
  margin-bottom: 1rem;
}

.section-badge {
  display: inline-block;
  background: linear-gradient(90deg, rgba(99, 102, 241, 0.9) 0%, rgba(20, 184, 166, 0.9) 100%);
  color: white;
  padding: 0.5rem 1rem;
  border-radius: var(--border-radius-full);
  font-weight: 600;
  font-size: 0.875rem;
  box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
  animation: badgePulse 2s infinite;
}

@keyframes badgePulse {
  0% { box-shadow: 0 4px 12px rgba(99, 102, 241, 0.2); }
  50% { box-shadow: 0 4px 20px rgba(99, 102, 241, 0.4); }
  100% { box-shadow: 0 4px 12px rgba(99, 102, 241, 0.2); }
}

.section-header {
  margin-bottom: 3rem;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
  color: var(--text-primary);
  background: linear-gradient(90deg, #333, #555);
  background-clip: text;
  -webkit-background-clip: text;
  color: transparent;
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
  background-color: rgba(255,255,255,0.7);
  box-shadow: var(--shadow);
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  border: 1px solid rgba(0, 0, 0, 0.05);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  backdrop-filter: blur(5px);
  position: relative;
  z-index: 1;
  overflow: hidden;
}

.feature-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, rgba(255,255,255,0.25) 0%, rgba(255,255,255,0) 100%);
  z-index: -1;
}

.card-hover:hover {
  transform: translateY(-10px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.feature-icon {
  margin-bottom: 1.5rem;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 80px;
  height: 80px;
  border-radius: 16px;
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(20, 184, 166, 0.15) 100%);
  padding: 16px;
  position: relative;
  transition: all 0.5s ease;
  box-shadow: 0 5px 15px rgba(99, 102, 241, 0.1);
  z-index: 1;
}

.feature-icon::before {
  content: '';
  position: absolute;
  inset: 2px;
  background: rgba(255, 255, 255, 0.8);
  border-radius: 14px;
  z-index: -1;
  backdrop-filter: blur(5px);
}

.feature-icon::after {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.5) 0%, rgba(20, 184, 166, 0.5) 100%);
  border-radius: 16px;
  opacity: 0;
  z-index: -2;
  transition: opacity 0.5s ease;
}

.feature-card:hover .feature-icon {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(99, 102, 241, 0.25);
}

.feature-card:hover .feature-icon::after {
  opacity: 0.6;
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
  background: var(--bg-color);
  position: relative;
  border-top: 1px solid rgba(0, 0, 0, 0.05);
  border-bottom: 1px solid rgba(0, 0, 0, 0.05);
  overflow: hidden;
}

.how-it-works::before {
  content: '';
  position: absolute;
  top: -50%;
  right: -50%;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle, rgba(99, 102, 241, 0.05) 0%, rgba(20, 184, 166, 0.05) 70%);
  border-radius: 50%;
  z-index: 0;
}

.how-it-works::after {
  content: '';
  position: absolute;
  bottom: -50%;
  left: -50%;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle, rgba(20, 184, 166, 0.05) 0%, rgba(99, 102, 241, 0.05) 70%);
  border-radius: 50%;
  z-index: 0;
}

.steps-container {
  position: relative;
  z-index: 1;
  margin-bottom: 3rem;
}

/* 步骤卡片样式 */
.step-card {
  position: relative;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.8) 0%, rgba(255, 255, 255, 0.95) 100%);
  border-radius: var(--border-radius-lg);
  padding: 2.5rem 2rem 2rem;
  box-shadow: var(--shadow);
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  border: 1px solid rgba(0, 0, 0, 0.05);
  transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
  z-index: 1;
  backdrop-filter: blur(10px);
  overflow: visible;
  margin-top: 25px;
}

.step-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 6px;
  background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
  opacity: 0.8;
  transition: height 0.3s ease;
}

.step-card:hover {
  transform: translateY(-15px);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
}

.step-card:hover::before {
  height: 8px;
}

.step-number {
  position: absolute;
  top: -20px;
  left: 50%;
  transform: translateX(-50%);
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  color: white;
  font-weight: 700;
  font-size: 1.25rem;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 10px rgba(99, 102, 241, 0.3);
  z-index: 2;
  overflow: visible;
}

.step-icon-wrapper {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(20, 184, 166, 0.1) 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.5rem;
  transition: all 0.3s ease;
  position: relative;
}

.step-icon-wrapper::after {
  content: '';
  position: absolute;
  top: -5px;
  left: -5px;
  right: -5px;
  bottom: -5px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
  opacity: 0;
  z-index: -1;
  transition: opacity 0.3s ease;
}

.step-card:hover .step-icon-wrapper {
  transform: scale(1.1);
  background: rgba(255, 255, 255, 0.8);
}

.step-card:hover .step-icon-wrapper::after {
  opacity: 0.3;
  animation: rotateBorder 3s linear infinite;
}

@keyframes rotateBorder {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.step-icon {
  color: var(--primary-color);
  transition: all 0.3s ease;
}

.step-card:hover .step-icon {
  transform: scale(1.2);
  color: var(--secondary-color);
}

.step-title {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
  color: var(--text-primary);
  position: relative;
  display: inline-block;
}

.step-title::after {
  content: '';
  position: absolute;
  bottom: -5px;
  left: 50%;
  transform: translateX(-50%);
  width: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
  transition: width 0.3s ease;
}

.step-card:hover .step-title::after {
  width: 80%;
}

.step-description {
  color: var(--text-secondary);
  font-size: 1rem;
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.step-arrow {
  color: var(--primary-color);
  width: 30px;
  height: 30px;
  transition: all 0.3s ease;
  opacity: 0.7;
}

.step-card:hover .step-arrow {
  transform: translateX(5px);
  opacity: 1;
  color: var(--secondary-color);
}

.step-success {
  color: var(--success-color, #10b981);
  width: 30px;
  height: 30px;
  transition: all 0.3s ease;
  opacity: 0.7;
}

.step-card:hover .step-success {
  transform: scale(1.2);
  opacity: 1;
}

/* 在小屏幕上隐藏箭头 */
@media (max-width: 768px) {
  .step-arrow {
    display: none;
  }
}

/* 步骤插图 */
.steps-illustration {
  max-width: 800px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
  display: flex;
  justify-content: center;
}

.steps-image {
  max-width: 100%;
  height: auto;
  filter: drop-shadow(0 10px 20px rgba(0, 0, 0, 0.1));
  transition: all 0.5s ease;
}

.steps-illustration:hover .steps-image {
  transform: translateY(-5px);
  filter: drop-shadow(0 15px 30px rgba(0, 0, 0, 0.15));
}

/* 动画样式 */
.animate-step-1 {
  animation: fadeInStep 0.8s cubic-bezier(0.19, 1, 0.22, 1) forwards;
  animation-delay: 0.1s;
  opacity: 0;
}

.animate-step-2 {
  animation: fadeInStep 0.8s cubic-bezier(0.19, 1, 0.22, 1) forwards;
  animation-delay: 0.3s;
  opacity: 0;
}

.animate-step-3 {
  animation: fadeInStep 0.8s cubic-bezier(0.19, 1, 0.22, 1) forwards;
  animation-delay: 0.5s;
  opacity: 0;
}

@keyframes fadeInStep {
  from {
    opacity: 0;
    transform: translateY(30px) scale(0.95);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
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

.cta::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle at 50% 50%, rgba(255,255,255,0.2) 0%, rgba(255,255,255,0) 50%);
  pointer-events: none;
  animation: ctaGlow 8s infinite alternate;
}

@keyframes ctaGlow {
  0% { opacity: 0.3; transform: scale(1); }
  100% { opacity: 0.8; transform: scale(1.5); }
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
  text-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.cta-description {
  font-size: 1.5rem;
  margin-bottom: 2.5rem;
  opacity: 0.9;
  text-shadow: 0 1px 5px rgba(0,0,0,0.1);
}

.cta-actions {
  display: flex;
  justify-content: center;
}

.cta .btn-animated {
  background-color: rgba(255,255,255,0.9);
  color: var(--primary-color);
  font-weight: 600;
  box-shadow: 0 5px 20px rgba(0,0,0,0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.cta .btn-animated:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.15);
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