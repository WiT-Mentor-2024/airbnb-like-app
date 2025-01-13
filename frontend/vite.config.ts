import { fileURLToPath, URL } from "node:url";
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import vueJsx from "@vitejs/plugin-vue-jsx";
import vueDevTools from "vite-plugin-vue-devtools";
import AutoImport from "unplugin-auto-import/vite";
import vuetify from "vite-plugin-vuetify";

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueJsx(),
    vuetify({ autoImport: true }),
    vueDevTools(),
    AutoImport({
      imports: [
        // presets
        "vue",
        "vue-router",
        "vuex",
        // custom
        {
          "@vueuse/core": [
            // named imports
            "useMouse",
            // alias
            ["useFetch", "useMyFetch"],
          ],
          axios: [
            // default imports
            ["default", "axios"],
          ],
        },
      ],
      dts: true, // auto generate `auto-imports.d.ts` file
    }),
  ],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
  ssr: {
    noExternal: ["vuetify", "@inertiajs/server"],
  },
});
