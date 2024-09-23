<template>
  <div class="login-container">
    <h2>Login</h2>
    <form @submit.prevent="loginUser" class="login-form">
      <input type="text" v-model="username" placeholder="Username" class="login-input" aria-label="Username" />
      <input type="password" v-model="password" placeholder="Password" class="login-input" aria-label="Password" />
      <button type="submit" class="login-button">Login</button>
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
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  font-family: 'Arial', sans-serif;
}

.login-form {
  display: flex;
  flex-direction: column;
}

.login-input {
  margin-bottom: 15px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 16px;
  transition: border-color 0.3s;
}

.login-input:focus {
  border-color: #007bff;
}

.login-input::placeholder {
  color: #999;
}

.login-button {
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.login-button:hover {
  background-color: #0056b3;
}

.error-message {
  color: red;
  margin-top: 10px;
}
</style>
