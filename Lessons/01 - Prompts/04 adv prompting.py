# For generating text responses:
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="qwen2:0.5b")

# Define an advanced prompt template with multiple variables and instructions
prompt_template = PromptTemplate.from_template(
    """
    You are an expert reviewer. Write a comprehensive, unbiased review for the following product.

    Product Name: {product_name}
    Key Features: {features}
    Target Audience: {audience}

    Please structure your review as follows:
    1. Introduction (briefly introduce the product and its intended audience)
    2. Key Features (elaborate on each feature listed)
    3. Pros and Cons (list at least three of each)
    4. Conclusion (provide a summary and a recommendation)

    Use a professional and informative tone.
    """
)

# Fill in the template with actual values
prompt = prompt_template.format(
    product_name="Aussita cinnamon tea",
    features="pure ceylon cinnamon tea, organic, healthy, ethically sourced",
    audience="young adults, fitness geeks"
)


response = llm.invoke(prompt)

print(response)