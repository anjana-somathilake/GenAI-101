

from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# llm = OllamaLLM(model="llama3.1:latest")
# llm = OllamaLLM(model="gemma2:2b")
# llm = OllamaLLM(model="gemma3:1b")
# llm = OllamaLLM(model="gemma2:latest")
llm = OllamaLLM(model="qwen2:0.5b")

template = PromptTemplate.from_template("answer this {quote}")

question = input('Ask me anything>')


prompt = template.format(quote=question)

response = llm.invoke(prompt)
print(response)