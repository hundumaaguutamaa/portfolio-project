<template>
    <div>
      <nav class="navbar">
        <button class="button is-primary add-team-button" @click="addTeam">Add Team</button>
      </nav>
      <div class="page-content"></div>
  
      <!-- About Section -->
      <div class="about-container">
        <!-- Button Section -->
        <button @click="AddTeamExperties" class="AddTeamExp">Add Team Expertise</button>
  
        <!-- Content Section -->
        <div class="content-section">
          <h3>Dispatch Route</h3>
          <p class="enhanced-paragraph">
            Streamline the process of assigning customer requests to the appropriate IT teams with ease. Dispatch Route ensures accurate assignments, saves time, and facilitates correct routing. Say goodbye to mis-assignments, delays, and the hassle of determining the right IT team for customer requests.
          </p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      addTeam() {
        // Logic for adding a new team
        console.log('Add Team button clicked');
        // Add team logic here
      },
      AddTeamExperties() {
        // Logic for adding team expertise
        console.log('Add Team Expertise button clicked');
        // Add team expertise logic here
      }
    }
  }
  </script>
  
  <style scoped>
  .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .add-team-button {
    margin-top: 20px;
    margin-left: auto;
    position: absolute;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
  }
  
  .about-container {
    margin-top: 100px;
    padding: 20px;
    max-width: 600px;
    margin: 100px auto 0;
    text-align: center;
  }
  
  .AddTeamExp {
    margin-top: 20px;
    background-color: #42b983;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    font-size: 16px;
    cursor: pointer;
  }
  
  .AddTeamExp:hover {
    background-color: #36a472;
  }
  
  .content-section {
    background-color: #D9EEE1;
    padding: 20px;
    border-radius: 10px;
    margin-top: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  .content-section h3 {
    color: #2E8B57;
  }
  
  .enhanced-paragraph {
    font-size: 16px;
    line-height: 1.8;
    color: #333;
    background-color: #fff;
    padding: 15px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    text-align: left;
  }
  </style>
  