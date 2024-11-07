import React from 'react';
import './CuisineDisplay.css';

const CuisineDisplay = ({ cuisine }) => {
  return (
    <div className="cuisine-display">
      <h2>{cuisine.cuisine_name}</h2>
      <p>{cuisine.description}</p>
      <h3>Popular Dishes:</h3>
      <ul>
        {cuisine.popular_dishes.map((dish, index) => (
          <li key={index}>{dish}</li>
        ))}
      </ul>
      <h3>Cooking Techniques:</h3>
      <ul>
        {cuisine.cooking_techniques.map((technique, index) => (
          <li key={index}>{technique}</li>
        ))}
      </ul>
    </div>
  );
};

export default CuisineDisplay;
