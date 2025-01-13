import type { Apartment } from "@/types/apartment";

const API_BASE_URL = "http://localhost:8000";

export const apartmentService = {
  async getApartments(): Promise<Apartment[]> {
    try {
      const response = await fetch(`${API_BASE_URL}/api/apartments`);

      if (!response.ok) {
        throw new Error("Failed to fetch apartments");
      }

      return await response.json();
    } catch (error) {
      console.error("Error fetching apartments:", error);
      throw error;
    }
  },
};
