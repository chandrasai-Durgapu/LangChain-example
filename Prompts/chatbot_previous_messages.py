from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from dotenv import load_dotenv

load_dotenv()

model=ChatGroq(model="llama-3.3-70b-versatile"
         ,temperature=0.7)

# to maintain chat history ....consider a list and append all messages in that list
chat_history=[
    SystemMessage(content="You are a helpful AI assistant")
]

while True:
    user_input=input("You: please give your input:")
    chat_history.append(HumanMessage(content=user_input))

    if user_input=='exit':
        break
    else:
        # result= model.invoke(user_input) # display output without chat_history
        result= model.invoke(chat_history)
        chat_history.append(AIMessage(content=result.content))
        print("AI output:",chat_history)

