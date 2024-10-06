import {Navbar, Nav, Container} from 'react-bootstrap';

export const NavBarBootstrap = () => {
    return (
        <Navbar bg="dark" data-bs-theme="dark">
        <Container>
          <Navbar.Brand href="">CookBook</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link href="#home">Home</Nav.Link>
            <Nav.Link href="#recipe">Recipe</Nav.Link>
            <Nav.Link href="#cuisine">Cuisine</Nav.Link>
            <Nav.Link href="#chatbot">Chatbot</Nav.Link>
          </Nav>
        </Container>
      </Navbar>
      
    );
}