import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import {NavBarBootstrap} from './components/NavBar/navbarBS';
// import {NavBar} from './components/NavBar/navbar';
import {Home} from './pages/Home/Home';
import {Recipe} from './pages/Recipe/Recipe';
import {ChatBot} from './pages/ChatBot/ChatBot';
import {Cuisine} from './pages/Cuisine/Cuisine';

import './App.css';

function App() {
  return (
    <Router>
      <NavBarBootstrap />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/recipe" element={<Recipe />} />
        <Route path="/chatbot" element={<ChatBot />} />
        <Route path="/cuisine" element={<Cuisine />} />
      </Routes>
        
    </Router>
  );
}

export default App;



