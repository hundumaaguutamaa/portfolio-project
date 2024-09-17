<template>
    <div>
      <form @submit.prevent="handleSearch">
        <input v-model="searchQuery" placeholder="Search Teams" />
        <button type="submit">Search</button>
      </form>
      <div v-if="results.length">
        <h4>Search Results:</h4>
        <ul>
          <li v-for="team in results" :key="team.id">{{ team.name }}</li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        searchQuery: '',
        results: []
      };
    },
    methods: {
      async handleSearch() {
        try {
          const response = await axios.get(`http://localhost:8000/api/teams/?search=${this.searchQuery}`);
          this.results = response.data;
        } catch (error) {
          console.error(error);
        }
      }
    }
  };
  </script>
  