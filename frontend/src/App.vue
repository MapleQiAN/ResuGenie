<template>
  <n-config-provider :theme="theme" :theme-overrides="themeOverrides">
    <n-loading-bar-provider>
      <n-dialog-provider>
        <n-notification-provider>
          <n-message-provider>
            <AppLayout>
              <router-view v-slot="{ Component }">
                <transition name="slide-fade" mode="out-in">
                  <component :is="Component" />
                </transition>
              </router-view>
            </AppLayout>
          </n-message-provider>
        </n-notification-provider>
      </n-dialog-provider>
    </n-loading-bar-provider>
  </n-config-provider>
</template>

<script setup>
import { ref, provide } from 'vue'
import { 
  darkTheme, 
  NConfigProvider, 
  NLoadingBarProvider, 
  NDialogProvider, 
  NNotificationProvider, 
  NMessageProvider,
  useDialog
} from 'naive-ui'
import AppLayout from '@/components/layout/AppLayout.vue'
import { useMediaQuery } from '@vueuse/core'

// 获取对话框API
const dialog = useDialog()
// 提供对话框服务
provide('dialog', dialog)

// 通过系统偏好检测是否使用深色模式
const prefersDark = useMediaQuery('(prefers-color-scheme: dark)')

// 应用主题状态
const theme = ref(null)
const isDarkMode = ref(prefersDark.value)

// 监听深色模式变化
const toggleDarkMode = (isDark) => {
  isDarkMode.value = isDark
  theme.value = isDark ? darkTheme : null
}

// 切换深色模式
const toggleTheme = () => {
  toggleDarkMode(!isDarkMode.value)
}

// 提供全局的主题切换功能
provide('toggleTheme', toggleTheme)
provide('isDarkMode', isDarkMode)

// 自定义主题覆盖配置 - 更新为更加年轻、有活力的配色
const themeOverrides = {
  common: {
    primaryColor: '#6366f1',
    primaryColorHover: '#4f46e5',
    primaryColorPressed: '#4338ca',
    primaryColorSuppl: '#6366f1',
    infoColor: '#06b6d4',
    successColor: '#10b981',
    warningColor: '#facc15',
    errorColor: '#f43f5e',
    borderRadius: '10px'
  },
  LoadingBar: {
    colorLoading: '#6366f1'
  },
  Button: {
    borderRadiusSmall: '8px',
    borderRadius: '10px', 
    borderRadiusLarge: '12px',
    fontWeight: '600',
    textColorPrimary: 'white',
    colorOpacitySecondary: '0.15',
    borderColor: 'transparent'
  },
  Card: {
    borderRadius: '16px',
    boxShadow: '0 10px 15px -3px rgba(0, 0, 0, 0.1)',
    colorTarget: 'rgba(255, 255, 255, .9)',
    colorEmbedded: 'rgba(255, 255, 255, .9)'
  },
  Input: {
    borderRadius: '10px'
  },
  Select: {
    peers: {
      InternalSelection: {
        borderRadius: '10px'
      }
    }
  },
  Dropdown: {
    peers: {
      Popover: {
        borderRadius: '12px'
      }
    }
  }
}
</script>

<style>
/* 全局应用样式 */
html, body {
  height: 100%;
  overflow-x: hidden;
  scroll-behavior: smooth;
}

#app {
  height: 100%;
  display: flex;
  flex-direction: column;
  transition: background-color 0.3s ease, color 0.3s ease;
}

/* 全局过渡动画 */
*, *::before, *::after {
  transition: background-color 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
}

/* 文字选择样式 */
::selection {
  background-color: rgba(99, 102, 241, 0.2);
}

/* 滚动条美化 */
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0.05);
  border-radius: 4px;
}

::-webkit-scrollbar-thumb {
  background: rgba(99, 102, 241, 0.3);
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: rgba(99, 102, 241, 0.5);
}
</style>
