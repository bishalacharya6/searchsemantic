from sentence_transformers import SentenceTransformer
import torch
from pinecone import Pinecone
import os

# Initialize the model
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2', device=device)

# Initialize connection to Pinecone
api_key = os.environ.get('PINECONE_API_KEY') or '041f5d83-b9ec-4fbd-bb68-f4ba876e82b6'
pc = Pinecone(api_key=api_key)

# Connect to index
index_name = 'semantic-search-fast'
index = pc.Index(index_name)

# Example query
query = "vad polisens öppettider i växjö?"
xq = model.encode(query).tolist()
xc = index.query(vector=xq, top_k=5, include_metadata=True)
print(xc)
