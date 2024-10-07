import React, { useState } from 'react';
import { useLocation } from 'react-router-dom'; // Import useLocation
import './ChatBot.css';
import RecipeDisplay from './RecipeDisplay'; // New component for displaying recipe
import Loading from '../../components/Loading/Loading'; // Import the Loading component

export const ChatBot = () => {
  const location = useLocation(); // Get the current location
  const queryParams = new URLSearchParams(location.search); // Parse the query parameters
  const topic = queryParams.get('topic'); // Get the topic parameter

  const [recipe, setRecipe] = useState(null); // State to hold recipe data
  const [loading, setLoading] = useState(false); // Loading state for progress display

  function askAI() {
    const prompt_input = document.getElementById("chat-input");
    const prompt = prompt_input.value;

    if (prompt.trim() === "") {
      return; // Prevent empty messages
    }
    prompt_input.value = "";

    const data = {
      query: prompt,
    };

    setLoading(true); // Start loading

    // Determine the endpoint based on the topic
    let endpoint;
    switch (topic) {
      case 'recipes':
        endpoint = 'http://localhost:5000/recipe';
        break;
      case 'cuisines':
        endpoint = 'http://localhost:5000//cuisine_info';
        break;
      case 'upload-recipes':
        endpoint = 'http://localhost:5000/upload-recipe';
        break;
      case 'cooking-tips':
        endpoint = 'http://localhost:5000/cooking_tips';
        break;
      case 'nutrition':
        endpoint = 'http://localhost:5000/nutrition';
        break;
      case 'meal-plans':
        endpoint = 'http://localhost:5000/meal-plans';
        break;
      default:
        endpoint = 'http://localhost:5000/recipe'; // Fallback endpoint
    }

    fetch(endpoint, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((resData) => {
        setRecipe(resData.recipe || null); // Set the received recipe
        setLoading(false); // End loading
      })
      .catch((err) => {
        console.error(err);
        setLoading(false); // Ensure loading stops even if there's an error
      });
  }

  return (
    <div className="chatbot">
      <div className="chatbot-container">
        <div className="chatbot-header">
          <div className="chatbot-header-title">AI-Powered Kitchen Companion</div>
        </div>
        <div className="chatbot-body">
          {loading ? (
            <Loading /> // Use the Loading component for the loading state
          ) : recipe ? (
            <RecipeDisplay recipe={recipe} /> // Show recipe in a structured way
          ) : (
            <p>Ask me for a recipe and I will guide you step-by-step!</p>
          )}
        </div>
        <div className="chatbot-footer">
          <input id="chat-input" type="text" placeholder="Ask for a recipe..." />
          <button onClick={askAI} id="chat-submit" className="chatbot-send-button">
            Generate Recipe
          </button>
        </div>
        <button className="floating-button" onClick={() => setRecipe(null)}>+</button> {/* Floating button */}
      </div>
    </div>
  );
};
