import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';  // Make sure this component exists and is correctly imported
import About from '../views/About.vue';
import Footer from '../views/Footer.vue';
import SearchRequest from '../views/SearchRequest.vue';
import Login from '../views/Login.vue';
// import AddTe from '../views/AddTe.vue';
import Signup from '../views/Signup.vue';

// Define the routes with meta information for requiring authentication
const routes = [
  { path: '/', redirect: '/home' },  // Redirect root path to /home
  { path: '/home', name: 'Home', component: Home, meta: { requiresAuth: true } },
  { path: '/about', name: 'About', component: About, meta: { requiresAuth: true } },
  { path: '/Search', name: 'SearchRequest', component: SearchRequest, meta: { requiresAuth: true } },
  { path: '/Login', name: 'Login', component: Login },
  { path: '/Signup', name: 'Signup', component: Signup },
];

// Create and configure the router
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),  // Use import.meta.env.BASE_URL for Vite
  routes,
});

// Add navigation guard to check authentication before each route
router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('access_token'); // Check if access_token exists in localStorage

  if (to.meta.requiresAuth && !isAuthenticated) {
    // If the route requires authentication and the user is not authenticated, redirect to Login
    next({ name: 'Login' });
  } else {
    // Otherwise, proceed to the route
    next();
  }
});

export default router;
