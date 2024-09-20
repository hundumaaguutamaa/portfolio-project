import { createApp } from 'vue';  // Import createApp from Vue 3
import App from './views/App.vue'; // Specify the exact file
import router from './router';  // Import the router
import 'bootstrap/dist/css/bootstrap.min.css';  // Import Bootstrap CSS
import 'bootstrap';  // Import Bootstrap JS
// Create the Vue app
const app = createApp(App);

// Use the router
app.use(router);

// Mount the app to the DOM element with id="app"
app.mount('#app');
