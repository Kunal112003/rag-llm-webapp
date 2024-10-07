import {Navbar, Nav, Container} from 'react-bootstrap';
import React from 'react';
import './NavBar.css';


export const NavBarBootstrap = () => {
    // This is the navigation bar, and make it only visible on the top of the page with the links to the other pages
    return (
        <Navbar bg="dark" data-bs-theme="dark">
        <Container>
            <Navbar.Brand href="">CookBook</Navbar.Brand>
            <Nav className="me-auto">
                <Nav.Link href="/">Home</Nav.Link>
                <Nav.Link href="/recipe">Recipe</Nav.Link>
                <Nav.Link href="/chatbot">ChatBot</Nav.Link>
                <Nav.Link href="/cuisine">Cuisine</Nav.Link>         
          </Nav>
        </Container>
      </Navbar>
      
    );
}