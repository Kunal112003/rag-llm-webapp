# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from cuisinebot.agent import CuisineAgent

app = Flask(__name__)
CORS(app)

@app.route("/recipe", methods=['POST'])
def get_recipe():
    data = request.json
    user_query = data.get("query")

    if not user_query:
        return jsonify({"error": "Missing query"}), 400

    agent = CuisineAgent(query=user_query)
    try:
        recipe = agent.get_recipe()
        return jsonify({"recipe": recipe})
    except Exception as e:
        print("Error getting recipe:", str(e))
        return jsonify({"error": "Failed to get recipe."}), 500


@app.route("/cuisine_info", methods=['POST'])
def get_cuisine_info():
    data = request.json
    user_query = data.get("query")

    if not user_query:
        return jsonify({"error": "Missing query"}), 400

    agent = CuisineAgent(query=user_query)
    info = agent.get_cuisine_info()

    return jsonify({"cuisine_info": info.dict()})


@app.route("/cooking_tips", methods=['POST'])
def get_cooking_tips():
    data = request.json
    user_query = data.get("query")

    if not user_query:
        return jsonify({"error": "Missing query"}), 400

    agent = CuisineAgent(query=user_query)
    tips = agent.get_tips()

    return jsonify({"cooking_tips": tips.dict()})

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
