<template>
    <div>
      <h1>IT Teams</h1>
      <ul v-if="teams.length">
        <li v-for="team in teams" :key="team.team_id">
          {{ team.team_name }} - Expertise: {{ team.expertise_areas }}
        </li>
      </ul>
      <p v-else>No teams found.</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'ITTeamList',
    data() {
      return {
        teams: []
      };
    },
    mounted() {
      this.fetchTeams();
    },
    methods: {
      async fetchTeams() {
        try {
          const response = await axios.get('http://localhost:8000/api/it-teams/');
          this.teams = response.data;
        } catch (error) {
          console.error('Error fetching teams:', error);
        }
      }
    }
  };
  </script>