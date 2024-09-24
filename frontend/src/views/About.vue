<template>
   <div>
      <nav class="navbar">
        <button class="button is-primary add-team-button" @click="addTeam">Add Team</button>
      </nav>
      <div class="page-content">
        </div>
    </div>
  <div class="about-container">
    <!-- Button Section -->
    <!--<router-link to="/" class="home-button">Go to Home</router-link> -->
    <button @click="AddTeamExperties" class="AddTeamExp">AddTeamExperties</button>

    
    <!-- Content Section -->
    <div class="content-section">
      <h3>Dispatch Route</h3>
      <p class="enhanced-paragraph">
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
.about-container {
  margin-top: 100px; /* Add top margin to avoid overlap with fixed nav */
  padding: 20px;
  max-width: 600px;
  margin: 100px auto 0; /* Center the container */
  text-align: center;
}

.home-button {
  display: inline-block;
  padding: 5px 10px; /* Reduced padding for a smaller button */
  margin-top: 20px; /* Add margin-top value */
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

.content-section {
  background-color: #D9EEE1;
  padding: 20px;
  border-radius: 10px;
  font-family: Arial, sans-serif;
  margin-top: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Add subtle shadow */
}

.content-section h3 {
  color: #2E8B57;
  text-align: center;
}

.enhanced-paragraph {
  font-size: 16px;
  line-height: 1.8; /* Increase line height for better readability */
  color: #333;
  background-color: #fff; /* Add background color */
  padding: 15px; /* Add padding */
  border-radius: 8px; /* Add rounded corners */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Add subtle shadow */
  text-align: left; /* Align text to the left */
}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .add-team-button {
    margin-top: 20px;
    margin-left: auto;
    /* New styles to position the button below the navigation */
    position: absolute;
    bottom: 20px; /* Adjust this value as needed */
    left: 50%; /* Center horizontally */
    transform: translateX(-50%);
  }
</style>
