

from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.1:latest")
# llm = OllamaLLM(model="gemma2:2b")
# llm = OllamaLLM(model="gemma3:1b")
# llm = OllamaLLM(model="gemma2:latest")
# llm = OllamaLLM(model="qwen2:0.5b")

template = PromptTemplate.from_template("Metaphorically interpret the meaning behind this {quote} as a single paragraph")
# template = PromptTemplate.from_template("interpret the meaning behind this {quote}")

subject = "When small men begin to cast big shadows, it means that the sun is about to set"
print(subject)
prompt = template.format(quote=subject)

response = llm.invoke(prompt)
print(response)