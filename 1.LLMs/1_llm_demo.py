from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile"
         ,temperature=0.7)

result= llm.invoke("What is the capital of India?")

print(result.content)



