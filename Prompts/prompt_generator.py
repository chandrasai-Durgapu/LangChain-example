import json
import os
from langchain.prompts import PromptTemplate

# Load a prompt template from a JSON file
def load_prompt_template(filename):
    script_dir = os.path.dirname(__file__)
    full_path = os.path.join(script_dir, filename)
    with open(full_path, 'r') as f:
        data = json.load(f)
    return PromptTemplate(**data)

# Fill in the variables in the prompt
def generate_prompt(template, variables):
    return template.format(**variables)

# Run this file directly
if __name__ == "__main__":
    template = load_prompt_template("prompt_template.json")

    variables = {
        "topic": "black holes",
        "audience": "high school student"
    }

    prompt = generate_prompt(template, variables)
    print(prompt)
