import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set environment variables for API keys
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['PINECONE_API_KEY'] = os.getenv('PINECONE_API_KEY')

def vectorize_txt(index, file_path_text):
    try:
        # Check if the file exists before attempting to load
        if os.path.exists(file_path_text):
            loader = TextLoader(file_path_text)  # Load the text file
            document = loader.load()  # Load the document content
        else:
            raise FileNotFoundError(f"Error: The file {file_path_text} does not exist.")

        # Split the document into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
        texts = text_splitter.split_documents(document)

        # Generate embeddings for the text chunks
        embeddings = OpenAIEmbeddings()

        # Store the embeddings in Pinecone vector store
        PineconeVectorStore.from_documents(texts, embeddings, index_name=index)
    except Exception as e:
        print(f"An error occurred: {e}")

# Define the index name from pinecone
index_name = os.getenv('indexname')
# Define the path to the text file
path = os.getenv('textpath')

# Call the vectorize function with the provided index name and file path
vectorize_txt(index_name, path)

