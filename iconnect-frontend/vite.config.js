import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
// import { createMakeHot } from 'svelte-hmr';

export default defineConfig({
	plugins: [
		sveltekit(),
	],
});
