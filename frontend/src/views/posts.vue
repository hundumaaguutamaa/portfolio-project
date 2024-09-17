<template>
  <div class="posts">
    <Header /> <!-- Using the Header component -->
    <Navbar /> <!-- Using the Navbar component -->
   
    <h1> Hellooo Amanuel</h1>
 
      <h2> Helen Dispatching today.</h2>
  <p>
      ALX Africa 

  </p>
  </div>
  <Footer /> <!-- Using the Navbar component -->
</template>

<script>
import Header from '../components/Header.vue';
import Navbar from '../components/Navbar.vue';
import Footer from '../components/Footer.vue';

export default {
  name: 'Posts',
  components: {
    Header,
    Navbar,
    Footer
  },
}
</script>

<style scoped>
/* Add your component-specific styles here */
</style>
