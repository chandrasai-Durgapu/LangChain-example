from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

chat_template=ChatPromptTemplate([
    ('system','you are helpful {domain} expert'),
    ('human','Explain in simple terms, what is {topic}')
   
    # [
    #     SystemMessage(content='you are helpful {doamin} export'),
    #     HumanMessage(content='Explain in simple terms, what is {topic}')
    # ]
                                ]
                                )
# create dynamic set of messages
prompt=chat_template.invoke({
    'domain':'cricket','topic':'googly'
                            })

print(prompt)