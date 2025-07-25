# For generating text responses:
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="qwen2:0.5b")

template = PromptTemplate.from_template("Complete the sentence as a joke: {sentence}")

prompt = template.format(sentence="Brown fox jumps ...")

response = llm.invoke(prompt)
print(response)
