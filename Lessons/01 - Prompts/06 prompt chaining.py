# Movie Script Chain Prompting Demo with Modern LangChain + Ollama - 9 lines
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = OllamaLLM(model="qwen2:0.5b")

chain1 = PromptTemplate.from_template("Describe the main character and setting of {movie}") | llm | StrOutputParser()
chain2 = PromptTemplate.from_template("Based on: {character_setting}, create a dramatic conflict scenario") | llm | StrOutputParser()
chain3 = PromptTemplate.from_template("Write a movie scene with dialogue for this conflict: {conflict}") | llm | StrOutputParser()

character_setting = chain1.invoke({"movie": "a space thriller like Interstellar"})
conflict = chain2.invoke({"character_setting": character_setting})
scene = chain3.invoke({"conflict": conflict})

print(f"Characters & Setting: {character_setting}\n\nConflict: {conflict}\n\nScene: {scene}")