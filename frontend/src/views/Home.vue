<template>
  <div class="team-container">
    <div v-for="team in teams" :key="team.team_id" class="team-card">
      <h2 class="team-name">{{ team.team_name }}</h2>
      <p class="expertise-area">Expertise Area: {{ team.expertise_area }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      teams: [
        { team_id: 1, team_name: "EUD Team", expertise_area: "Provide Desktop Computer" },
        { team_id: 2, team_name: "Network Support Team", expertise_area: "Add WiFi Access Point" },
        // Add other teams here
      ],
    };
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
