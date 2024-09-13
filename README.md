# RAG Implementation: Session 2 - Shipping Intel ReAct Class

This project contains an implementation of Retrieval-Augmented Generation (RAG) using the LangChain framework. The code integrates OpenAI's GPT models and Pinecone's vector store to create a domain-specific chatbot and document vectorizer. Additionally, a Flask-based web app is included for a basic interactive frontend.

Please see the Branch Week2-Vectorize for the code implementation including pre-requisites and setup instructions.

## Table of Contents
1. [Overview](#overview)

6. [License](#license)

## Overview
This repository contains code for the following:
- **RAG-based domain-specific query resolution**: Queries a vector store using Pinecone and OpenAI embeddings.
- **Text file ingestion and vectorization**: Splits a document into chunks and indexes it in Pinecone for retrieval-based tasks.
- **Foundation model interaction**: Simple API call to OpenAI's GPT model.
- **Basic Flask web app**: Includes an interface to simulate chatbot interactions.


Project is licensed under MIT License.

