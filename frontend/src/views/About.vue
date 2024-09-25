<template>
  <div>
    <nav class="navbar">
      <button class="button is-primary add-team-button" @click="addTeam">Add Team</button>
    </nav>
    <div class="page-content">
      <div class="button-container">
        <h2>Add Team and Exprtise</h2>
        <form @submit.prevent="submitTeam">
          <div>
            <label for="teamName">Team Name:</label>
            <input type="text" id="teamName" v-model="teamName" required>
          </div>
          <div>
            <label for="expertiseArea">Select Expertise Area:</label>
            <select v-model="selectedExpertise">
              <option v-for="expertise in expertiseAreas" :key="expertise.id" :value="expertise.id">
                {{ expertise.name }}
              </option>
            </select>
          </div>
          <button type="submit">Add Team</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      teamName: '',
      expertiseAreas: [],
      selectedExpertise: null,
    };
  },
  mounted() {
    this.fetchExpertiseAreas();
  },
  methods: {
    fetchExpertiseAreas() {
    // http://127.0.0.1:8000/admin/api/requestservice/
      axios.get('http://127.0.0.1:8000/admin/api/userrequest/')
        .then(response => {
          this.expertiseAreas = response.data;
        })
        .catch(error => {
          console.error("There was an error fetching the expertise areas!", error);
        });
    },
    submitTeam() {
  const teamData = {
    team_name: this.teamName,
    expertise_area: this.selectedExpertise
  };

  console.log("Submitting team data:", teamData); // Debugging log

  axios.post('http://127.0.0.1:8000/teams/', teamData)
    .then(response => {
      alert('Team added successfully!');
      this.teamName = '';
      this.selectedExpertise = null;
    })
    .catch(error => {
      console.error("There was an error adding the team!", error.response.data); // Log error response
    });
}
  }
};
</script>

<style scoped>
.about-container {
  margin-top: 100px;
  padding: 20px;
  max-width: 600px;
  margin: 100px auto 0;
  text-align: center;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.add-team-button {
  margin-top: 20px;
}

.button-container {
  display: flex;
  flex-direction: column; /* Stack items vertically */
  align-items: center;    /* Center items horizontally */
  margin-top: 20px;      /* Space between navbar and button */
}

button {
  background-color: #42b983;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  width: 100%;           /* Full width button */
}

button:hover {
  background-color: #36a472;
}

form {
  margin: 20px 0;       /* Add space between the form and button */
  width: 20%;          /* Make the form full width */
}

label {
  display: block;
  margin-bottom: 5px;
}

input, select {
  margin-bottom: 10px;
  padding: 5px;
  width: 100%;
}
</style>
