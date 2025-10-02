from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import _TypedDict,Annotated


load_dotenv()

model=ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.4
)

class Review(_TypedDict):
    summary: Annotated[str, "a brief summary of the review"]
    sentiment: Annotated[str, "Return the sentiment of the review either negative, positive or neutral"]

strucutred_output= model.with_structured_output(Review)


result=strucutred_output.invoke(""" The hardware is great , but the software feels bloated. There are too many pre-installed apps that I cannot remove. 
                    Also UI looks outdated compared to other brands. Hoping for a software update to fix this
                    """)

print(result)

# result is dictionary data type

print(result["summary"])

print(result["sentiment"])


