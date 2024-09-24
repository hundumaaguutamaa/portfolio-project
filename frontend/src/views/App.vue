<template>
  <div class="app">
    <div class="nav">
      <img :src="logo" alt="Logo" class="logo" @click="goHome" />
      <router-link to="/">Home</router-link>
      <router-link to="/About">About</router-link>
      <router-link to="/Search">Search</router-link>
      
      <button @click="logout" class="logout-button">Logout</button>
       <!-- <router-link to="/Signup">Signup</router-link>-->
    </div>
    
    <!-- This renders the current view based on the route -->
    <router-view />

    <!-- Footer component will be rendered at the bottom of every page -->
    <Footer />
  </div>
</template>

<script>
import logo from '/src/logo.png'; // Correct path to the logo
import Footer from '../views/Footer.vue'; // Import the Footer component

export default {
  components: {
    Footer, // Register the Footer component
  },
  data() {
    return {
      logo // Add logo to the component's data
    };
  },
  methods: {
    goHome() {
      this.$router.push('/'); // Redirect to home page
    },
    logout() {
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
      this.$router.push('/login'); // Redirect to login page
    }
  }
};
</script>

<style>
.app {
  display: flex;                /* Use flexbox layout */
  flex-direction: column;       /* Stack children vertically */
  min-height: 100vh;            /* Ensure the app takes at least the full viewport height */
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.nav {
  position: fixed;             /* Fix the navigation bar at the top */
  top: 0;
  width: 100%;
  background-color: #fff;      /* Background color to match the design */
  padding: 30px;
  display: flex;               /* Use flexbox for alignment */
  align-items: center;         /* Center items vertically */
  justify-content: center;     /* Center items horizontally */
  box-shadow: 0 2px 5px rgba(0,0,0,0.1); /* Add a shadow for better visibility */
  z-index: 1000;               /* Ensure it stays above other content */
}

.logo {
  height: 40px;                /* Adjust the height as needed */
  margin-right: 20px;          /* Add some space between the logo and the links */
  cursor: pointer;             /* Change cursor to pointer to indicate it's clickable */
}

.nav a, .logout-button {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
  padding: 10px 20px;         /* Add horizontal padding */
  margin: 0 10px;             /* Add space between links */
  border-radius: 4px;
  background: none;
  border: none;
  cursor: pointer;
}

.nav a.router-link-exact-active {
  color: #42b983;
}

.logout-button:hover {
  color: #42b983;
}

.content {
  margin-top: 100px;           /* Add margin to avoid overlap with fixed nav */
  flex: 1;
  overflow-y: auto;
}

footer {
  position: fixed;             /* Fix the footer at the bottom */
  bottom: 0;
  width: 100%;
  background-color: #f1f1f1;
  text-align: center;
  padding: 10px;
  box-shadow: 0 -2px 5px rgba(0,0,0,0.1);
  z-index: 1000;               /* Ensure it stays above other content */
}
</style>
