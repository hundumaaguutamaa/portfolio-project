import React, { useState } from 'react';
import { Button, Container, InputGroup, FormControl, Row, Col, Navbar, Nav } from 'react-bootstrap';
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
    <div>
      <Navbar bg="dark" variant="dark" expand="lg">
        <Navbar.Brand href="#home">Dispatch Route</Navbar.Brand>
        <Nav className="mr-auto">
          <Nav.Link href="#home">Home</Nav.Link>
          <Nav.Link href="#features">Features</Nav.Link>
        </Nav>
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
          <InputGroup.Append>
            <Button variant="primary">Search</Button>
          </InputGroup.Append>
        </InputGroup>

        {suggestion && <p className="search-suggestion">{suggestion}</p>}

        <Row className="locations">
          <Col md={4} className="mb-3">
            <img
              src="https://images.unsplash.com/photo-1479920252409-6e3d8e8d4866?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
              alt="Location 1"
              className="location-image img-fluid"
            />
          </Col>
          <Col md={4} className="mb-3">
            <img
              src="https://images.unsplash.com/photo-1471897488648-5eae4ac6686b?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
              alt="Location 2"
              className="location-image img-fluid"
            />
          </Col>
          <Col md={4} className="mb-3">
            <img
              src="https://images.pexels.com/photos/18471478/pexels-photo-18471478/free-photo-of-a-row-of-computers-with-monitors-on-them.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
              alt="Location 3"
              className="location-image img-fluid"
            />
          </Col>
        </Row>

        <footer className="py-5 my-5 bg-dark text-white text-center">
          <div className="container">
            <p>Copyright @ Dispatch Route 2024</p>
          </div>
        </footer>
      </Container>
    </div>
  );
}

export default App;
