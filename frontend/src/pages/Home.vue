<template>
  <div>
    <!-- Full-Width Navbar Section -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light w-100">
      <a class="navbar-brand" href="#">Dispatch Route</a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav me-auto">
          <li class="nav-item active">
            <a class="nav-link" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Email</a>
          </li>
        </ul>
      </div>
    </nav>

    <!-- Search Section -->
    <div class="section">
      <form class="d-flex" @submit.prevent="handleSearch">
        <input
          class="form-control me-2"
          type="search"
          placeholder="Search Requests"
          aria-label="Search"
          v-model="searchQuery"
        />
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>

      <!-- Display the search query -->
      <div class="mt-2">
        <p v-if="lastSearchQuery">You searched for: <strong>{{ lastSearchQuery }}</strong></p>
      </div>

      <!-- Error Message -->
      <div v-if="errorMessage" class="alert alert-danger mt-3">
        {{ errorMessage }}
      </div>

      <!-- Display search results -->
      <div class="mt-3">
        <h4 v-if="results.length > 0">Search Results:</h4>
        <ul v-if="results.length > 0">
          <li v-for="item in results" :key="item.request_id" class="mb-3">
            <strong>Request Description:</strong> {{ item.request_description }} <br />
            <strong>Service:</strong> {{ item.service.service_name }} <br />
            <strong>Team:</strong> {{ item.team.team_name }} (Expertise: {{ item.team.expertise_areas }}) <br />
            <strong>Status:</strong> {{ item.request_status }}
          </li>
        </ul>
        <p v-else-if="lastSearchQuery">No results found for "{{ lastSearchQuery }}"</p>
      </div>
    </div>

    <!-- Carousel Section -->
    <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="https://picsum.photos/1024/480/?image=52" class="d-block w-100" alt="First slide" />
        </div>
        <div class="carousel-item">
          <img src="https://picsum.photos/1024/480/?image=54" class="d-block w-100" alt="Second slide" />
        </div>
        <div class="carousel-item">
          <img src="https://picsum.photos/1024/480/?image=58" class="d-block w-100" alt="Third slide" />
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>

    <!-- Full-Width Footer Section -->
    <footer class="mt-4 bg-light text-center py-3 w-100">
      <p>© 2024 Hunduma Tesfaye. All Rights Reserved.</p>
    </footer>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  name: 'Home',
  setup() {
    const searchQuery = ref('');
    const lastSearchQuery = ref('');
    const results = ref([]);
    const errorMessage = ref('');

    const handleSearch = async () => {
      if (searchQuery.value) {
        lastSearchQuery.value = searchQuery.value;

        try {
          const response = await fetch(
            `http://127.0.0.1:8000/userrequests/search/?q=${encodeURIComponent(lastSearchQuery.value)}`
          );
          if (!response.ok) throw new Error('Network response was not ok');
          const data = await response.json();
          results.value = data;
          errorMessage.value = ''; // Clear any previous error message
        } catch (error) {
          console.error('Error fetching search results:', error);
          errorMessage.value = 'Error fetching search results. Please try again.';
        }

        searchQuery.value = '';
      }
    };

    return {
      searchQuery,
      lastSearchQuery,
      results,
      errorMessage,
      handleSearch,
    };
  },
};
</script>
