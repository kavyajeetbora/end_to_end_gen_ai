from src.data_preprocessor import URLLoader
from src.data_preprocessor import TextSplitter
from src.embeddings import Embeddings

def main():
    
    ## Load the 
    url_loader = URLLoader(
        urls = [
            "https://talksport.com/topic/transfer-news/page",
            "https://talksport.com/topic/transfer-news/page/2",
            "https://talksport.com/topic/transfer-news/page/3"
        ]
    )

    documents = url_loader.load()

    ## Process the documents
    text_splitter = TextSplitter(
        documents=documents,
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = text_splitter.split()

    ## Once the chunking is done, Embedding
    embeddings = Embeddings()
    vector_store = embeddings.create_embeddings(chunks)

    if vector_store is not None:
        print("Vector store created successfully")
    else:
        print("There was some problem in creating the vector store")

if __name__ == "__main__":
    main()