import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/HomeView.vue'),
    meta: {
      title: '首页 - ResuGenie'
    }
  },
  {
    path: '/create',
    name: 'create',
    component: () => import('@/views/CreateResumeView.vue'),
    meta: {
      title: '创建简历 - ResuGenie'
    }
  },
  {
    path: '/optimize',
    name: 'optimize',
    component: () => import('@/views/OptimizeResumeView.vue'),
    meta: {
      title: '优化简历 - ResuGenie'
    }
  },
  {
    path: '/help',
    name: 'help',
    component: () => import('@/views/HelpView.vue'),
    meta: {
      title: '帮助中心 - ResuGenie'
    }
  },
  {
    path: '/faq',
    name: 'faq',
    component: () => import('@/views/FAQView.vue'),
    meta: {
      title: '常见问题 - ResuGenie'
    }
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('@/views/AboutView.vue'),
    meta: {
      title: '关于我们 - ResuGenie'
    }
  },
  // 404页面
  {
    path: '/:pathMatch(.*)*',
    name: 'not-found',
    component: () => import('@/views/NotFoundView.vue'),
    meta: {
      title: '页面未找到 - ResuGenie'
    }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

// 全局前置守卫 - 设置页面标题
router.beforeEach((to, from, next) => {
  document.title = to.meta.title || 'ResuGenie · AI简历生成与优化助手'
  next()
})

export default router 