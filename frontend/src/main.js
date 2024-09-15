import "bootstrap/dist/css/bootstrap.css"; // Import Bootstrap CSS
import { createApp } from 'vue';
import './style.css'; // Your own global styles
import router from './router';
import App from './App.vue';

// Import Bootstrap JS (includes Popper.js for tooltips, dropdowns, etc.)
import "bootstrap/dist/js/bootstrap.bundle.js"; // Make sure Popper.js is included

const app = createApp(App);

// Uncomment if you're using Pinia or Vuex for state management
// import { createPinia } from 'pinia'; 
// app.use(createPinia()); // or Vuex if applicable

app.use(router); // Add the router to the Vue app

app.mount('#app'); // Mount the app to the DOM element with id 'app'
