# LangChain-example
LangChain-example

## Create virtual environment
```bash
python -m venv Langchain-example
```

## Activate virtual environment
```bash
Langchain-example/Scripts/Activate
```

## Install Dependencies
```bash 
pip install -r requirements.txt
```
---
## Set the API key in your environment:
```bash
export GROQ_API_KEY="your_api_key_here"
```
---
run the code
```bash
python 1.LLMs/1_llm_demo.py
```
---
run the code
```bash
python 2.ChatModels/1_chatmodel_groq.py
```

run the hugging face api model
```bash
python 2.ChatModels/2_chatmodel_hf_api.py
```
---
run the hugging face embeddings query locally
```bash
python 3.EmbeddedModels/1_embedding_huggingface.py
```

run the hugging face embeddings document
```bash
python 3.EmbeddedModels/2_huggingface_document.py
```

run the hugging face emdeggings and perform document cosine similarity 
```bash
python 3.EmbeddedModels/3_document_similarity.py
```
---
run the prompt
```bash
python Prompts/prompt.py
```

run the prompt
```bash
python Prompts/prompt_generator.py
```

run the chatbot
```bash
python Prompts/chatbot.py
```

run the messages with previous history
```bash
python Prompts/messages.py
```

run the chatbot with previous chat history and previous chat messages
```bash
python Prompts/chatbot_previous_messages.py
```

run the chat prompt template (dynamic template & multiple messages)
```bash
python Prompts/chat_prompt_template.py
```

run the messages with place holder(save the previous chat history)
```bash
python Prompts/message_placeholder.py
```
---

run the structured output with typed dict
```bash
python Structured_Output/typed_dict.py
```

run the annotated typed dict with structured output
```bash
python Structured_Output/annotated_typedict.py
```

run the pydantic (pydantic====data validation)
```bash
python Structured_Output/pydantic_demo.py
```

run the pydantic with structured output
```bash
python Structured_Output/pydantic_structured_output.py
```

run pydantic with json schema
```bash
python Structured_Output/pydantic_json.py
```
---

run the str output parser with hugging face llm
```bash
python Output_Parsers/str_output_parser.py
```



