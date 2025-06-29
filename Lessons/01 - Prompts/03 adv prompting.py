# For generating text responses:
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.1")

template = PromptTemplate.from_template(
    "Translate the following sentence to Sinhalese : {sentence} output as a single sentance"
)

prompt = template.format(sentence="how are you?")

# prompt = template.format(sentence="how are you?")
# prompt = template.format(sentence="how are you?")

# response = llm.invoke(prompt)
response = llm.chat(prompt)

print(response)