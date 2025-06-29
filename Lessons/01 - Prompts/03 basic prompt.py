# For generating text responses:
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="qwen2:0.5b")

template = PromptTemplate.from_template(
    "As a world class marketing expert write a one line catchy description for this {product}"
)

# prompt = template.format(product="organic toothpase")
prompt = template.format(product="ceylon cinamon tea")
# prompt = template.format(product="organic toothpase")
# prompt = template.format(product="organic toothpase")

response = llm.invoke(prompt)
print(response)
