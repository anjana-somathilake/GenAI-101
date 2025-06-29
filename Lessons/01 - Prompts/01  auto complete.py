# For generating text responses:
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="qwen2:0.5b")

response = llm.invoke("Brown fox jumps ...")

print(response)

