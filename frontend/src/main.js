import { createApp } from 'vue';  // Import createApp from Vue 3
import App from './App.vue';  // Import your App component
import router from './routes.js';  // Import the router
import 'bootstrap/dist/css/bootstrap.min.css';  // Import Bootstrap CSS



// Create and mount the Vue app
createApp(App)
  .use(router)  // Use the router
  .mount('#app');  // Mount the app to the DOM element with id="app"
