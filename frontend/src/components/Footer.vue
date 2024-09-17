<template>
    <footer class="footer">
      <p>© 2024 Hunduma Tesfaye</p>
    </footer>
  </template>
  
  <script>
  export default {
    name: 'Footer'
  }
  </script>
  
  <style scoped>
  .footer {
    position: fixed;
    width: 100%;
    left: 0;
    right: 0;
    bottom: 0;
    background: var(--footer-bg, linear-gradient(135deg, #05000a 0%, #555657 100%));
    padding: 10px;
    text-align: center;
    color: var(--footer-text-color, white);
    font-family: var(--footer-font, 'Arial', sans-serif);
    font-size: 14px;
    box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
  }
  
  .footer p {
    margin: 5px 0;
  }
  </style>
  