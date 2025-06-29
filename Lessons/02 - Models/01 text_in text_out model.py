# For generating text responses:
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2-vision")

template = PromptTemplate.from_template(
    "What is in this {image}"
)


prompt = template.format(image="image.jp")


response = llm.invoke(prompt)
print(response)

