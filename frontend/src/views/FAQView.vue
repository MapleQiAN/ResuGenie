<template>
  <div style="display: none">FAQ页面将重定向到帮助中心</div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// 页面加载时重定向到帮助中心的FAQ选项卡
onMounted(() => {
  // 添加一个短暂延迟以确保路由系统已完全准备好
  setTimeout(() => {
    router.replace({ 
      path: '/help',
      query: { tab: 'faq' }
    })
  }, 50)
})
</script> 