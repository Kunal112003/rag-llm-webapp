import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./Home.css";

const slidesData = [
    { id: 1, title: "Recipes", description: "Find delicious recipes", link: "/chatbot?topic=recipes" },
    { id: 2, title: "Cuisines", description: "Explore different cuisines", link: "/chatbot?topic=cuisines" },
    { id: 3, title: "Uploading Recipes", description: "Upload your own recipes", link: "/chatbot?topic=upload-recipes" },
    { id: 4, title: "Cooking Tips", description: "Get helpful cooking tips", link: "/chatbot?topic=cooking-tips" },
    { id: 5, title: "Nutrition", description: "Learn about nutrition", link: "/chatbot?topic=nutrition" },
    { id: 6, title: "Meal Plans", description: "Get personalized meal plans", link: "/chatbot?topic=meal-plans" }
];

export const Home = () => {
    const navigate = useNavigate();
    const [slides, setSlides] = useState([]);

    useEffect(() => {
        setSlides(slidesData);
    }, []);

    const handleSlideClick = (link) => {
        // Extracting the topic from the link
        const topic = link.split('=')[1]; // This assumes the link format is "/chatbot?topic={topic}"
        // Navigating to the ChatBot page with the selected topic
        navigate(link, { state: { selectedTopic: topic } });
    };

    return (
        <div className="home">
            <h1>Welcome to the CookBook</h1>
            <div className="slides">
                {slides.length > 0 ? (
                    slides.map(slide => (
                        <div 
                            key={slide.id} 
                            className="slide" 
                            onClick={() => handleSlideClick(slide.link)}
                        >
                            <h2>{slide.title}</h2>
                            <p>{slide.description}</p>
                        </div>
                    ))
                ) : (
                    <p>No slides available.</p>
                )}
            </div>
        </div>
    );
};

export default Home;
