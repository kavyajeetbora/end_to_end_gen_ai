from src.data_preprocessor import URLLoader
from src.data_preprocessor import TextSplitter
from src.embeddings import Embeddings
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

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


    ### HERE WE CREATE THE RAG PIPELINE

    ## Search similar documents by query from retriever
    retriever = vector_store.as_retriever(
        search_type = "similarity",
        search_kwargs = {"k": 3}
    )
    
    ## Create the prompt template
    template = """Answer the question based only on the following context:
    {context}

    Question: {question}
    """ 
    prompt_template = ChatPromptTemplate.from_template(template=template)


    ## Create the language model
    llm = ChatOpenAI(model='gpt-4o-mini')

    ## RAG Pipeline using LECL
    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt_template
        | llm
        | StrOutputParser()
    )

    query = "Who are manchester city targeting in the transfer market?"
    response = chain.invoke(query)

    print(response)

if __name__ == "__main__":
    main()