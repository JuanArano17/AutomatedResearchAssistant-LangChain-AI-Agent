# --------------------------------------------
# Embedding Manager: Converts text chunks into embeddings and builds a vector store
# --------------------------------------------

from typing import List
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document

class EmbeddingManager:
    def __init__(self, openai_api_key: str):
        self.embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    
    def build_vector_store(self, documents: List[Document]) -> FAISS:
        return FAISS.from_documents(documents, self.embeddings)
