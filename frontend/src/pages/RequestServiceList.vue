<!-- src/components/RequestServiceList.vue -->
<template>
    <div>
      <h1>Request Services</h1>
      <ul>
        <li v-for="service in services" :key="service.service_id">
          {{ service.service_name }} - {{ service.description }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        services: []
      };
    },
    mounted() {
      axios.get('requestservices/')
        .then(response => {
          this.services = response.data;
        })
        .catch(error => {
          console.error('Error fetching request services:', error);
        });
    }
  };
  </script>
  