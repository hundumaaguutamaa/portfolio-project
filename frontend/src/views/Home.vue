<template>
  <div>
    <div class="search-container">
      <input
        type="text"
        v-model="searchQuery"
        placeholder="Search by team name or expertise area"
        @input="filterTeams"
        class="search-input"
      />
      <button @click="handleSearch" class="search-button">Search</button>
    </div>
    
    <div v-if="searchQuery" class="current-search">
      <p>Searching for: "{{ searchQuery }}"</p>
    </div>

    <div class="team-container">
      <div v-for="team in filteredTeams" :key="team.team_id" class="team-card">
        <h2 class="team-name">{{ team.team_name }}</h2>
        <p class="expertise-area">Expertise Area: {{ team.expertise_area }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"; // Importing axios to make HTTP requests

export default {
  data() {
    return {
      teams: [], // Initially empty, will be filled with backend data
      searchQuery: "", // Stores the search input
      filteredTeams: [], // Stores the filtered results
    };
  },
  created() {
    // Automatically fetch data when the component is created
    this.fetchTeams();
  },
  methods: {
    fetchTeams() {
      axios
        .get("http://127.0.0.1:8000/api/teams/") // Adjust this URL to match your Django API endpoint
        .then((response) => {
          this.teams = response.data; // Assign the backend data to the teams array
          this.filteredTeams = this.teams; // Initialize filtered teams with all teams
        })
        .catch((error) => {
          console.error("Error fetching teams:", error);
        });
    },
    handleSearch() {
      this.filterTeams(); // Call the filter function
      this.searchQuery = ""; // Clear the search input
    },
    filterTeams() {
      const query = this.searchQuery.toLowerCase(); // Normalize the query
      this.filteredTeams = this.teams.filter(team => 
        team.team_name.toLowerCase().includes(query) || 
        team.expertise_area.toLowerCase().includes(query)
      );
    },
  },
};
</script>

<style scoped>
.team-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  padding: 20px;
}

.search-container {
  margin-bottom: 30px; /* Increased space between search and teams */
}

.search-input {
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.search-button {
  padding: 10px 15px;
  font-size: 1rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-left: 10px; /* Space between input and button */
}

.search-button:hover {
  background-color: #0056b3;
}

.current-search {
  margin-bottom: 20px; /* Space for the current search text */
  font-style: italic;
}

.team-card {
  background-color: #f5f5f5;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 20px;
  transition: transform 0.3s ease;
}

.team-card:hover {
  transform: scale(1.05);
}

.team-name {
  font-size: 1.5rem;
  color: #333;
}

.expertise-area {
  font-size: 1.1rem;
  color: #777;
}
</style>
