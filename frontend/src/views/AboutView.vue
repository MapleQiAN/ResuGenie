<template>
  <div class="about-view">
    <div class="container">
      <n-space vertical size="large">
        <div class="page-header">
          <h1 class="page-title">关于 ResuGenie</h1>
          <p class="page-description">用AI为求职者赋能，让简历创作更简单</p>
        </div>
        
        <n-card class="about-card">
          <div class="about-content">
            <div class="about-section">
              <h2>我们的故事</h2>
              <p>ResuGenie 诞生于一个简单的想法：求职过程不应该如此复杂和令人沮丧。</p>
              <p>作为曾经的求职者，我们深知做出一份令面试官满意的简历有多么困难，尤其是对于尚未有过求职经历的大学生们。简历应该清晰展示您的技能和成就，但大多数人很难客观地评估自己的经历并以专业的方式呈现。</p>
              <p>因此，我们创建了 ResuGenie，一个基于AI的平台，帮助求职者轻松创建、优化和完善他们的简历，让才华得到应有的认可。</p>
            </div>
            
            <div class="about-section">
              <h2>我们的使命</h2>
              <p>ResuGenie 的使命是通过技术赋能求职者，帮助他们以最佳方式展示自己的价值。</p>
              <p>我们相信：</p>
              <ul>
                <li>每个人都应该有机会获得理想的工作机会</li>
                <li>技术应该简化复杂的流程，而不是增加障碍</li>
                <li>人工智能可以辅助人类决策，而非替代它</li>
              </ul>
            </div>
            
            <div class="about-section">
              <h2>我们的技术</h2>
              <p>ResuGenie 采用尖端的自然语言处理技术和大型语言模型，为用户提供智能化的简历创作体验。</p>
              <p>我们的AI系统经过专业招聘文档的深度训练，能够理解各行业的招聘标准和要求，为您的简历提供针对性的优化建议。</p>
              <p>与此同时，我们坚持"以人为本"的设计理念，确保技术服务于用户需求，而不是相反。</p>
            </div>
            
            <div class="about-section">
              <h2>团队</h2>
              <p>ResuGenie 团队由来自不同背景的热情创造者组成，包括软件工程师、设计师、人力资源专家和教育工作者。我们的多元化背景使我们能够从不同角度理解求职挑战，并打造出真正有价值的解决方案。</p>
            </div>
            
            <div class="about-section">
              <h2>愿景</h2>
              <p>我们期望 ResuGenie 成为全球求职者的得力助手，不仅帮助他们创建引人注目的简历，还能提供全方位的求职支持。</p>
              <p>未来，我们计划拓展更多功能，包括：</p>
              <ul>
                <li>针对不同行业和职位的专业化简历指导</li>
                <li>面试准备和模拟训练</li>
                <li>个性化的职业发展规划</li>
                <li>更多语言支持，服务全球用户</li>
              </ul>
            </div>
            
            <div class="about-section">
              <h2>联系我们</h2>
              <p>我们很乐意听取您的反馈和建议！</p>
              <p>电子邮件：<a href="mailto:contact@resugenie.com">contact@resugenie.com</a></p>
              <p>GitHub：<a href="https://github.com/MapleQiAN/ResuGenie" target="_blank">https://github.com/MapleQiAN/ResuGenie</a></p>
            </div>
          </div>
        </n-card>
      </n-space>
    </div>
  </div>
</template>

<script setup>
import { NSpace, NCard } from 'naive-ui'
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

.about-card {
  margin-bottom: 3rem;
}

.about-content {
  max-width: 800px;
  margin: 0 auto;
}

.about-section {
  margin-bottom: 2.5rem;
}

.about-section h2 {
  font-size: 1.75rem;
  color: var(--text-primary);
  margin-bottom: 1rem;
  position: relative;
  padding-left: 1rem;
}

.about-section h2:before {
  content: "";
  position: absolute;
  left: 0;
  top: 0.5rem;
  bottom: 0.5rem;
  width: 4px;
  background: linear-gradient(to bottom, var(--primary-color), var(--secondary-color));
  border-radius: 2px;
}

.about-section p {
  margin-bottom: 1rem;
  line-height: 1.7;
  color: var(--text-secondary);
}

.about-section ul {
  margin-left: 1.5rem;
  margin-bottom: 1rem;
}

.about-section li {
  margin-bottom: 0.5rem;
  color: var(--text-secondary);
}

.about-section a {
  color: var(--primary-color);
  text-decoration: none;
}

.about-section a:hover {
  text-decoration: underline;
}
</style> 