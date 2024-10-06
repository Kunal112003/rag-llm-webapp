from langflow.load import run_flow_from_json

TWEAKS = {
  "TextInput-mbn0J": {
    "input_value": "jeoy"
  },
  "ChatInput-0P0qd": {
    "files": "",
    "input_value": "hey have i asked you anything yet?",
    "sender": "User",
    "sender_name": "",
    "session_id": "",
    "should_store_message": True
  },
  "Prompt-p5RB1": {
    "template": "Hey, answer the user's question based on the following context:\nThe context is this: {context}\nAnd this is the message History: {history}\nThe users question is this: {question}",
    "context": "",
    "history": "",
    "question": ""
  },
  "ChatOutput-pC82L": {
    "data_template": "{text}",
    "input_value": "",
    "sender": "Machine",
    "sender_name": "AI",
    "session_id": "",
    "should_store_message": True
  },
  "Memory-oNU9a": {
    "n_messages": 100,
    "order": "Ascending",
    "sender": "Machine and User",
    "sender_name": "",
    "session_id": "",
    "template": "{sender_name}: {text}"
  },
  "OpenAIModel-cQNAX": {
    "api_key": "OPENAI_API_KEY",
    "input_value": "",
    "json_mode": False,
    "max_tokens": None,
    "model_kwargs": {},
    "model_name": "gpt-4o-mini",
    "openai_api_base": "",
    "output_schema": {},
    "seed": 1,
    "stream": False,
    "system_message": "",
    "temperature": 0.1
  },
  "AstraDB-AUbaG": {
    "api_endpoint": "endpoint",
    "batch_size": None,
    "bulk_delete_concurrency": None,
    "bulk_insert_batch_concurrency": None,
    "bulk_insert_overwrite_concurrency": None,
    "collection_indexing_policy": "",
    "collection_name": "collection",
    "metadata_indexing_exclude": "",
    "metadata_indexing_include": "",
    "metric": "",
    "namespace": "",
    "number_of_results": 4,
    "pre_delete_collection": False,
    "search_filter": {},
    "search_input": "",
    "search_score_threshold": 0,
    "search_type": "Similarity",
    "setup_mode": "Sync",
    "token": "AstraDB_token"
  },
  "OpenAIEmbeddings-6kvti": {
    "chunk_size": 1000,
    "client": "",
    "default_headers": {},
    "default_query": {},
    "deployment": "",
    "dimensions": None,
    "embedding_ctx_length": 1536,
    "max_retries": 3,
    "model": "text-embedding-3-small",
    "model_kwargs": {},
    "openai_api_base": "",
    "openai_api_key": "new key",
    "openai_api_type": "",
    "openai_api_version": "",
    "openai_organization": "",
    "openai_proxy": "",
    "request_timeout": None,
    "show_progress_bar": False,
    "skip_empty": False,
    "tiktoken_enable": True,
    "tiktoken_model_name": ""
  },
  "File-sxZ3N": {
    "path": "cookbook.pdf",
    "silent_errors": False
  },
  "SplitText-n4xat": {
    "chunk_overlap": 200,
    "chunk_size": 1000,
    "separator": "\n"
  },
  "ParseData-uG09c": {
    "sep": "\n",
    "template": "{text}"
  }
}

# result = run_flow_from_json(flow="Recipe cookbook bot.json",
#                             input_value="message",
#                             fallback_to_env_vars=True, # False by default
#                             tweaks=TWEAKS)

# print(result)

def run_chatbot(input_message):
    # Modify the tweaks or input_value dynamically based on the incoming message
    TWEAKS["ChatInput-0P0qd"]["input_value"] = input_message

    # Run the flow with your tweaks and return the result
    result = run_flow_from_json(
        flow="data/Recipe cookbook bot.json",  # Path to your Langflow JSON
        input_value=input_message,
        fallback_to_env_vars=True,
        tweaks=TWEAKS
    )
    
    return result

# print(run_chatbot("hey have i asked you anything yet?"))
