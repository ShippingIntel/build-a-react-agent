# RAG Implementation: Session 2 - Shipping Intel ReAct Class

This project contains an implementation of Retrieval-Augmented Generation (RAG) using the LangChain framework. The code integrates OpenAI's GPT models and Pinecone's vector store to create a domain-specific chatbot and document vectorizer. Additionally, a Flask-based web app is included for a basic interactive frontend.

## Table of Contents
1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Setup Instructions](#setup-instructions)
4. [Usage](#usage)
   - [Domain-Specific Query](#domain-specific-query)
   - [Text Vectorization](#text-vectorization)
   - [Foundation Model Query](#foundation-model-query)
5. [Web Application](#web-application)
6. [License](#license)

## Overview
This repository contains code for the following:
- **RAG-based domain-specific query resolution**: Queries a vector store using Pinecone and OpenAI embeddings.
- **Text file ingestion and vectorization**: Splits a document into chunks and indexes it in Pinecone for retrieval-based tasks.
- **Foundation model interaction**: Simple API call to OpenAI's GPT model.
- **Basic Flask web app**: Includes an interface to simulate chatbot interactions.

## Prerequisites
- Python 3.10+
- OpenAI API Key
- Pinecone API Key
- Flask

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/rag-implementation
   cd rag-implementation

2. **Switch to branch Week1-Vectorize**:
    ```bash
    git checkout Week2-Vectorize

3. **Install Requirements**:
    pip install -r requirements.txt

4. **Add environmental variables**:
    Create a file in the root directory named ".env"
    Please save the following 2 api-keys in this file:
    'PINECONE_API_KEY'
    'OPENAI_API_KEY'

    Ensure that .env file is ignored from version control
    echo ".env" >> .gitignore

5. 

To start flask app:
cd 'Chatbot UI'
python app.py

Project is licensed under MIT License.
