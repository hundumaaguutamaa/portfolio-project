<template>
  <div class="overlay" v-if="isVisible">
    <div class="login-form">
      <h2>Login</h2>
      <form @submit.prevent="loginUser">
        <input type="text" v-model="username" placeholder="Username" />
        <input type="password" v-model="password" placeholder="Password" />
        <button type="submit">Login</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  props: ['isVisible'],
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    async loginUser() {
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
        this.$emit('login-success'); // Emit event to parent
      } else {
        alert('Invalid credentials');
      }
    }
  }
};
</script>

<style scoped>
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
}

.login-form {
  background: white;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
}
</style>
