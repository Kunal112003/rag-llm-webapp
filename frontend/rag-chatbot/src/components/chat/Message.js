import React from "react";

function Message(props) {
  // Determine the role based on position
  let dataRoll = props.position === "left_bubble" ? "ASSISTANT" : "USER";

  // Define the class for the chat bubble
  let thisClass = `chat-bubble ${props.position}`;

  // Ensure props.message is a string
  const messageText = typeof props.message === 'string' 
    ? props.message.replace(/<\/?[^>]+(>|$)/g, "") 
    : "Invalid message content"; // Fallback if message is not a string

  return (
    <div data-role={dataRoll} className="bubble-container">
      <div className={thisClass}>
        <div className="text_message">
          {messageText}
        </div>
      </div>
      <div className="clear"></div>
    </div>
  );
}

export default Message;
