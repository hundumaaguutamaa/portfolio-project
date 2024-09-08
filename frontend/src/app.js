import React, { useState } from 'react';
import './main.css';

function App() {
  const [search, setSearch] = useState('');
  const [suggestion, setSuggestion] = useState('');

  // Handle input change and set search suggestion
  const handleSearchChange = (e) => {
    setSearch(e.target.value);
    setSuggestion(`Searching for: ${e.target.value}`);
  };

  return (
    <div className="container">
      <h1>Route Service Desk</h1>

      <input
        type="text"
        className="search-bar"
        placeholder="Search Team product"
        value={search}
        onChange={handleSearchChange}
      />

      {suggestion && <p className="search-suggestion">{suggestion}</p>}

      <button className="button">Search</button>

      <div className="locations">
        <img
          src="https://images.unsplash.com/photo-1479920252409-6e3d8e8d4866?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
          alt="Location 1"
          className="location-image"
        />
        <img
          src="https://images.unsplash.com/photo-1471897488648-5eae4ac6686b?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
          alt="Location 2"
          className="location-image"
        />
        <img
          src="https://images.pexels.com/photos/18471478/pexels-photo-18471478/free-photo-of-a-row-of-computers-with-monitors-on-them.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
          alt="Location 3"
          className="location-image"
        />
      </div>

      {/* Add the footer directly here */}
      <footer className="py-5 my-5 bg-dark">
        <div className="container px-4 px-lg-5">
          <p className="text-center text-white">Copyright @ Dispatch Route 2024</p>
        </div>
      </footer>
    </div>
  );
}
export default App;
