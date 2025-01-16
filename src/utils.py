import pickle
from logger import logging

def save_vector_store(vector_store_object, path):
    with open(path, 'wb') as f:
        pickle.dump(vector_store_object, f)

    logging.info(f'Embeddings saved to {path}')
    return path
    
def load_vector_store(path):
    with open(path, 'rb') as f:
        vector_store_object = pickle.load(f)

    logging.info(f'Vectorstore loaded')
    return vector_store_object