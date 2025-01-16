from logger import logging
from langchain_openai import ChatOpenAI
from langchain.chains.qa_with_sources.retrieval import RetrievalQAWithSourcesChain

class Retrieval:
    def __init__(self):
        self.llm = ChatOpenAI(model='gpt-4o-mini')
