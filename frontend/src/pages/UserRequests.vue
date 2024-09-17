// src/components/UserRequests.vue
<template>
  <div>
    <h1>User Requests</h1>
    <ul>
      <li v-for="request in userRequests" :key="request.request_id">
        {{ request.request_description }} - {{ request.request_status }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      userRequests: []
    };
  },
  mounted() {
    axios.get('userrequests/')
      .then(response => {
        this.userRequests = response.data;
      })
      .catch(error => {
        console.error('Error fetching user requests:', error);
      });
  }
};
</script>
