from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Initialize embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Your query
query = "What is the capital of India?"

# Your documents
documents = [
    "Delhi is the capital city of India.",
    "Mumbai is known as the financial capital of India.",
    "Paris is the capital of France.",
    "New Delhi is located in the northern part of India."
]

# Get query embedding (shape: [384])
query_embedding = embedding_model.embed_query(query)

# Get document embeddings (shape: [n_docs, 384])
doc_embeddings = embedding_model.embed_documents(documents)

# Compute cosine similarity
similarities = cosine_similarity([query_embedding], doc_embeddings)[0]

# Print results
for doc, score in zip(documents, similarities):
    print(f"Score: {score:.4f} | Doc: {doc}")
