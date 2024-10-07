# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import os
# import json
# from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
# from llama_index.core import StorageContext, load_index_from_storage
# from llama_index.core.chat_engine import CondenseQuestionChatEngine
# from llama_index.core.prompts import Prompt
# from llama_index.core.llms import MessageRole, ChatMessage




# os.environ['OPEN_AI_API_KEY']=  "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"

# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# def create_llama_index():

#     try:
#         index_dir = 'index'  # Create a folder named 'llama_index' in the same directory as this script
#         os.makedirs(index_dir, exist_ok=True)

#         # from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
#         documents = SimpleDirectoryReader('uploads').load_data()
#         index = VectorStoreIndex.from_documents(documents)
#         index.storage_context.persist(persist_dir=index_dir)
#         if not os.path.exists(index_dir) or not os.listdir(index_dir):
#             return jsonify({'error': 'Index not created'})
#         return jsonify({'message': 'Index created'})
#     except Exception as e:
#         return jsonify({'error': str(e)})


# def get_custom_prompt():
#     try:
        
#         return Prompt("""\
# Rephrase the conversation and subsequent message into 
# a self-contained question while including all relevant details. 
# Conclude the question with: Only refer to this document.

# <Chat History> 
# {chat_history}

# <Follow Up Message>
# {question}

# <Standalone question>
# """)
#     except Exception as e:
#         # If an error occurs during the try block, catch it here
#         return jsonify({'error':  f"An error occurred: {e}"})

# # creates chat history


# def getChatHistory(history='[]'):
#     try:
        
#         history = json.loads(history)

#         # initialize chart history
#         custom_chat_history = []
#         roles = {"left_bubble": "ASSISTANT", "right_bubble": "USER"}
#         for chat in history:
#             position = chat['position']
#             role = MessageRole[roles[position]]
#             content = chat['message']
#             custom_chat_history.append(
#                 ChatMessage(
#                     # can be USER or ASSISTANT
#                     role=role,
#                     content=content
#                 )
#             )
#         return custom_chat_history
#     except Exception as e:
#         # If an error occurs during the try block, catch it here
#         return jsonify({'error':  f"An error occurred: {e}"})


# def query_index():
#     # retrive open ai key
#     open_ai_key = os.getenv('OPEN_AI_API_KEY')
#     print("test")
#     try:
        

#         index_dir = 'index'

#         if not os.path.exists(index_dir) or not os.listdir(index_dir):
#             return jsonify({'error':  f"Index directory '{index_dir}' does not exist or is empty."})
#         data = request.get_json()
#         prompt = data.get('prompt')
#         chatHistory = data.get('chatHistory')
#         print(prompt)
#         storage_context = StorageContext.from_defaults(persist_dir=index_dir)
#         index = load_index_from_storage(storage_context)
#         query_engine = index.as_query_engine()
#         chat_engine = CondenseQuestionChatEngine.from_defaults(
#             query_engine=query_engine,
#             condense_question_prompt=get_custom_prompt(),
#             chat_history=getChatHistory(chatHistory),
#             verbose=True
#         )

#         response_node = chat_engine.chat(prompt)  # chat here
#         #print the response in the console
#         print(response_node.response)
#         return jsonify({'result':  response_node.response})

#     except Exception as e:
#         return jsonify({'error':  f"An error occurred: {e}"})


# @app.route('/')
# def hello_world():
#     return jsonify({'result':  "Hello world"})


# @app.route('/ask_ai', methods=['POST'])
# def query_endpoint():
#     response = query_index()
#     return response

 

# @app.route('/upload_file', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'})
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'})
    
#     if file:
#         upload_dir = 'uploads'  # Create a folder named 'uploads' in the same directory as this script
#         os.makedirs(upload_dir, exist_ok=True)
#         file.save(os.path.join(upload_dir, file.filename))
        
#         return create_llama_index()
    
#     return jsonify({'error': 'An error occurred'})






# if __name__ == '__main__':
#     app.run()