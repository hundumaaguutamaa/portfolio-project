<template>
  <div>
    <h1>Corporate IT Teams Expertise </h1>
    
    <!-- Add Logout button -->
    
    <button @click="logout" class="logout-button">Logout</button>
    
    
    <!-- Flex container for teams list -->
    <div class="teams-container">
      <div class="team-card" v-for="team in teams" :key="team.team_id">
        <h2>{{ team.team_name }}</h2>
        <p>Expertise Areas:</p>
        <ul>
          <li v-for="area in team.expertise_areas" :key="area.id">{{ area.name }}</li>
        </ul>
      </div>
    </div>

    <!-- Show login overlay if not authenticated -->
    <LoginOverlay v-if="!isAuthenticated" @login-success="handleLoginSuccess" />
  </div>
</template>

<script>
import { onMounted, ref } from 'vue';
import axios from 'axios';
import LoginOverlay from './LoginOverlay.vue'; // Import the LoginOverlay component

export default {
  name: "EmployeeList",
  components: {
    LoginOverlay
  },
  setup() {
    const teams = ref([]);
    const isAuthenticated = ref(!!localStorage.getItem('access_token')); // Check if user is authenticated

    const fetchTeams = () => {
      axios.get('http://127.0.0.1:8000/teams/')
        .then((resp) => {
          teams.value = resp.data; // Assign the response data to the teams variable
        })
        .catch((error) => {
          console.error("Error fetching teams:", error);
        });
    };

    onMounted(() => {
      if (isAuthenticated.value) {
        fetchTeams(); // Fetch teams only if authenticated
      }
    });

    const logout = () => {
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
      isAuthenticated.value = false; // Update authentication status
      window.location.href = '/login'; // Redirect to login page
    };

    const handleLoginSuccess = () => {
      isAuthenticated.value = true; // Update authentication status
      fetchTeams(); // Fetch teams after login
      window.location.href = '/home'; // Redirect to home after login
    };

    return {
      teams,
      logout,
      isAuthenticated,
      handleLoginSuccess
    };
  }
};
</script>

<style scoped>
/* Main container */
div {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

/* Heading styles */
h1 {
  text-align: center;
  color: #333;
  margin-bottom: 20px;
}

/* Flex container for teams */
.teams-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: space-around;
}

/* Flex items (individual team cards) */
.team-card {
  background-color: #f9f9f9;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  flex: 1 1 calc(33% - 40px); /* Make the cards responsive (3 cards per row) */
  transition: transform 0.2s;
}

.team-card:hover {
  transform: translateY(-2px);
}

/* Subheading styles */
h2 {
  margin: 0;
  font-size: 1.5rem;
  color: #007bff;
}

/* Expertise area list */
p {
  margin: 10px 0;
  font-weight: bold;
}

ul {
  list-style-type: none;
  padding: 0;
}

ul > li {
  background-color: #e9ecef;
  margin-top: 5px;
  padding: 10px;
  border-radius: 3px;
}

/* Add styling for Logout button */
.logout-button-container {
  position: relative;
}

.logout-button {
  background-color: #dc3545;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  cursor: pointer;
  position: absolute;
  top: 30px;
  right: 400px;
}


.logout-button:hover {
  background-color: #c82333;
}
</style>
