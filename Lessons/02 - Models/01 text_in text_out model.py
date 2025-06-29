# For generating text responses:
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="qwen2:0.5b")

template = PromptTemplate.from_template(
    "Generate a detailed prompt as a expert in fantasy story writing for an LLM to this given {basic_prompt} and limit to 100 words"
)


prompt = template.format(basic_prompt="write a poem about a dog")

response = llm.invoke(prompt)
print(response)