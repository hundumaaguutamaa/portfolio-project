<template>
  <div class="login-container">
    <h2>Login</h2>
    <form @submit.prevent="loginUser" class="login-form">
      <div class="form-group">
        <label for="username">Username</label>
        <input
          type="text"
          v-model="username"
          class="form-control"
          id="username"
          placeholder="Enter username"
          aria-label="Username"
        />
      </div>

      <div class="form-group">
        <label for="password">Password</label>
        <input
          type="password"
          v-model="password"
          class="form-control"
          id="password"
          placeholder="Enter password"
          aria-label="Password"
        />
      </div>

      <button type="submit" class="btn btn-primary">Login</button>

      <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      errorMessage: ''
    };
  },
  methods: {
    async loginUser() {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/token/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            username: this.username,
            password: this.password
          })
        });
        const data = await response.json();

        if (response.ok) {
          localStorage.setItem('access_token', data.access);
          localStorage.setItem('refresh_token', data.refresh);
          this.$router.push('/home');
        } else {
          this.errorMessage = 'Invalid credentials';
        }
      } catch (error) {
        console.error('Error during login:', error);
        this.errorMessage = 'Login failed, please try again.';
      }
    }
  }
};
</script>

<style scoped>
.login-container {
  padding: 20px;
  max-width: 600px;
  margin: 100px auto 0; /* Add top margin to avoid overlap with fixed nav */
  text-align: center;
  background-color: #fff; /* Match the navigation bar background color */
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  font-family: 'Avenir', Helvetica, Arial, sans-serif; /* Match the navigation bar font */
}

.login-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

.form-control {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px; /* Match the navigation bar border radius */
  font-size: 16px;
  transition: border-color 0.3s;
  font-family: 'Avenir', Helvetica, Arial, sans-serif; /* Match the navigation bar font */
  color: #2c3e50; /* Match the navigation bar text color */
}

.form-control:focus {
  border-color: #42b983; /* Match the navigation bar active color */
}

.form-control::placeholder {
  color: #999;
}

.btn-primary {
  padding: 10px;
  background-color: #42b983; /* Match the navigation bar button color */
  color: white;
  border: none;
  border-radius: 4px; /* Match the navigation bar border radius */
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s;
  font-weight: bold; /* Match the navigation bar font weight */
}

.btn-primary:hover {
  background-color: #36a472; /* Match the navigation bar hover color */
}

.error-message {
  color: red;
  margin-top: 10px;
}
</style>
