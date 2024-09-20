import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';  // Make sure this component exists and is correctly imported
import About from '../views/About.vue';
import Footer from '../views/Footer.vue';
import SearchRequest from '../views/SearchRequest.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },

  {
    path: '/about',
    name: 'About',
    component: About
  },

  {
    path: '/Search',
    name: 'SearchRequest',
    component: SearchRequest,
  },
];

// Create and configure the router
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),  // Use import.meta.env.BASE_URL for Vite
  routes,
});

export default router
