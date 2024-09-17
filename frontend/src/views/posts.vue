<template>
  <div class="posts">
    <Header /> <!-- Using the Header component -->
    <Navbar /> <!-- Using the Navbar component -->
    <Search /> <!-- Using the Search component -->

   <div class="shadowbox">
      <p> Helen Dispatching today. </p>
      </div>
 
  </div>
  <Footer /> <!-- Using the Navbar component -->
</template>

<script>
import Header from '../components/Header.vue';
import Navbar from '../components/Navbar.vue';
import Search from '../components/Search.vue';
import Footer from '../components/Footer.vue';

export default {
  name: 'Posts',
  components: {
    Header,
    Navbar,
    Search,
    Footer
  },
}
</script>

<style scoped>
/* Add your component-specific styles here */
</style>
