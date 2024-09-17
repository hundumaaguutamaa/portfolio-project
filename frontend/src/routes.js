import { createRouter, createWebHistory } from 'vue-router';
import Posts from './views/posts.vue';  // Make sure this component exists and is correctly imported

const routes = [
  {
    path: '/',
    name: 'posts',
    component: Posts,
  },
];

// Create and configure the router
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),  // Use import.meta.env.BASE_URL for Vite
  routes,
});

export default router;
