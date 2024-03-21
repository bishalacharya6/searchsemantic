import os
import pandas as pd
import torch
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec, PodSpec
from tqdm.auto import tqdm

# Define the path to the model file
model_path = 'paraphrase-multilingual-MiniLM-L12-v2.model'

# Set the device
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# Check if the pre-trained model is already saved
if os.path.exists(model_path):
    # Load the pre-trained model from the saved file
    model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2', device=device)
    model.load_state_dict(torch.load(model_path, map_location=device))
else:
    # Initialize the model and save it to disk
    model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2', device=device)
    torch.save(model.state_dict(), model_path)

# Load the JSON file into a DataFrame
dataset = pd.read_json(r"C:\Users\NItro\Desktop\Python_Learning\2_modified_migration_plus_polisen.json")

# Extract the 'content' column
content = dataset['content']

# Display the first few rows of the content column
print(content.head())

# Define a batch size for encoding
batch_size = 100 # Adjust based on your system's memory capacity

# Initialize an empty list to store the encoded vectors
encoded_vectors = []

# Encode the texts in batches to manage memory usage
for i in range(0, len(dataset), batch_size):
    batch = dataset.iloc[i:i+batch_size]['content'].tolist() # Convert the batch to a list
    vectors = model.encode(batch)
    encoded_vectors.extend(vectors.tolist())

# At this point, `encoded_vectors` contains the encoded vectors for all texts
print(len(encoded_vectors))

# Initialize connection to Pinecone
api_key = os.environ.get('PINECONE_API_KEY') or '041f5d83-b9ec-4fbd-bb68-f4ba876e82b6'
pc = Pinecone(api_key=api_key)

index_name = 'semantic-search-fast'
index = pc.Index(index_name)

# Assuming you have already created the Pinecone index and it's ready for use
# Here you would typically insert the encoded vectors into the Pinecone index
# For demonstration, let's assume you're querying the index

# Example query
query = "vad polisens öppettider i växjö?"
xq = model.encode(query).tolist()
xc = index.query(vector=xq, top_k=5, include_metadata=True)
print(xc)
