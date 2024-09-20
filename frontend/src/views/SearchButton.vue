<template>
    <button @click="$emit('search')" class="search-button">
      Search
    </button>
  </template>
  
  <script>
  export default {
    name: 'SearchButton',
  };
  </script>
  
  <style scoped>
  .search-button {
    padding: 10px 20px;
    font-size: 1rem;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    margin-top: 20px;
  }
  
  .search-button:hover {
    background-color: #0056b3;
  }
  </style>
  