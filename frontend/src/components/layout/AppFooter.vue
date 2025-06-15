<template>
  <footer class="app-footer">
    <div class="footer-wave">
      <svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
        <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z" class="shape-fill"></path>
      </svg>
    </div>
    
    <div class="footer-content container">
      <div class="footer-logo">
        <router-link to="/" class="logo">
          <div class="logo-icon">
            <n-icon size="24" color="var(--primary-color)">
              <magic-icon />
            </n-icon>
          </div>
          <h2 class="logo-text">ResuGenie</h2>
        </router-link>
        <p class="slogan">让简历说人话</p>
        <div class="newsletter">
          <p class="newsletter-text">订阅获取最新资讯和求职技巧</p>
          <div class="newsletter-form">
            <n-input-group>
              <n-input placeholder="输入您的邮箱" round />
              <n-button type="primary" ghost round>
                订阅
              </n-button>
            </n-input-group>
          </div>
        </div>
      </div>
      
      <div class="footer-links">
        <div class="link-group">
          <h3>产品</h3>
          <router-link to="/create" class="footer-link">创建简历</router-link>
          <router-link to="/optimize" class="footer-link">优化简历</router-link>
          <router-link to="/templates" class="footer-link">简历模板</router-link>
        </div>
        
        <div class="link-group">
          <h3>帮助</h3>
          <router-link to="/help" class="footer-link">使用教程</router-link>
          <router-link to="/faq" class="footer-link">常见问题</router-link>
          <a href="#" class="footer-link">用户反馈</a>
        </div>
        
        <div class="link-group">
          <h3>关于</h3>
          <router-link to="/about" class="footer-link">关于我们</router-link>
          <a href="#" class="footer-link">博客</a>
          <a href="mailto:contact@resugenie.com" class="footer-link">联系我们</a>
        </div>
      </div>
    </div>
    
    <div class="footer-bottom container">
      <p>© {{ currentYear }} ResuGenie. 保留所有权利</p>
      <div class="social-links">
        <n-tooltip placement="top" trigger="hover">
          <template #trigger>
            <n-button quaternary circle class="social-btn">
              <template #icon><n-icon><github-icon /></n-icon></template>
            </n-button>
          </template>
          GitHub
        </n-tooltip>
        
        <n-tooltip placement="top" trigger="hover">
          <template #trigger>
            <n-button quaternary circle class="social-btn">
              <template #icon><n-icon><logo-twitter-icon /></n-icon></template>
            </n-button>
          </template>
          Twitter
        </n-tooltip>
        
        <n-tooltip placement="top" trigger="hover">
          <template #trigger>
            <n-button quaternary circle class="social-btn">
              <template #icon><n-icon><logo-linkedin-icon /></n-icon></template>
            </n-button>
          </template>
          LinkedIn
        </n-tooltip>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { computed } from 'vue'
import { NIcon, NButton, NTooltip, NInput, NInputGroup } from 'naive-ui'
import { ColorWand as MagicIcon } from '@vicons/ionicons5'
import { 
  LogoGithub as GithubIcon, 
  LogoTwitter as LogoTwitterIcon,
  LogoLinkedin as LogoLinkedinIcon
} from '@vicons/ionicons5'

// 当前年份
const currentYear = computed(() => new Date().getFullYear())
</script>

<style scoped>
.app-footer {
  background-color: var(--card-bg);
  position: relative;
  border-top: 1px solid var(--border-color);
  padding: 4rem 0 1.5rem;
  margin-top: 3rem;
}

.footer-wave {
  position: absolute;
  top: -60px;
  left: 0;
  width: 100%;
  overflow: hidden;
  line-height: 0;
  transform: rotate(180deg);
}

.footer-wave svg {
  position: relative;
  display: block;
  width: calc(100% + 1.3px);
  height: 60px;
  transform: rotateY(180deg);
}

.footer-wave .shape-fill {
  fill: var(--card-bg);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
}

.footer-content {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  margin-bottom: 3rem;
}

.footer-logo {
  flex: 1;
  min-width: 300px;
}

.logo {
  display: flex;
  align-items: center;
  text-decoration: none;
  color: var(--text-primary);
  margin-bottom: 0.75rem;
  transition: transform 0.3s ease;
}

.logo:hover {
  transform: scale(1.05);
}

.logo-icon {
  margin-right: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 32px;
  height: 32px;
}

.logo-text {
  font-size: 1.5rem;
  font-weight: 700;
  margin: 0;
  background-image: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
  background-clip: text;
  -webkit-background-clip: text;
  color: transparent;
}

.slogan {
  color: var(--text-secondary);
  margin-top: 0.5rem;
  font-size: 1rem;
  margin-bottom: 1.5rem;
}

.newsletter {
  margin-top: 1.5rem;
}

.newsletter-text {
  color: var(--text-secondary);
  margin-bottom: 1rem;
  font-size: 0.95rem;
}

.newsletter-form {
  max-width: 100%;
}

:deep(.n-input) {
  border-top-right-radius: 0;
  border-bottom-right-radius: 0;
}

:deep(.n-button) {
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
}

.footer-links {
  display: flex;
  flex-wrap: wrap;
  gap: 4rem;
}

.link-group {
  display: flex;
  flex-direction: column;
  min-width: 140px;
}

.link-group h3 {
  font-size: 1.1rem;
  margin-bottom: 1.25rem;
  color: var(--text-primary);
  position: relative;
  padding-bottom: 10px;
}

.link-group h3::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 30px;
  height: 3px;
  background: var(--gradient-primary);
  border-radius: 3px;
}

.footer-link {
  color: var(--text-secondary);
  text-decoration: none;
  margin-bottom: 0.75rem;
  font-size: 0.95rem;
  transition: all 0.2s ease;
  position: relative;
  padding-left: 0;
}

.footer-link:hover {
  color: var(--primary-color);
  padding-left: 8px;
}

.footer-link::before {
  content: '';
  position: absolute;
  left: 0;
  top: 50%;
  width: 0;
  height: 2px;
  background-color: var(--primary-color);
  transform: translateY(-50%);
  opacity: 0;
  transition: all 0.2s ease;
}

.footer-link:hover::before {
  width: 4px;
  opacity: 1;
}

.footer-bottom {
  padding-top: 1.5rem;
  border-top: 1px solid var(--border-color);
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.9rem;
  color: var(--text-light);
}

.social-links {
  display: flex;
  gap: 12px;
}

.social-btn {
  transition: transform 0.3s ease, background-color 0.3s ease;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 36px;
  height: 36px;
}

.social-btn:hover {
  transform: translateY(-3px);
  background-color: rgba(99, 102, 241, 0.1);
}

:deep(.n-icon) {
  display: flex;
  justify-content: center;
  align-items: center;
}

/* 响应式适配 */
@media (max-width: 768px) {
  .app-footer {
    padding-top: 3rem;
  }
  
  .footer-content {
    flex-direction: column;
    gap: 2.5rem;
  }
  
  .footer-links {
    gap: 2rem;
  }
  
  .footer-bottom {
    flex-direction: column;
    gap: 1.25rem;
    align-items: center;
    text-align: center;
  }
}
</style> 