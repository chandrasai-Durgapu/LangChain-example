from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",  
    task="text-generation",  # Still use text-generation here
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    temperature=0.7,
    max_new_tokens=200
)

model=ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name: str=Field(description="name of the person")
    age: int=Field(gt=18, description="age should be greater than 18")
    city: str=Field(description="name of the city")

parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# prompt= template.invoke({'place': 'indian'})
# result= model.invoke(prompt)
# final_result=parser.parse(result.content)

chain=template|model|parser
final_result=chain.invoke({'place':'indian'})
print(final_result)