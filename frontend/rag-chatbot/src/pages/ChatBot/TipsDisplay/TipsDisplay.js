import React from 'react';
import PropTypes from 'prop-types';
import './TipsDisplay.css';

const TipsDisplay = ({ tips, bestIngredients, commonMistakes }) => {
  return (
    <div className="tips-display">
      <h2>Cooking Tips</h2>
      <p>Here are some helpful tips for your cooking journey:</p>
      
      <h3>Tips:</h3>
      <ul>
        {Array.isArray(tips) && tips.length > 0 ? (
          tips.map((tip, index) => (
            <li key={index}>{tip}</li>
          ))
        ) : (
          <li>No tips available.</li>
        )}
      </ul>

      <h3>Best Ingredients:</h3>
      <ul>
        {Array.isArray(bestIngredients) && bestIngredients.length > 0 ? (
          bestIngredients.map((ingredient, index) => (
            <li key={index}>{ingredient}</li>
          ))
        ) : (
          <li>No best ingredients available.</li>
        )}
      </ul>

      <h3>Common Mistakes:</h3>
      <ul>
        {Array.isArray(commonMistakes) && commonMistakes.length > 0 ? (
          commonMistakes.map((mistake, index) => (
            <li key={index}>{mistake}</li>
          ))
        ) : (
          <li>No common mistakes available.</li>
        )}
      </ul>
    </div>
  );
};

TipsDisplay.propTypes = {
  tips: PropTypes.array.isRequired,
  bestIngredients: PropTypes.array,
  commonMistakes: PropTypes.array,
};

export default TipsDisplay;
