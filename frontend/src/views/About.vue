<template>
  <div>
    <h1>Thank you for visiting</h1>
    <h1>Content under development...</h1>
    <router-link to="/" class="home-button">Go to Home</router-link>
  </div>
</template>

<script>
export default {
  // Add any necessary script here
};
</script>

<style scoped>
.home-button {
  display: inline-block; /* Make it behave like a button */
  padding: 10px 20px;   /* Add some padding */
  margin-top: 20px;     /* Space above the button */
  background-color: #42b983; /* Background color */
  color: white;         /* Text color */
  text-decoration: none; /* Remove underline */
  border-radius: 4px;   /* Rounded corners */
  font-weight: bold;     /* Bold text */
}

.home-button:hover {
  background-color: #36a472; /* Darker shade on hover */
}
</style>
