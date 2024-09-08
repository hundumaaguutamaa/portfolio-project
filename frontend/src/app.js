import React, { useState } from 'react';
import { Button, Container, InputGroup, FormControl, Row, Col, Navbar, Nav } from 'react-bootstrap';
import axios from 'axios'; // Import axios for API requests
import './main.css';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  const [search, setSearch] = useState('');
  const [suggestion, setSuggestion] = useState('');
  const [results, setResults] = useState([]);

  // Handle input change and set search suggestion
  const handleSearchChange = (e) => {
    setSearch(e.target.value);
    setSuggestion(`Searching for: ${e.target.value}`);
  };

  // Handle search button click
  const handleSearchClick = () => {
    axios.get(`/api/search/?q=${search}`)
      .then(response => {
        setResults(response.data);
      })
      .catch(error => {
        console.error('Error fetching search results:', error);
      });
  };

  return (
    <div>
      <Navbar bg="dark" variant="dark" expand="lg">
        <Navbar.Brand href="#home">Dispatch Route</Navbar.Brand>
        <Navbar.Collapse className="justify-content-center">
          <Nav>
            <Nav.Link href="#home">Home</Nav.Link>
            <Nav.Link href="#features">Features</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Navbar>

      <Container fluid className="my-4">
        <h1>Search and Dispatch</h1>

        <InputGroup className="mb-3">
          <FormControl
            type="text"
            placeholder="Search Team product"
            value={search}
            onChange={handleSearchChange}
          />
          <Button variant="primary" onClick={handleSearchClick}>Search</Button>
        </InputGroup>

        {suggestion && <p className="search-suggestion">{suggestion}</p>}

        <Row className="locations">
          {results.map(result => (
            <Col md={4} className="mb-3" key={result.id}>
              <img
                src={result.image_url} // Assuming your results have image URLs
                alt={result.name}
                className="location-image img-fluid"
              />
            </Col>
          ))}
        </Row>

        <footer className="py-3 my-3 bg-dark bottom-0 text-white text-center">
          <div className="container">
            <p>Copyright @ Dispatch Route 2024</p>
          </div>
        </footer>
      </Container>
    </div>
  );
}

export default App;
