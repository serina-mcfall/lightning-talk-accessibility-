import jsxA11y from 'eslint-plugin-jsx-a11y'
import react from 'eslint-plugin-react'
import tsParser from '@typescript-eslint/parser'

export default [
  {
    files: ['**/*.tsx', '**/*.jsx'],
    languageOptions: {
      parser: tsParser,
      parserOptions: {
        ecmaFeatures: { jsx: true },
        ecmaVersion: 'latest',
        sourceType: 'module',
      },
    },
    plugins: {
      'jsx-a11y': jsxA11y,
      react,
    },
    rules: {
      ...jsxA11y.configs.recommended.rules,
      // Override to "warn" (yellow squiggle) to match how CRA / Vite ship
      // these rules out of the box — and what Serina experienced in the
      // React state kata that seeded this talk.
      'jsx-a11y/click-events-have-key-events': 'warn',
      'jsx-a11y/no-static-element-interactions': 'warn',
    },
    settings: {
      react: { version: 'detect' },
    },
  },
]
