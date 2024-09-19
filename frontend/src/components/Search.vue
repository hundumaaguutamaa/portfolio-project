<template>
    <div>
      <form @submit.prevent="handleSearch" class="d-flex ms-auto">
        <input 
          v-model="searchQuery" 
          class="form-control me-2 rounded-pill small-search-input" 
          type="search" 
          placeholder="Search..." 
          aria-label="Search"
        >
        <button class="btn btn-outline-primary rounded-pill" type="submit">Search</button>
      </form>
      
      <!-- Display search results -->
      <div v-if="searchResults.length">
        <ul>
          <li v-for="(result, index) in searchResults" :key="index">
            {{ result.service_name }}
          </li>
        </ul>
      </div>
  
      <div v-else-if="searchExecuted">
        <p>No results found</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        searchQuery: '',  // To store the search input
        searchResults: [],  // To store the results from the API
        searchExecuted: false,  // To track if the search was executed
      };
    },
    methods: {
      async handleSearch() {
        if (this.searchQuery) {
          try {
            const response = await fetch(`/http://127.0.0.1:8000/teamsq=${this.searchQuery}`);
            const data = await response.json();
            this.searchResults = data.results;
          } catch (error) {
            console.error('Error fetching search results:', error);
          }
        } else {
          this.searchResults = [];
        }
        this.searchExecuted = true;
      },
    },
  };
  </script>
  
  <style scoped>
  /* Styling to minimize the search input size and placeholder */
  .small-search-input {
    height: 30px;
    font-size: 14px;
    padding: 5px 10px;
    width: 200px; /* You can adjust this width based on your design */
  }
  
  .small-search-input::placeholder {
    font-size: 12px; /* Smaller font size for the placeholder */
    color: #aaa;     /* Slightly lighter color for the placeholder */
  }
  
  .btn {
    padding: 5px 15px;
    font-size: 14px;
  }
  </style>
  