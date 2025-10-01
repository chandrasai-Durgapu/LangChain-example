from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model=ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3
)

result = model.invoke("What is the capital of India")

print(result.content)