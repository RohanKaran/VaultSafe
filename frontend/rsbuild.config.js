import { defineConfig, loadEnv } from '@rsbuild/core';
import { pluginReact } from '@rsbuild/plugin-react';

export default defineConfig(({ envMode }) => {
  const { publicVars } = loadEnv({
    cwd: __dirname,
    mode: envMode,
    prefixes: ['REACT_APP_', 'PUBLIC_'],
  });

  return {
    plugins: [pluginReact()],
    html: {
      template: './public/index.html',
    },
    server: {
      port: 3000,
    },
    source: {
      define: publicVars,
    },
  };
});
