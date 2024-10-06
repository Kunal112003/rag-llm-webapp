import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import {NavBarBootstrap} from './components/NavBar/navbarBS';
// import {NavBar} from './components/NavBar/navbar';
import {Home} from './pages/Home/Home';
import {Recipe} from './pages/Recipe/Recipe';
import {ChatBot} from './pages/ChatBot/ChatBot';
import {Cuisine} from './pages/Cuisine/Cuisine';

function App() {
  return (
    <Router>
      <NavBarBootstrap />
      <Routes>
        <Route path="/" exact component={Home} />
        <Route path="/recipe" component={Recipe} />
        <Route path="/chatbot" component={ChatBot} />
        <Route path="/cuisine" component={Cuisine} />
      </Routes>
        
    </Router>
  );
}

export default App;



