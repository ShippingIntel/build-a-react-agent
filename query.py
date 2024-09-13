# RAG Implementation
# Session 2 - Shipping Intel ReAct Class

#!/usr/bin/env python3.10
import os
import logging
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Pinecone as PineconeLangChain
from dotenv import load_dotenv


# Set up logging
# logging.basicConfig(level=logging.DEBUG)

# Load environment variables from .env file
load_dotenv()

# Set environment variables for API keys
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['PINECONE_API_KEY'] = os.getenv('PINECONE_API_KEY')

def domain_specific(query: str, index_name: str):
    try:
        embeddings = OpenAIEmbeddings()
        docsearch = PineconeLangChain.from_existing_index(index_name=index_name, embedding=embeddings)
        chat = ChatOpenAI(verbose=False, temperature=0)
        qa = RetrievalQA.from_chain_type(llm=chat, chain_type="stuff", retriever=docsearch.as_retriever(), return_source_documents=True)
        outcome_from_db_query = qa({"query": query})
        return outcome_from_db_query
    except Exception as e:
        return {"error": str(e)}

query='Give me a summary'
index = 'quickstart'
output=domain_specific(query, index)
print(output)









