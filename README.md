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

run the code
```bash
python 1.LLMs/1_llm_demo.py
```

run the code
```bash
python 2.ChatModels/1_chatmodel_groq.py
```

run the hugging face api model
```bash
python 2.ChatModels/2_chatmodel_hf_api.py
```

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



