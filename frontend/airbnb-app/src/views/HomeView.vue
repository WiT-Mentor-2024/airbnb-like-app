<template>
  <div class="home">
    <div class="listings-grid">
      <div class="listing-card" v-for="n in 6" :key="n">
        <div class="listing-image">
          <img src="https://placehold.co/300x200" alt="Listing image" />
        </div>

        <PriceDisplay />

        <div class="listing-info">
          <h3>Cozy Apartment {{ n }}</h3>
          <p>Beautiful location</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import PriceDisplay from "@/components/PriceDisplay.vue";
</script>

<style scoped>
.listings-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: var(--spacing-large);
  padding: var(--spacing-large);
}

.listing-card {
  border-radius: var(--border-radius);
  overflow: hidden;
  transition: transform 0.2s;
  background-color: var(--color-bg-light);
  box-shadow: var(--box-shadow-small);
}

.listing-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--box-shadow-medium);
}

.listing-image {
  width: 100%;
  aspect-ratio: 3/2;
  overflow: hidden;
}

.listing-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.listing-info {
  padding: var(--spacing-medium);
}

.listing-info h3 {
  margin: 0;
  font-size: var(--font-size-large);
  font-weight: var(--font-weight-medium);
}

.listing-info p {
  margin: 0;
  font-size: 0.9rem;
}
</style>
