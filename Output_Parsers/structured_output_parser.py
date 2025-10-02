from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",  
    task="text-generation",  # Still use text-generation here
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    temperature=0.7,
    max_new_tokens=200
)

model=ChatHuggingFace(llm=llm)

schema=[
    ResponseSchema(name="fact_1", description='Fact1 about the topic'),
    ResponseSchema(name="fact_2", description='Fact2 about the topic'),
    ResponseSchema(name="fact_3", description='Fact3 about the topic')

]



parser= StructuredOutputParser.from_response_schemas(schema)

template=PromptTemplate(
    template='Give 3 facts about the {topic}\n{format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)


chain= template | model | parser
result= chain.invoke({'topic': 'black hole'})

print(result)
