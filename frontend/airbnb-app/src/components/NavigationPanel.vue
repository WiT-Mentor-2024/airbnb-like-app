<script setup lang="ts">
import { ref } from "vue";

const navItems = ref([
  { icon: "mdi-home", text: "Home", route: "/" },
  { icon: "mdi-heart", text: "Wishlists", route: "/wishlists" },
  { icon: "mdi-account", text: "Profile", route: "/profile" },
  { icon: "mdi-information", text: "About", route: "/about" },
]);
</script>

<template>
  <nav class="nav-panel">
    <div class="logo">
      <!-- Add your logo here -->
    </div>
    <div class="nav-items">
      <router-link
        v-for="item in navItems"
        :key="item.text"
        :to="item.route"
        class="nav-item"
      >
        <v-icon>{{ item.icon }}</v-icon>
        <span>{{ item.text }}</span>
      </router-link>
    </div>
  </nav>
</template>

<style scoped>
.nav-panel {
  width: 250px;
  background: var(--color-bg-light);
  border-right: 1px solid #ebebeb;
  padding: 20px;
}

.nav-items {
  margin-top: 30px;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  text-decoration: none;
  color: var(--color-font-dark);
  border-radius: 8px;
  margin-bottom: 8px;
}

.nav-item:hover {
  background: #f7f7f7;
}

.nav-item.router-link-active {
  color: var(--color-primary);
  background: #fff1f1;
}
</style>
