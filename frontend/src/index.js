import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './app'; // Import the App component
import './main.css'; // Import your CSS
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap CSS

// This uses React 18’s `createRoot` API
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);


