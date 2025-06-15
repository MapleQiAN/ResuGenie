<template>
  <div class="app-layout">
    <AppHeader />
    
    <main class="app-main">
      <div class="main-content">
        <slot></slot>
      </div>
    </main>
    
    <AppFooter />
  </div>
</template>

<script setup>
import AppHeader from './AppHeader.vue'
import AppFooter from './AppFooter.vue'
</script>

<style scoped>
.app-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  overflow-x: hidden;
}

.app-main {
  flex: 1;
  display: flex;
  flex-direction: column;
  background-color: var(--bg-color);
  width: 100%;
}

.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  transition: all 0.3s ease;
}

@media (max-width: 768px) {
  .app-main {
    padding-top: 0;
  }
}
</style> 