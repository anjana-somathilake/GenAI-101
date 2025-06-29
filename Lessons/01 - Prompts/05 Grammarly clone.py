# For generating text responses:
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="qwen2:0.5b")

template = PromptTemplate.from_template("""As a professional copywriter, please rewrite the following paragraph to 
                                            match the desired tone and format:
                                            
                                            Paragraph: {paragraph}
                                            Tone: {tone}
                                            Format: {format} """)

prompt = template.format(paragraph="I need to take leave for 2 days please give me ", tone="friendly", format="email")

response = llm.invoke(prompt)
print(response)
