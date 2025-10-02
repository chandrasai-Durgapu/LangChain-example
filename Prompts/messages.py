from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model=ChatGroq(model="llama-3.3-70b-versatile"
         ,temperature=0.7)

# System Message----> the work should be done by the llm(Groq llm) ....example;-- "llm act as an Doctor Assistant"

#Human Message---> user input

#AI Message----> output given by the llm

messages=[
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about Langchain")
]

result=model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)

