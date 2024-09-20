<template>
  <div>
    <h1>Teams List</h1>
    <ul>
      <li v-for="team in teams" :key="team.team_id">
        <h2>{{ team.team_name }}</h2>
        <p>Expertise Areas:</p>
        <ul>
          <li v-for="area in team.expertise_areas" :key="area.id">{{ area.name }}</li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script>
import { onMounted, ref } from 'vue'; // Importing necessary functions
import axios from 'axios';

export default {
  name: "EmployeeList",
  setup() {
    const teams = ref([]); // Create a reactive variable to hold teams

    onMounted(() => {
      axios.get('http://127.0.0.1:8000/teams/')
        .then((resp) => {
          // Assuming the response is an array of team objects
          teams.value = resp.data; // Assign the response data to the teams variable
          console.warn(resp.data); // Log the entire response for debugging
        })
        .catch((error) => {
          console.error("Error fetching teams:", error);
        });
    });

    return {
      teams, // Expose the teams variable to the template
    };
  }
};
</script>

<style scoped>
/* Main container */
div {
  max-width: 800px; /* Limit the width for better readability */
  margin: 0 auto; /* Center the container */
  padding: 20px; /* Add padding around the content */
  font-family: Arial, sans-serif; /* Set a clean font */
}

/* Heading styles */
h1 {
  text-align: center; /* Center the main heading */
  color: #333; /* Darker text for better contrast */
  margin-bottom: 20px; /* Space below the heading */
}

/* List styles */
ul {
  list-style-type: none; /* Remove default bullet points */
  padding: 0; /* Remove default padding */
}

li {
  background-color: #f9f9f9; /* Light background for list items */
  margin: 10px 0; /* Space between list items */
  border-radius: 5px; /* Rounded corners */
  padding: 15px; /* Inner padding for items */
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Subtle shadow */
  transition: transform 0.2s; /* Animation effect */
}

li:hover {
  transform: translateY(-2px); /* Lift effect on hover */
}

/* Subheading styles */
h2 {
  margin: 0; /* Remove default margin */
  font-size: 1.5rem; /* Slightly larger font size */
  color: #007bff; /* Blue color for team names */
}

/* Expertise area list */
p {
  margin: 5px 0; /* Space around paragraphs */
  font-weight: bold; /* Make the expertise label bold */
}

ul > li {
  background-color: #e9ecef; /* Lighter background for expertise areas */
  margin-top: 5px; /* Space above expertise area items */
  padding: 10px; /* Inner padding */
  border-radius: 3px; /* Slightly rounded corners */
}
</style>

