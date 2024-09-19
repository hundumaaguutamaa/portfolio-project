import { createApp } from 'vue';  // Import createApp from Vue 3

import App from './views/App.vue'; // Specify the exact file
import router from './router';  // Import the router
import 'bootstrap/dist/css/bootstrap.min.css';  // Import Bootstrap CSS


// Create and mount the Vue app
createApp(App).use(router).mount('#app');  // Mount the app to the DOM element with id="app"
