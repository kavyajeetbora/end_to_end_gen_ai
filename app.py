from src.data_preprocessor import URLLoader
from src.data_preprocessor import TextSplitter
from src.embeddings import Embeddings
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

import streamlit as st

st.title("News Chatbot 🔎")
st.subheader("This is a chatbot that can answer questions based on the news articles")

st.sidebar.title("Enter the URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

button = st.sidebar.button("Search the URLs")

query = st.text_input("Enter the question")

progress_status = st.empty()
answer = st.empty()
    
if len(urls)>0 and button and len(query) > 3:

    ## Create the url loader
    url_loader = URLLoader(urls = urls)
    documents = url_loader.load()
    progress_status.text("URLs loaded successfully  ✅✅✅")

    ## Process the documents
    text_splitter = TextSplitter(
        documents=documents,
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = text_splitter.split()
    progress_status.text(f"Documents processed successfully into {len(chunks)} chunks ✅✅✅")

    ## Once the chunking is done, Embedding
    embeddings = Embeddings()
    vector_store = embeddings.create_embeddings(chunks)

    if vector_store is not None:
        progress_status.text("Vector store created successfully ✅✅✅")

        ### HERE WE CREATE THE RAG PIPELINE

        progress_status.text("Creating the RAG pipeline...⌛⌛⌛")
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
        progress_status.text("RAG Pipeline created successfully ✅✅✅")

        response = chain.invoke(query)

        answer.text(response)
    else:
        progress_status.text("There was some problem in creating the vector store")


    
