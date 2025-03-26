import os
from tools.agent import ResearchAssistant
from tools.document_manager import DocumentManager
from tools.embedding_manager import EmbeddingManager
from tools.text_processor import TextProcessor

# --------------------------------------------
# Main function: Orchestrates the document ingestion, processing, vectorization and query answering.
# --------------------------------------------
def main():
    # Configuration
    documents_directory = "./documents"  # Directory containing the research documents
    openai_api_key = os.getenv("OPENAI_API_KEY")  # Ensure your OpenAI API key is set in your environment

    # Load raw documents from the specified directory
    doc_manager = DocumentManager(documents_directory)
    raw_docs = doc_manager.load_documents()
    if not raw_docs:
        raise ValueError("No documents were loaded. Please add documents to the folder before running the application.")


    # Process documents: Split them into chunks for better embedding quality
    text_processor = TextProcessor(chunk_size=1000, chunk_overlap=200)
    processed_docs = text_processor.split_documents(raw_docs)

    # Build a vector store from the processed documents using OpenAI embeddings and FAISS
    embedding_manager = EmbeddingManager(openai_api_key)
    vector_store = embedding_manager.build_vector_store(processed_docs)

    # Initialize the Research Assistant that uses the vector store and LLM to answer queries
    research_assistant = ResearchAssistant(vector_store, openai_api_key)

    # Example query to test the research assistant
    query = input("Input user query: ")
    answer = research_assistant.answer_query(query)
    print("Query:", query)
    print("Answer:", answer)

if __name__ == "__main__":
    main()
