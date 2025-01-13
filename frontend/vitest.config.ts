import { fileURLToPath } from "node:url";
import { mergeConfig, defineConfig, configDefaults } from "vitest/config";
import viteConfig from "./vite.config";

export default mergeConfig(
  viteConfig,
  defineConfig({
    test: {
      server: {
        deps: {
          inline: ["vuetify"],
        },
      },
      environment: "jsdom",
      include: ["src/**/*.spec.ts", "src/components/__tests__/*.spec.js"],
      exclude: [...configDefaults.exclude, "e2e/**"],
      root: fileURLToPath(new URL("./", import.meta.url)),
      globals: true,
    },
  }),
);
