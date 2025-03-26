# --------------------------------------------
# Research Assistant: Ties the components together to answer user queries
# --------------------------------------------

from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_community.llms import OpenAI

class ResearchAssistant:
    def __init__(self, vector_store: FAISS, openai_api_key: str):
        self.vector_store = vector_store
        self.llm = OpenAI(openai_api_key=openai_api_key, temperature=0)
        # Load a QA chain that "stuffs" retrieved documents into the prompt
        self.qa_chain = load_qa_chain(self.llm, chain_type="stuff")
    
    def answer_query(self, query: str) -> str:
        # Retrieve top k relevant documents
        docs = self.vector_store.similarity_search(query, k=4)
        # Use the QA chain to generate an answer based on the documents
        answer = self.qa_chain.run(input_documents=docs, question=query)
        return answer
