import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';
import './ChatBot.css';
import RecipeDisplay from './RecipeDisplay';
import TipsDisplay from './TipsDisplay/TipsDisplay';
import CuisineDisplay from './CuisineDisplay/CuisineDisplay';
import Loading from '../../components/Loading/Loading';

export const ChatBot = () => {
  const location = useLocation();
  const { selectedTopic } = location.state || {}; // Access selected topic from state

  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  const askAI = () => {
    const promptInput = document.getElementById("chat-input");
    const prompt = promptInput.value;

    if (prompt.trim() === "") {
      return; // Prevent empty messages
    }
    promptInput.value = "";

    const requestData = {
      query: prompt,
    };

    setLoading(true);
    let endpoint = "http://localhost:5000/recipe";

    if (selectedTopic === 'cooking-tips') {
      endpoint = "http://localhost:5000/cooking_tips";
    } else if (selectedTopic === 'cuisines') {
      endpoint = "http://localhost:5000/cuisine_info";
    }

    fetch(endpoint, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(requestData),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((resData) => {
        setData(resData || null);
        setLoading(false);
      })
      .catch((err) => {
        console.error(err);
        setLoading(false);
      });
  };

  // Check if selectedTopic is defined
  if (!selectedTopic) {
    return <p>Error: No topic selected!</p>;
  }

  return (
    <div className="chatbot">
      <div className="chatbot-container">
        <div className="chatbot-header">
          <div className="chatbot-header-title">{selectedTopic.replace("-", " ").toUpperCase()}</div>
        </div>
        <div className="chatbot-body">
          {loading ? (
            <Loading />
          ) : data ? (
            selectedTopic === 'cooking-tips' ? (
              <TipsDisplay tips={data.cooking_tips} />
            ) : selectedTopic === 'cuisines' ? (
              <CuisineDisplay cuisine={data.cuisine_info} />
            ) : (
              <RecipeDisplay recipe={data.recipe} />
            )
          ) : (
            <p>Ask me for a recipe, cooking tips, or cuisine info!</p>
          )}
        </div>
        <div className="chatbot-footer">
          <input id="chat-input" type="text" placeholder="Ask something..." />
          <button onClick={askAI} id="chat-submit" className="chatbot-send-button">
            Generate
          </button>
        </div>
        <button className="floating-button" onClick={() => setData(null)}>+</button>
      </div>
    </div>
  );
};
