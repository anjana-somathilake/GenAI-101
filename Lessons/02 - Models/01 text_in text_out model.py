# For generating text responses:
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="qwen2:0.5b")

template = PromptTemplate.from_template(
    "As an expert in fantasy story writing, generate a detailed and imaginative prompt for a language model based on "
    "the following input: {basic_prompt}. Keep the final prompt rich in fantasy elements and limit it to 100 words."
)


prompt = template.format(basic_prompt="write a poem about a dog")

response = llm.invoke(prompt)
print(response)