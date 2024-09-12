import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

os.environ['OPENAI_API_KEY'] = 'ENTER API KEY'
os.environ['PINECONE_API_KEY'] = 'ENTER API KEY'

def vectorize_txt(index, file_path_text):
    try:
        print("Ingesting... [TextLoader]")
        # Check if the file exists before attempting to load
        if os.path.exists(file_path_text):
            loader = TextLoader(file_path_text)
            document = loader.load()
        else:
            raise FileNotFoundError(f"Error: The file {file_path_text} does not exist.")

        print("Splitting... [RecursiveCharacterTextSplitter]")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
        texts = text_splitter.split_documents(document)
        print(f"Created {len(texts)} chunks.")

        print("Embed... [OpenAIEmbeddings]")
        embeddings = OpenAIEmbeddings()

        print("Ingesting... [Pinecone]")
        PineconeVectorStore.from_documents(texts, embeddings, index_name=index)
        print("Finished.")
    except Exception as e:
        print(f"An error occurred: {e}")

index_name = 'ENTER INDEX NAME'
path = 'ENTER PATH TO TXT FILE'
vectorize_txt(index_name, path)

