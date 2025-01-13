import pluginVue from "eslint-plugin-vue";
import vueTsEslintConfig from "@vue/eslint-config-typescript";
import pluginVitest from "@vitest/eslint-plugin";
import pluginCypress from "eslint-plugin-cypress/flat";
import skipFormatting from "@vue/eslint-config-prettier/skip-formatting";
import globals from "globals";
import pluginJs from "@eslint/js";
import eslintConfigPrettier from "eslint-config-prettier";
import prettierPlugin from "eslint-plugin-prettier";
import typescriptEslintPlugin from "@typescript-eslint/eslint-plugin";

export default [
  {
    name: "app/files-to-lint",
    files: ["**/*.{ts,mts,tsx,vue,js}"],
  },
  {
    languageOptions: {
      globals: {
        ...globals.browser,
        ...globals.node,
      },
      parser: "@typescript-eslint/parser",
      parserOptions: {
        ecmaVersion: "latest",
        sourceType: "module",
        ecmaFeatures: {
          jsx: true,
        },
      },
    },
  },
  pluginJs.configs.recommended,
  {
    plugins: {
      vue: pluginVue,
      prettier: prettierPlugin,
      "@typescript-eslint": typescriptEslintPlugin,
    },
  },
  {
    rules: {
      ...eslintConfigPrettier.rules,
      "no-unused-vars": "warn",
      "no-undef": "error",
      "no-console": "warn",
      "no-debugger": "warn",
      "no-constant-condition": "warn",
      semi: [2, "always"],
      "max-len": [
        "warn",
        { code: 120, ignorePattern: "^import\\s.+\\sfrom\\s.+;$" },
      ],
      "no-multiple-empty-lines": ["warn", { max: 1, maxEOF: 1 }],
      quotes: [
        "error",
        "single",
        { allowTemplateLiterals: true, avoidEscape: true },
      ],
      "import/extensions": "off",
      "import/prefer-default-export": "off",
      "max-lines-per-function": ["off", 40],
      "padding-line-between-statements": [
        "error",
        {
          blankLine: "always",
          prev: "*",
          next: ["if", "for", "while", "switch"],
        },
        { blankLine: "always", prev: "*", next: "return" },
        { blankLine: "always", prev: ["const", "let"], next: "*" },
        { blankLine: "always", prev: "*", next: ["const", "let"] },
        {
          blankLine: "any",
          prev: ["const", "let"],
          next: ["export", "const", "let"],
        },
      ],
    },
  },
  ...pluginVue.configs["flat/essential"],
  ...vueTsEslintConfig(),
  {
    ...pluginVitest.configs.recommended,
    files: ["src/**/__tests__/*"],
  },
  {
    ...pluginCypress.configs.recommended,
    files: [
      "cypress/e2e/**/*.{cy,spec}.{js,ts,jsx,tsx}",
      "cypress/support/**/*.{js,ts,jsx,tsx}",
    ],
  },
  skipFormatting,
  {
    ignores: [
      ".config/*",
      "node_modules/*",
      "build/**/*",
      "*.spec.js",
      "backend/server.js",
    ],
  },
];
