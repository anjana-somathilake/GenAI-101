
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader("./text.data")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)
splitted_docs = splitter.split_documents(docs)
print(splitted_docs)

# # pip install pypdf
# from langchain_community.document_loaders import PyPDFLoader
# loader = PyPDFLoader("./test.pdf")
# pages = loader.load()