<template>
  <div class="home">
    <div v-if="loading" class="loading">Загрузка...</div>
    <div v-else-if="error" class="error">
      {{ error }}
    </div>
    <div v-else class="listings-grid">
      <div
        class="listing-card"
        v-for="apartment in apartments"
        :key="apartment.id"
      >
        <div class="listing-image">
          <img
            :src="apartment.imageUrl || 'https://placehold.co/600x400'"
            :alt="apartment.title"
            class="listing-image"
          />
        </div>

        <PriceDisplay
          :id="apartment.id"
          :price_per_night="apartment.price_per_night"
          :rating="apartment.rating"
        />

        <div class="listing-info">
          <h3>{{ apartment.title }}</h3>
          <p>{{ apartment.location }}</p>
          <p>{{ apartment.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import PriceDisplay from "@/components/PriceDisplay.vue";
import { apartmentService } from "@/services/apartmentService";
import type { Apartment } from "@/types/apartment";

const apartments = ref<Apartment[]>([]);
const loading = ref(true);
const error = ref<string | null>(null);

onMounted(async () => {
  try {
    apartments.value = await apartmentService.getApartments();
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
  } catch (_e: unknown) {
    error.value = "Ошибка при загрузке данных";
  } finally {
    loading.value = false;
  }
});
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

.loading,
.error {
  text-align: center;
  padding: var(--spacing-large);
  font-size: var(--font-size-large);
}

.error {
  color: var(--color-error);
}
</style>
