<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light shadow-sm">
    <div class="container-fluid">
      <!-- Logo/Brand -->
      <a class="navbar-brand" href="#">DispatchRoute</a>
      
      <!-- Toggler for mobile view -->
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      
      <!-- Navbar content -->
      <div class="collapse navbar-collapse justify-content-center" id="navbarNavDropdown">
        <!-- Centered Navbar tabs -->
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Pricing</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Features</a>
          </li>
        </ul>
      </div>

      <!-- Search form aligned to the right -->
      <form class="d-flex ms-auto">
        <input class="form-control me-2 rounded-pill" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-primary rounded-pill" type="submit">Search</button>
      </form>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
}
</script>

<style scoped>
a {
  color: #000;
}

.navbar-nav .nav-link {
  font-size: 16px;
  padding-left: 20px;
  padding-right: 20px;
}

.navbar {
  font-family: 'Arial', sans-serif;
}
</style>
