# --------------------------------------------
# Document Manager: Loads raw documents from a folder
# --------------------------------------------

import os
from typing import List
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain.docstore.document import Document

class DocumentManager:
    def __init__(self, directory: str, file_extensions: List[str] = [".txt", ".pdf", ".docx"]):
        self.directory = directory
        self.file_extensions = file_extensions

    def load_documents(self) -> List[Document]:
        docs = []
        for filename in os.listdir(self.directory):
            if any(filename.lower().endswith(ext) for ext in self.file_extensions):
                file_path = os.path.join(self.directory, filename)
                loader = UnstructuredFileLoader(file_path)
                loaded_docs = loader.load()
                docs.extend(loaded_docs)
        return docs

