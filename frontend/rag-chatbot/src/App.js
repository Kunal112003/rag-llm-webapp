import React, { useState } from 'react';

function App() {
    const [userMessage, setUserMessage] = useState('');
    const [chatbotResponse, setChatbotResponse] = useState('');
    const [chatHistory, setChatHistory] = useState([]);

    // Function to send the user message to the backend
    const sendMessageToChatbot = async () => {
        try {
            const response = await fetch('http://localhost:5000/chatbot', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: userMessage }),
            });

            const data = await response.json();
            const responseMessage = data.response;

            // Update the chat history with both the user message and chatbot response
            setChatHistory([
                ...chatHistory,
                { sender: 'User', text: userMessage },
                { sender: 'Chatbot', text: responseMessage },
            ]);

            // Clear the input field and update the chatbot's response
            setUserMessage('');
            setChatbotResponse(responseMessage);

        } catch (error) {
            console.error('Error:', error);
        }
    };

    // Handle form submission
    const handleSubmit = (e) => {
        e.preventDefault();
        sendMessageToChatbot();
    };

    return (
        <div>
            <h1>Chat with AI</h1>
            <div className="chatbox">
                {chatHistory.map((entry, index) => (
                    <div key={index} className={`message ${entry.sender}`}>
                        <strong>{entry.sender}:</strong> {entry.text}
                    </div>
                ))}
            </div>

            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={userMessage}
                    onChange={(e) => setUserMessage(e.target.value)}
                    placeholder="Type your message..."
                />
                <button type="submit">Send</button>
            </form>

            {chatbotResponse && (
                <div className="chatbot-response">
                    <h3>Response from Chatbot:</h3>
                    <p>{chatbotResponse}</p>
                </div>
            )}
        </div>
    );
}

export default App;
