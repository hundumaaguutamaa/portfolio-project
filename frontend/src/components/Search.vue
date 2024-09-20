<template>
  <div class="search-container">
    <h1>Search for IT Teams</h1>

    <!-- Search Inputs -->
    <div class="search-inputs">
      <input
        v-model="searchTerm"
        type="text"
        placeholder="Search by team name"
        class="input-field"
      />
      <input
        v-model="expertiseAreaTerm"
        type="text"
        placeholder="Search by expertise area"
        class="input-field"
      />
    </div>

    <!-- Search Button -->
    <SearchButton @search="handleSearch" />

    <!-- Placeholder for Results -->
    <div class="results-container" v-if="teams.length">
      <h2>Search Results:</h2>
      <ul>
        <li v-for="team in teams" :key="team.team_id">
          <h3>{{ team.team_name }}</h3>
          <ul>
            <li v-for="area in team.expertise_areas" :key="area.id">
              {{ area.name }}
            </li>
          </ul>
        </li>
      </ul>
    </div>

    <!-- Placeholder if no results -->
    <div v-else-if="searchPerformed">
      <p>No teams found for your search.</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import SearchButton from './SearchButton.vue'; // Importing SearchButton component

export default {
  name: 'SearchRequest',
  components: {
    SearchButton,
  },
  data() {
    return {
      searchTerm: '', // For team name input
      expertiseAreaTerm: '', // For expertise area input
      teams: [], // To store search results
      searchPerformed: false, // To track if a search was made
    };
  },
  methods: {
    handleSearch() {
      if (this.searchTerm || this.expertiseAreaTerm) {
        axios
          .get(
            `http://127.0.0.1:8000/api/search/?team_name=${this.searchTerm}&expertise_area=${this.expertiseAreaTerm}`
          )
          .then((response) => {
            this.teams = response.data; // Assuming response is an array of teams
            this.searchPerformed = true; // Mark that a search was made
          })
          .catch((error) => {
            console.error('Error fetching search results:', error);
          });
      } else {
        alert('Please enter a search term or expertise area.');
      }
    },
  },
};
</script>

<style scoped>
.search-container {
  padding: 20px;
  max-width: 600px;
  margin: 0 auto;
  text-align: center;
}

.input-field {
  margin: 10px;
  padding: 10px;
  width: 250px;
  font-size: 1rem;
}

.results-container {
  margin-top: 20px;
}

h2 {
  margin-bottom: 10px;
}

li {
  list-style-type: none;
  padding: 5px;
}

ul {
  padding: 0;
}
</style>
