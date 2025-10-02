from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()



# 1. Create the LLM (Groq-hosted model, e.g., Mixtral)
llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",  
    temperature=0.7
)


# Step 2: Create a prompt template
prompt_template = PromptTemplate(
    input_variables=["topic"],
    template="Explain the concept of {topic} in simple terms."
)

# Step 3: Format the prompt manually
formatted_prompt = prompt_template.format(topic="quantum entanglement")

# Step 4: Send the formatted prompt to the model
result = llm.invoke(formatted_prompt)

# Step 5: Print the response
print(result.content)  # response is a ChatMessage object

