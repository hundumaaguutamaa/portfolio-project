<template>
  <div class="app">
    <div class="nav">
      <router-link to="/">Home</router-link>
      <router-link to="/About">About</router-link>
      <router-link to="/Search">Search</router-link>
      <!--  <router-link to="/Login">Login</router-link> -->
      
    </div>
    
    <!-- This renders the current view based on the route -->
    <router-view />

    <!-- Footer component will be rendered at the bottom of every page -->
    <Footer />
  </div>
</template>

<script>
import Footer from '../views/Footer.vue'; // Import the Footer component

export default {
  components: {
    Footer, // Register the Footer component
  },
};
</script>

<style>
.app {
  display: flex;                /* Use flexbox layout */
  flex-direction: column;       /* Stack children vertically */
  min-height: 100vh;           /* Ensure the app takes at least the full viewport height */
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.nav {
  padding: 30px;
  display: flex;               /* Use flexbox for alignment */
  justify-content: center;     /* Center items horizontally */
}

.nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
  padding: 10px 20px;         /* Add horizontal padding */
  margin: 0 10px;             /* Add space between links */
  border-radius: 4px;
}

.nav a.router-link-exact-active {
  color: #42b983;
}

footer {
  margin-top: auto; /* Push footer to the bottom */
}
</style>
