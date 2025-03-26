# --------------------------------------------
# Text Processor: Splits documents into manageable chunks
# --------------------------------------------
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from typing import List

class TextProcessor:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap
        )
    
    def split_documents(self, docs: List[Document]) -> List[Document]:
        return self.splitter.split_documents(docs)