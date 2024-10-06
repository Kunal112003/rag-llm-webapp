from flask import Flask, request, jsonify
from models.rag_model import run_chatbot  # Import your chatbot logic from the models folder
import os

app = Flask(__name__)

# Path to the Langflow JSON file in the `data` folder
json_file_path = os.path.join(os.path.dirname(__file__), 'data', 'Recipe cookbook bot.json')

@app.route('/chatbot', methods=['POST'])

def chatbot():
    data = request.get_json()
    user_message = data.get("message")

    # Run the chatbot with the user's message, using the chatbot logic from the models folder
    response = run_chatbot(user_message, json_file_path)  # Pass the path to the JSON

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

# To run the Flask app, execute the following command in the terminal:
# python app.py
# This will start the Flask server on http://

    
    
    


