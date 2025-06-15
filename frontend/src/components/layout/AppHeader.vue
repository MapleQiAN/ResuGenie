<template>
  <header class="app-header">
    <div class="header-content">
      <router-link to="/" class="logo">
        <div class="logo-icon">
          <n-icon size="28" color="var(--primary-color)">
            <magic-icon />
          </n-icon>
        </div>
        <h1 class="logo-text">ResuGenie</h1>
      </router-link>

      <nav class="nav-desktop">
        <n-menu v-model:value="activeKey" mode="horizontal" :options="menuOptions" />
      </nav>
      
      <div class="header-actions">
        <n-button
          quaternary
          circle
          @click="toggleTheme"
          class="theme-toggle"
        >
          <template #icon>
            <n-icon size="22">
              <moon-icon v-if="!isDarkMode" />
              <sun-icon v-else />
            </n-icon>
          </template>
        </n-button>
        
        <n-button class="header-btn btn-animated" type="primary" round @click="handleStartNow">
          <n-icon class="icon-margin-right" size="18"><rocket-icon /></n-icon>
          立即体验
        </n-button>
        
        <n-button quaternary class="menu-toggle" @click="showDrawer = true">
          <template #icon>
            <n-icon size="24">
              <menu-icon />
            </n-icon>
          </template>
        </n-button>
      </div>
    </div>
    
    <!-- 移动端菜单 -->
    <n-drawer v-model:show="showDrawer" :width="280" placement="right">
      <n-drawer-content title="菜单">
        <n-menu
          v-model:value="activeKey"
          :options="menuOptions"
          :indent="18"
          @update:value="handleMobileMenuClick"
        />
        <div class="drawer-footer">
          <n-button class="btn-animated" type="primary" block round @click="handleMobileStartNow">
            <n-icon class="icon-margin-right"><rocket-icon /></n-icon>
            立即体验
          </n-button>
        </div>
      </n-drawer-content>
    </n-drawer>
  </header>
</template>

<script setup>
import { h, ref, inject, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { NIcon, NMenu, NButton, NDrawer, NDrawerContent } from 'naive-ui'
import { 
  ColorWand as MagicIcon, 
  Moon as MoonIcon, 
  Sunny as SunIcon, 
  Menu as MenuIcon,
  Home as HomeIcon,
  DocumentText as FileTextIcon,
  Create as EditIcon,
  HelpCircle as HelpCircleIcon,
  Eye as PreviewIcon,
  Rocket as RocketIcon,
  ChatbubbleEllipses as ChatbubbleEllipsesIcon
} from '@vicons/ionicons5'

const isDarkMode = inject('isDarkMode')
const toggleTheme = inject('toggleTheme')

const router = useRouter()
const route = useRoute()

// 移动端菜单控制
const showDrawer = ref(false)

// 当前激活的菜单项
const activeKey = computed(() => route.name)

// 处理移动端菜单点击
const handleMobileMenuClick = () => {
  showDrawer.value = false
}

// 处理移动端的"立即体验"按钮点击
const handleMobileStartNow = () => {
  showDrawer.value = false
  router.push('/create')
}

// 菜单项配置
const menuOptions = [
  {
    label: () => h('div', { class: 'menu-item' }, '首页'),
    key: 'home',
    icon: renderIcon(HomeIcon),
    onClick: () => router.push('/')
  },
  {
    label: () => h('div', { class: 'menu-item' }, '创建简历'),
    key: 'create',
    icon: renderIcon(FileTextIcon),
    onClick: () => router.push('/create')
  },
  {
    label: () => h('div', { class: 'menu-item' }, '优化简历'),
    key: 'optimize',
    icon: renderIcon(EditIcon),
    onClick: () => router.push('/optimize')
  },
  {
    label: () => h('div', { class: 'menu-item' }, '简历预览'),
    key: 'preview',
    icon: renderIcon(PreviewIcon),
    onClick: () => router.push('/preview')
  },
  {
    label: () => h('div', { class: 'menu-item' }, '帮助中心'),
    key: 'help',
    icon: renderIcon(HelpCircleIcon),
    onClick: () => router.push('/help')
  }
]

// 渲染图标助手函数
function renderIcon(icon) {
  return () => h(NIcon, null, { default: () => h(icon) })
}

// 处理"立即体验"按钮点击
const handleStartNow = () => {
  router.push('/create')
}
</script>

<style scoped>
.app-header {
  background-color: var(--card-bg);
  box-shadow: var(--shadow);
  position: sticky;
  top: 0;
  z-index: 100;
  transition: all 0.3s ease;
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  background-color: rgba(255, 255, 255, 0.9);
}

:deep(.n-menu) {
  background-color: transparent !important;
}

:deep(.n-menu-item-content) {
  display: flex;
  align-items: center;
  margin: 0 5px;
}

:deep(.n-menu-item-content::before) {
  background-color: var(--primary-color) !important;
  height: 3px !important;
  border-radius: 3px 3px 0 0;
}

:deep(.n-menu-item-content-header) {
  font-weight: 600;
}

:deep(.n-base-menu-item--selected) .menu-item::after {
  width: 100%;
}

.header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 70px;
  padding: 0 24px;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
}

.logo {
  display: flex;
  align-items: center;
  text-decoration: none;
  color: var(--text-primary);
  position: relative;
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
  width: 40px;
  height: 40px;
  animation: pulse 2s infinite ease-in-out;
}

@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.1); }
  100% { transform: scale(1); }
}

.logo-text {
  font-size: 1.75rem;
  font-weight: 800;
  margin: 0;
  background-image: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
  background-clip: text;
  -webkit-background-clip: text;
  color: transparent;
  letter-spacing: -0.5px;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 12px;
}

.theme-toggle {
  margin-right: 4px;
  transition: transform 0.3s ease;
}

.theme-toggle:hover {
  transform: rotate(30deg);
}

.icon-margin-right {
  margin-right: 8px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.menu-toggle {
  display: none;
}

.menu-item {
  position: relative;
  padding: 0 6px;
  font-weight: 600;
  display: flex;
  align-items: center;
}

.menu-item::after {
  content: '';
  position: absolute;
  bottom: -5px;
  left: 0;
  width: 0;
  height: 2px;
  background-color: var(--primary-color);
  transition: width 0.3s ease;
}

.menu-item:hover::after {
  width: 100%;
}

.drawer-footer {
  padding: 16px;
  margin-top: 24px;
}

/* 响应式适配 */
@media (max-width: 768px) {
  .nav-desktop {
    display: none;
  }
  
  .header-btn {
    display: none;
  }
  
  .menu-toggle {
    display: flex;
  }
  
  .logo-text {
    font-size: 1.5rem;
  }
  
  .header-content {
    height: 64px;
  }
}

:deep(.n-icon) {
  display: flex;
  justify-content: center;
  align-items: center;
}

.step-icon {
  font-size: 1.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style> 