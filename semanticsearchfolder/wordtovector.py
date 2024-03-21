import numpy as np
from transformers import AutoTokenizer, AutoModel
import torch

# # Load the BERT model and tokenizer
# tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
# model = AutoModel.from_pretrained("bert-base-uncased")

# # Query
# query = "vad är polisens öppettider i växjö?"

# # Tokenize the query
# inputs = tokenizer(query, return_tensors="pt", padding=True, truncation=True, max_length=512)

# # Generate embeddings
# with torch.no_grad():
#     outputs = model(**inputs)

# # Get the last hidden state of the first token (which is the [CLS] token)
# cls_token_embedding = outputs.last_hidden_state[0, 0, :]

# # Convert the tensor to a numpy array
# query_vector = cls_token_embedding.numpy()

# # Take the first 384 dimensions
# query_vector_384 = query_vector[:384]

# # Normalize the vector
# query_vector_384 /= np.linalg.norm(query_vector_384)

# # Print the shape of the vector to confirm its dimensions
# print("Shape of the 384-dimensional vector:", query_vector_384.shape)

# print("Vector representation of the query (384 dimensions):")
# print(query_vector_384)



from gensim.models import KeyedVectors

# Load the GloVe embeddings
glove_model = KeyedVectors.load_word2vec_format('glove.6B.300d.txt', binary=False)

# The question you provided
question = "Vad är polisens öppettider i Växjö?"

# Tokenize the question into words
words = question.split()

# Initialize an empty list to hold the word vectors
word_vectors = []

# Iterate over each word in the question
for word in words:
    # Check if the word is in the GloVe vocabulary
    if word in glove_model.vocab:
        # Get the vector for the word
        word_vector = glove_model[word]
        # Append the vector to the list
        word_vectors.append(word_vector)

# If there are no vectors (all words were out of vocabulary), print a message
if not word_vectors:
    print("No words in the question were found in the GloVe vocabulary.")
else:
    # Average the word vectors to get a single vector for the question
    question_vector = np.mean(word_vectors, axis=0)
    
    # Print the question vector
    print("Question vector:", question_vector)
