<template>
  <div class="price-container">
    <div class="price-header">
      <span class="amount">${{ price }}</span>
      <span class="period">night</span>
    </div>
    <div class="total-reviews">
      <span class="rating">★ 4.95</span>
      <span class="reviews">(153 reviews)</span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

const price = ref(150);
</script>

<style scoped>
.price-container {
  padding: var(--spacing-medium);
  border: var(--border-width) solid var(--color-contrast-secondary);
  border-radius: var(--border-radius);
  box-shadow: var(--box-shadow-medium);
}

.price-header {
  display: flex;
  align-items: baseline;
  gap: var(--spacing-small);
}

.amount {
  font-size: var(--font-size-large);
  font-weight: var(--font-weight-bold);
  color: var(--color-font-dark);
}

.period {
  color: var(--color-font-muted-light);
}

.total-reviews {
  margin-top: var(--spacing-small);
  font-size: var(--font-size-small);
}

.rating {
  color: var(--color-primary);
}

.reviews {
  color: var(--color-font-muted-light);
  margin-left: var(--spacing-small);
}
</style>
