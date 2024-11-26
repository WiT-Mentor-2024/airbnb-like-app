<script setup lang="ts">
import NavigationPanel from "@/components/NavigationPanel.vue";
</script>

<template>
  <div class="app-container">
    <NavigationPanel />
    <main class="main-content">
      <router-view v-slot="{ Component }">
        <transition name="slide" mode="out-in">
          <Suspense timeout="0">
            <div>
              <component :is="Component"></component>
            </div>
          </Suspense>
        </transition>
      </router-view>
    </main>
  </div>
</template>

<style scoped>
.app-container {
  display: flex;
  min-height: 100vh;
}

.main-content {
  flex: 1;
  padding: 20px;
}
</style>
