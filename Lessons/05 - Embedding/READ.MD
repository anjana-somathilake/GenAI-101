# What Are Embedding Models?

Embedding models are AI systems that convert text (or other data) into numerical vectors (arrays of numbers) that capture the semantic meaning of the content. Think of them as translators that turn human language into a mathematical format that computers can understand and work with.

## What Are Embeddings?

An embedding is essentially a list of numbers that represents the "meaning" of a piece of text. For example:

```
"The cat sat on the mat" → [0.2, -0.5, 0.8, 0.1, -0.3, ...]
"A feline rested on the rug" → [0.3, -0.4, 0.7, 0.2, -0.2, ...]
```

Notice how similar sentences get similar numbers - this is the key insight.

## Why Are They Useful?

**Semantic Search**: Instead of just matching keywords, you can find content with similar meaning:
- Search for "car" and find documents about "automobile" or "vehicle"
- Search for "happy" and find content about "joyful" or "pleased"

**Similarity Comparison**: You can mathematically compare how similar two pieces of text are by comparing their embedding vectors.

## How They Work

1. **Training**: The model learns from millions of text examples to understand language patterns
2. **Encoding**: When you give it text, it processes it through neural networks
3. **Output**: It produces a vector (typically 384, 768, or 1536 dimensions)

## Common Use Cases

**Vector Databases**: Store embeddings to enable semantic search over large document collections

**Recommendation Systems**: Find similar products, articles, or content

**Chatbots**: Help AI understand what users are really asking about

**Document Analysis**: Group similar documents together automatically

## Popular Embedding Models

**OpenAI**: `text-embedding-ada-002` (paid API)
**Ollama**: `nomic-embed-text`, `all-minilm` (free, local)
**Hugging Face**: `sentence-transformers/all-MiniLM-L6-v2` (free)

## Simple Example

```python
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="nomic-embed-text")

# Convert text to numbers
vector1 = embeddings.embed_query("I love pizza")
vector2 = embeddings.embed_query("Pizza is delicious")
vector3 = embeddings.embed_query("The weather is cold")

# vector1 and vector2 will be more similar to each other
# than either is to vector3
```

The magic is that semantically similar text gets similar numerical representations, enabling powerful search and comparison capabilities that go far beyond simple keyword matching.