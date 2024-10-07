import React, { useEffect, useState } from 'react';
import './RecipeDisplay.css'; // Ensure the styling matches your design
import axios from 'axios'; // Import axios for making requests

const RecipeDisplay = ({ recipe }) => {
  const [imageUrl, setImageUrl] = useState(''); // State to hold image URL

  useEffect(() => {
    // Function to fetch image based on the dish name
    const fetchImage = async () => {
      try {
        const response = await axios.get(
          `https://api.unsplash.com/search/photos?query=${recipe.dish_name}&client_id=aa_cNdt5UJrVxJXE6TckFeuN_1dQgvG_glKdAxZ4T7w`
        );

        // Check if there are any results
        if (response.data.results.length > 0) {
          setImageUrl(response.data.results[0].urls.regular); // Set the first image URL
        }
      } catch (error) {
        console.error('Error fetching the image:', error);
      }
    };

    fetchImage();
  }, [recipe.dish_name]); // Fetch new image when dish name changes

  return (
    <div className="recipe-display">
      <div className="recipe-header">
        <h2>{recipe.dish_name}</h2>
        <p className="recipe-info">
          <span><strong>Prep Time:</strong> {recipe.preparation_time}</span>
          <span><strong>Difficulty:</strong> {recipe.difficulty_level}</span>
        </p>
      </div>

      {imageUrl && <img src={imageUrl} alt={recipe.dish_name} className="recipe-image" />} {/* Display image */}

      <div className="recipe-section">
        <h3>Ingredients:</h3>
        <div className="ingredients-list">
          {recipe.ingredients.map((ingredient, index) => (
            <li key={index}>{ingredient}</li>
          ))}
        </div>
      </div>

      <div className="recipe-section">
        <h3>Instructions:</h3>
        <div className="instructions-list">
          {recipe.instructions.map((instruction, index) => (
            <div key={index} className="instruction-item">
              {instruction}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default RecipeDisplay;
