# LangChain-example
# 🦜 LangChain Example

This repository demonstrates how to use [LangChain](https://github.com/langchain-ai/langchain) with different models, prompt strategies, embeddings, and structured output handling. It provides modular examples for learning or building production-ready LLM apps.

---
## 🧰 Tech Stack

This project uses the following technologies and tools:

- **Python 3.8+**  
  Core programming language used for scripting and automation.

- **LangChain**  
  Framework for building applications powered by language models. Handles prompts, chains, memory, and more.

- **OpenAI / GROQ / Hugging Face APIs**  
  Supports multiple LLM providers for chat, completion, and embeddings.

- **Pydantic & TypedDict**  
  For defining and parsing structured outputs returned by LLMs.

- **python-dotenv**  
  Loads environment variables securely from a `.env` file.

- **FAISS** *(optional)*  
  A library for efficient similarity search and clustering of dense vectors (used in embedding examples).

---

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

## ✅ 1.LLMs/1_llm_demo.py

🎯 Purpose: Basic LLM prompt-response demo.

📝 Description: Sends a static text prompt to a large language model and receives a completion. Good starting point to test connection with the LLM provider and observe model behavior on simple inputs.

...run the code
```bash
python 1.LLMs/1_llm_demo.py
```

---

## ✅ 2.ChatModels/1_chatmodel_groq.py

🎯 Purpose: Chat interface using Groq LLM API.

📝 Description: Demonstrates how to interact with the Groq LLM using conversational format (user ↔ assistant messages). Useful for testing dialogue-based tasks with Groq’s API.

...🔧 run command for the code
```bash
python 2.ChatModels/1_chatmodel_groq.py
```

---

## ✅ 2.ChatModels/2_chatmodel_hf_api.py

🎯 Purpose: Chat interface using Hugging Face-hosted model.

📝 Description: Connects to a Hugging Face Inference API model to simulate chat. Helps compare open-source hosted models for dialogue applications.

...🔧 run command for the hugging face api model
```bash
python 2.ChatModels/2_chatmodel_hf_api.py
```

---

## ✅ 3.EmbeddedModels/1_embedding_huggingface.py

🎯 Purpose: Generate text embeddings via Hugging Face model.

📝 Description: Converts raw text into high-dimensional vectors. Useful for semantic similarity, clustering, or as input to vector databases.

...🔧 run command for the hugging face embeddings query locally
```bash
python 3.EmbeddedModels/1_embedding_huggingface.py
```

---

## ✅ 3.EmbeddedModels/2_huggingface_document.py

🎯 Purpose: Embed entire documents using Hugging Face models.

📝 Description: Processes full documents (multi-sentence text) and converts them into embeddings. Prepares data for similarity search or vector indexing.

...🔧 run command for the hugging face embeddings document
```bash
python 3.EmbeddedModels/2_huggingface_document.py
```

---

## ✅ 3.EmbeddedModels/3_document_similarity.py

🎯 Purpose: Compute similarity between documents.

📝 Description: Uses cosine similarity between embedding vectors to assess how semantically similar different documents are. Useful for retrieval or recommendation systems.

...🔧 run command for the hugging face emdeggings and perform document cosine similarity 
```bash
python 3.EmbeddedModels/3_document_similarity.py
```

---

## ✅ Prompts/prompt.py

🎯 Purpose: Basic static prompt example.

📝 Description: Demonstrates sending a simple prompt to the LLM. Great for testing prompt formatting or syntax before scaling to dynamic use cases.

...🔧 run command for the prompt
```bash
python Prompts/prompt.py
```

---

## ✅ Prompts/prompt_generator.py

🎯 Purpose: Dynamically generate prompts.

📝 Description: Builds prompts programmatically using templates or variables. Ideal for creating structured, reusable prompt patterns.

...🔧 run command for the prompt generator
```bash
python Prompts/prompt_generator.py
```

---

## ✅ Prompts/chatbot.py

🎯 Purpose: Basic chatbot using a single message.

📝 Description: Implements a one-turn chatbot. Sends user input and returns model response. Does not maintain prior context.

...🔧 run command for the chatbot
```bash
python Prompts/chatbot.py
```

---

## ✅ Prompts/messages.py

🎯 Purpose: Create structured conversation history.

📝 Description: Builds and formats message sequences (system/user/assistant) to mimic a multi-turn conversation for LLM input.

...🔧 run command for the messages with previous history
```bash
python Prompts/messages.py
```

---

## ✅ Prompts/chatbot_previous_messages.py

🎯 Purpose: Chatbot with full history support.

📝 Description: Maintains conversation context by tracking all previous messages. Enables the LLM to respond contextually over multiple turns.


...🔧 run command for the chatbot with previous chat history and previous chat messages
```bash
python Prompts/chatbot_previous_messages.py
```

---

## ✅ Prompts/chat_prompt_template.py

🎯 Purpose: Use templated prompts in chat.

📝 Description: Shows how to create dynamic templates for chat messages with variable placeholders. Useful for repeated prompt patterns.

...🔧 run command for the chat prompt template (dynamic template & multiple messages)
```bash
python Prompts/chat_prompt_template.py
```

---

## ✅ Prompts/message_placeholder.py

🎯 Purpose: Store and reuse chat history placeholders.

📝 Description: Demonstrates using message placeholders in prompt templates for preserving and reusing conversational state between turns.

...🔧 run command for the messages with place holder(save the previous chat history)
```bash
python Prompts/message_placeholder.py
```

---

## ✅ Output_Parsers/str_output_parser.py

🎯 Purpose: Handle plain string outputs.

📝 Description: Parses simple LLM responses as plain strings. Basic parser without structural enforcement — useful for free-text outputs.

...run the str output parser with hugging face llm
```bash
python Output_Parsers/str_output_parser.py
```

---

## ✅ Output_Parsers/structured_output_parser.py

🎯 Purpose: Parse structured outputs (e.g. JSON).

📝 Description: Processes LLM responses expected in a structured format (like JSON or dicts). Ensures correct field extraction from LLM response.

...run the structured output parser
```bash
python Output_Parsers/structured_output_parser.py
```

---

## ✅ Output_Parsers/pydantic_output_parser.py

🎯 Purpose: Parse and validate output using Pydantic.

📝 Description: Uses Pydantic models to parse and enforce correct format and types in LLM outputs. Combines parsing and validation in one step.

...🔧 run command for the pydantic output parser
```bash
python Output_Parsers/pydantic_output_parser.py
```

---


## ✅ Structured_Output/typed_dict.py

🎯 Purpose: Define expected output using TypedDict.

📝 Description: Uses static typing to enforce structured keys and types in LLM outputs. Ensures response fields like {"summary": ..., "sentiment": ...} match type expectations.


...🔧 run command for the structured output with typed dict
```bash
python Structured_Output/typed_dict.py
```

---

## ✅ Structured_Output/annotated_typedict.py

🎯 Purpose: Enhanced typed output with annotations.

📝 Description: Adds metadata (like descriptions) to TypedDict fields. Helps guide the LLM to produce more accurate structured outputs.

...🔧 run command for the annotated typed dict with structured output
```bash
python Structured_Output/annotated_typedict.py
```

---

## ✅ Structured_Output/pydantic_demo.py

🎯 Purpose: Intro to Pydantic for validation.

📝 Description: Validates data models using Pydantic. Useful for creating robust schemas that check LLM output formats and catch errors.

...🔧 run command for the pydantic (pydantic====data validation)
```bash
python Structured_Output/pydantic_demo.py
```

---

## ✅ Structured_Output/pydantic_structured_output.py

🎯 Purpose: Enforce structured LLM output using Pydantic.

📝 Description: Applies Pydantic models to force LLM to return data in a predictable structure (e.g. dictionaries with validated fields and types).

...run the pydantic with structured output
```bash
python Structured_Output/pydantic_structured_output.py
```

---

## ✅ Structured_Output/pydantic_json.py

🎯 Purpose: Validate or parse JSON with Pydantic schema.

📝 Description: Parses JSON responses from LLM and validates them against a defined Pydantic schema. Ensures LLM follows contract for structured APIs.

...run pydantic with json schema
```bash
python Structured_Output/pydantic_json.py
```


