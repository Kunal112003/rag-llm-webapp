import faiss # type: ignore
from sentence_transformers import SentenceTransformer

class FaissIndex:
    def __init__(self):
        self.model = SentenceTransformer('facebook/bart-large')
        self.index = faiss.IndexFlatL2(self.model.get_sentence_embedding_dimension())

    def add_documents(self, documents):
        embeddings = self.model.encode(documents)
        self.index.add(embeddings)

    def search(self, query, k=5):
        query_embedding = self.model.encode([query])
        D, I = self.index.search(query_embedding, k)
        return D[0], I[0]
    
# Now you can use FaissIndex to create an index and search for similar documents
# For example:
# index = FaissIndex()
# index.add_documents(["This is a document.", "This is another document."])
# distances, indices = index.search("This is a query.")
# print(distances)  # This will output the distances of the top k=5 results
# print(indices)  # This will output the indices of the top k=5 results
# You can then use the indices to retrieve the corresponding documents from your dataset
# For example:
# print("Top results:")
# for i in indices:
#     print(documents[i])
# This will output the top k=5 results from your dataset
#
# Note: Make sure to replace "documents" with your actual dataset of documents
# and adjust the k value as needed.
# Also, you can further customize the Faiss index by using different parameters or index types.
# For more information, refer to the Faiss documentation:
