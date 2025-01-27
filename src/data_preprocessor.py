from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from src.logger import logging

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

class URLLoader:

    def __init__(self, urls):
        self.urls = urls

        logging.info(f'Loading documents from {self.urls}')
        self.loader = UnstructuredURLLoader(
            urls = self.urls
        )

    def load(self):

        logging.info('Loading documents')
        documents = self.loader.load()
        logging.info(f'Number of documents loaded: {len(documents)}')
        return documents

    
class TextSplitter:

    def __init__(self, documents, chunk_size=500, chunk_overlap=100):
        self.documents = documents
        logging.info("Creating recursive character text splitter...")
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = chunk_size,
            chunk_overlap = chunk_overlap
        )

    def split(self):
        logging.info('Splitting documents')
        chunks = self.text_splitter.split_documents(self.documents)
        logging.info(f"Documents split into {len(chunks)} chunks")

        return chunks 