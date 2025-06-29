from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="all-minilm")
# embeddings = OllamaEmbeddings(model="qwen2:0.5b")
# embeddings = OllamaEmbeddings(model="gemma3:1b") # (status code: 500)

embedding_vector = embeddings.embed_query("Hello, world")

print(f"First 10 values: {embedding_vector[:10]}")
print(f"Vector dimension: {len(embedding_vector)}")



# How it works
#
# Tokenization: Breaks down your text into tokens (words/subwords)
# Neural processing: Passes tokens through a trained neural network
# Vector generation: Produces a dense vector where each dimension captures different semantic features
# Normalization: Often normalizes the vector for consistent scaling
#
# Why embeddings matter
# Semantic similarity: Texts with similar meanings produce similar vectors. For example:
#
# "cat" and "kitten" will have vectors close to each other
# "cat" and "database" will have vectors far apart
#
# Mathematical operations: You can calculate similarity using cosine similarity, dot product, or Euclidean distance.
# Key characteristics
#
# Fixed dimension: All embeddings from the same model have the same length (e.g., 768, 1024, or 1536 dimensions)
# Dense representation: Every dimension typically has a non-zero value
# Context-aware: Modern embeddings consider the context around words
#
# Common use cases
#
# Vector search: Finding similar documents or text passages
# Clustering: Grouping similar texts together
# Classification: Using embeddings as features for ML models
# Recommendation systems: Finding similar content
#
# embed_query vs embed_documents
#
# embed_query(): For single text strings (search queries)
# embed_documents(): For batches of documents (more efficient for multiple texts)
#
# The embedding vectors enable computers to understand and work with text mathematically,
# making semantic search and similarity matching possible.

