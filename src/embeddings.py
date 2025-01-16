from langchain.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from logger import logging

class Embeddings:
    def __init__(self):
        logging.info('Creating embeddings...')
        self.embeddings = HuggingFaceEmbeddings(model_name = 'all-MiniLM-L6-v2')
        logging.info("Embeddings created")

        logging.info('Creating vector store...')
        self.vector_store = FAISS(self.embeddings.vector_size)
        logging.info('Vector store initiated')

    def create_embeddings(self, documents):

        logging.info('Adding documment embeddings to local vector store...')
        embeddings = self.vector_store.from_documents(
            documents = documents, 
            embeddings = self.embeddings
        )
        logging.info('Embeddings added to vector store')

        return embeddings
    


