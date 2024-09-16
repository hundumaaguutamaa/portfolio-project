<template>
  <div class="posts">
    <Header /> <!-- Using the Header component -->
    <Navbar /> <!-- Using the Navbar component -->
    <h1> Hellooo Amanuel</h1>
  </div>
</template>

<script>
import Header from '../components/Header.vue';
import Navbar from '../components/Navbar.vue';

export default {
  name: 'Posts',
  components: {
    Header,
    Navbar
  },
}
</script>

<style scoped>
/* Add your component-specific styles here */
</style>
