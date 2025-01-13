<template>
  <div class="price-container">
    <div class="price-header">
      <span class="amount">${{ currentPrice }}</span>
      <span class="period">night</span>
    </div>
    <div class="total-reviews">
      <span class="rating">★ {{ currentRating }}</span>
      <span class="reviews">(153 reviews)</span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from "vue";

const props = defineProps<{
  price_per_night: number;
  rating: number;
  id: number;
}>();

const currentPrice = ref(props.price_per_night);
const currentRating = ref(props.rating);

let ws: WebSocket;

onMounted(() => {
  ws = new WebSocket("ws://localhost:8000/ws");

  ws.onopen = () => {
    ws.send(
      JSON.stringify({
        action: "subscribe",
        price: props.price_per_night,
        id: props.id,
      }),
    );
  };

  ws.onmessage = (event) => {
    try {
      const data =
        typeof event.data === "string" ? JSON.parse(event.data) : event.data;

      if (data.type === "price_updates" && Array.isArray(data.updates)) {
        const priceUpdate = data.updates.find(
          (p: { id: number; price: number }) => p.id === props.id,
        );

        if (priceUpdate) {
          currentPrice.value = priceUpdate.price;
        }
      }
    } catch (error) {
      console.error("Error parsing WebSocket message:", error);
    }
  };

  ws.onclose = () => {
    console.log("WebSocket connection closed");
  };

  ws.onerror = (error) => {
    console.error("WebSocket error:", error);
  };
});

onBeforeUnmount(() => {
  if (ws) {
    ws.close();
  }
});
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
