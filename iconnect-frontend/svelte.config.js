// import adapter from '@sveltejs/adapter-static';
// import adapter from '@sveltejs/adapter-auto';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';
// import { preprocess } from 'svelte/compiler';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	preprocess: vitePreprocess(),
}

export default config;
