<template>
    <div>
      <h2>Sign Up</h2>
      <form @submit.prevent="signupUser">
        <input type="text" v-model="username" placeholder="Username" />
        <input type="password" v-model="password" placeholder="Password" />
        <input type="email" v-model="email" placeholder="Email" />
        <button type="submit">Sign Up</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        password: '',
        email: ''
      };
    },
    methods: {
      async signupUser() {
        const response = await fetch('http://127.0.0.1:8000/signup/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            username: this.username,
            password: this.password,
            email: this.email
          })
        });
        if (response.ok) {
          this.$router.push('/login');
        } else {
          alert('Error creating account');
        }
      }
    }
  };
  </script>
  