import os
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))

index_name = os.getenv('indexname')
pc.create_index(
    name=index_name,
    dimension=1536, # Replace with your model dimensions
    metric="cosine", # Replace with your model metric
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    ) 
)