# For generating text responses:
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="gemma3:1b")

response = llm.invoke("Brown fox jumps ...")

print(response)

