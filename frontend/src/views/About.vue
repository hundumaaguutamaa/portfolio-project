<template>
  <div>
    <!-- Button Section -->
    <router-link to="/" class="home-button">Go to Home</router-link>
    
    <!-- Content Section -->
    <div style="background-color:#D9EEE1; padding: 20px; border-radius: 10px; font-family: Arial, sans-serif; margin-top: 20px;">
      <h3 style="color: #2E8B57; text-align: center;">Dispatch Route</h3>
      <p style="font-size: 16px; line-height: 1.6; color: #333;">
        Streamline the process of assigning customer requests to the appropriate IT teams with ease. Dispatch Route ensures accurate assignments, saves time, and facilitates correct routing. Say goodbye to mis-assignments, delays, and the hassle of determining the right IT team for customer requests.
      </p>
    </div>
  </div>
</template>

<script>
export default {
  // Add any necessary script here
};
</script>

<style scoped>
.home-button {
  display: inline-block;
  padding: 5px 10px; /* Reduced padding for a smaller button */
  margin-top: 20px;
  background-color: #42b983;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  font-weight: bold;
  font-size: 12px; /* Smaller font size */
}

.home-button:hover {
  background-color: #36a472;
}
</style>
