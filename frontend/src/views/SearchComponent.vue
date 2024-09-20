<template>
    <div>
      <input v-model="query" @input="search" placeholder="Search by team or expertise area" />
      <div v-if="results.length">
        <h3>Search Results:</h3>
        <ul>
          <li v-for="result in results" :key="result.id">{{ result.name }}</li>
        </ul>
      </div>
      <div v-else>
        <p>No results found</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        query: '',
        results: []
      };
    },
    methods: {
      async search() {
        if (this.query.length > 2) {
          try {
            const response = await axios.get(`/api/search/?q=${this.query}`);
            this.results = response.data;
          } catch (error) {
            console.error(error);
          }
        } else {
          this.results = [];
        }
      }
    }
  };
  </script>
  
  <style scoped>
  /* Add your styles here */
  </style>
  