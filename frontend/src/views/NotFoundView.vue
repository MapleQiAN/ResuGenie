<template>
  <div class="not-found-view">
    <div class="container">
      <div class="not-found-content">
        <div class="not-found-icon">
          <n-icon size="128" color="var(--primary-color)">
            <alert-circle-icon />
          </n-icon>
        </div>
        <h1 class="not-found-title">404</h1>
        <p class="not-found-description">很抱歉，您访问的页面不存在</p>
        <div class="not-found-actions">
          <n-button type="primary" @click="goHome">
            返回首页
          </n-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { NButton, NIcon } from 'naive-ui'
import { AlertCircle as AlertCircleIcon } from '@vicons/ionicons5'

const router = useRouter()

// 跳转到首页
const goHome = () => {
  router.push('/')
}
</script>

<style scoped>
.not-found-view {
  min-height: calc(100vh - 64px - 60px);
  display: flex;
  align-items: center;
  justify-content: center;
}

.not-found-content {
  text-align: center;
  padding: 4rem 1rem;
}

.not-found-icon {
  margin-bottom: 1rem;
}

.not-found-title {
  font-size: 6rem;
  font-weight: 700;
  color: var(--primary-color);
  margin: 0;
  line-height: 1.2;
  background-image: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
  background-clip: text;
  -webkit-background-clip: text;
  color: transparent;
}

.not-found-description {
  font-size: 1.5rem;
  color: var(--text-secondary);
  margin-bottom: 2rem;
}

.not-found-actions {
  margin-top: 2rem;
}
</style> 