from flask import Flask, request, jsonify
from models.rag_model import rag_pipeline  # Import your RAG logic

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    query = data['query']
    response = rag_pipeline(query)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)

