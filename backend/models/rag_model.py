from sentence_transformers import SentenceTransformer
from transformers import RagTokenizer, RagRetriever, RagTokenForGeneration

class RagModel:
    def __init__(self):
        self.model = SentenceTransformer('facebook/bart-large')
        self.tokenizer = RagTokenizer.from_pretrained('facebook/rag-token-nq')
        self.retriever = RagRetriever.from_pretrained('facebook/rag-token-nq', index_name='exact', use_dummy_dataset=True)
        self.generator = RagTokenForGeneration.from_pretrained('facebook/rag-token-nq')

    def get_response(self, question):
        input_ids = self.tokenizer(question, return_tensors='pt').input_ids
        retriever_results = self.retriever(input_ids)
        generator_input = {'retrieved_doc_embeds': retriever_results['retrieved_doc_embeds'], 'retrieved_doc_ids': retriever_results['doc_ids'], 'question_encoder_input_ids': input_ids}
        outputs = self.generator.generate(**generator_input)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
    

rag_pipeline = RagModel()

# Now you can use rag_pipeline.get_response(question) to get a response to a question
# For example:
# response = rag_pipeline.get_response("What is the capital of France?")
# print(response)
# This will output "Paris"


