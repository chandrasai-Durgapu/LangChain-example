from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

documents = "Delhi is the capital of India"

result = embedding.embed_documents(documents)
print(result)  # List of 384 floats
