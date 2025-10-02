from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",  
    task="text-generation",  # Still use text-generation here
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    temperature=0.7,
    max_new_tokens=200
)

model=ChatHuggingFace(llm=llm)


# 1 st prompt ---detailed report
template1= PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2 nd prompt  ---summary
template2= PromptTemplate(
    template='Write a five line summary report on {text}',
    input_variables=['text']
)

# prompt1=template1.invoke({
#     'topic': 'black hole'
# })

# result=model.invoke(prompt1)


# prompt2=template2.invoke({
#     'text': result.content
# })

#str output parser
parser= StrOutputParser()
chain = template1 | model | parser | template2 | model | parser

#result1=model.invoke(prompt2)

result = chain.invoke({
    'topic': 'black hole'
})

print(result)
