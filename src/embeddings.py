from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from src.logger import logging
from src.utils import save_vector_store
import os

class Embeddings:
    def __init__(self):
        logging.info('Creating embeddings...⌛⌛⌛')
        self.embeddings = HuggingFaceEmbeddings(model_name = 'all-MiniLM-L6-v2')
        logging.info("Embeddings created ✅✅✅")

        self.vector_store_path = os.path.join("artifacts", "vector_store.pkl") 

    def create_embeddings(self, documents):

        try:

            logging.info('Adding documment embeddings to local vector store...')
            
            logging.info('Creating vector store...⌛⌛⌛')
            vector_store = FAISS.from_documents(
                documents = documents, 
                embedding = self.embeddings
            )
            logging.info('Vector store created and Embeddings added to vector store ✅✅✅')

            ## export the vector store to a local file
            save_vector_store(vector_store, self.vector_store_path)
            logging.info(f"Succesfully exported the vector store to {self.vector_store_path} - ✅✅✅ ")

            return vector_store
        
        except Exception as e:
            logging.error(f"Error creating embeddings\n.{e}")
            return None

