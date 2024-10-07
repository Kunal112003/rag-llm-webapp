import React from 'react';
import './Loading.css'; // Add CSS for styling

const Loading = () => {
  return (
    <div className="loading-container">
      <div className="spinner"></div>
      <p>Generating your recipe...</p>
    </div>
  );
};

export default Loading;
