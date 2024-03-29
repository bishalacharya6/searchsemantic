
# bishalAPI - Q2gybEpvNEJ5VUs5aFM4N2NyNVk6UjRmNFcwVFVSYnlMRklLTTREWFlsZw==
# MPF Semantic Search - RUIzdEpvNEJ5VUs5aFM4N01MNEE6TWU5a29zY2JSUk8tZnlULXdiWkhDQQ==
# Cloud API Key for AI search - Y1BBZExJNEJNWmxqWEF6M1hCUms6YXptY2VvOVdTX2lsbXpaUzJ5NUFSdw==

# POlisen full data API - bnZUOE1JNEJNWmxqWEF6M21zZ186SWRrMUVCQzdSMlMyUFdrS3lIaFZ4Zw==

# import elasticsearch
# print(elasticsearch.__version__)

# from elasticsearch import Elasticsearch

# # Replace '/path/on/host/machine/http_ca.crt' with the actual path to the CA certificate file on your host machine
# print("Connecting to Elasticsearch...")
# # client = Elasticsearch(
# #     "https://localhost:9200",
# #     api_key="Q2gybEpvNEJ5VUs5aFM4N2NyNVk6UjRmNFcwVFVSYnlMRklLTTREWFlsZw==",
# #     ca_certs=r"C:\Users\NItro\Desktop\Python_Learning\http_ca.crt" 
# # )


# client = Elasticsearch(
#   "https://0b6d81aeba3343c3b48b4fd33bb1476d.us-central1.gcp.cloud.es.io:443",
#   api_key="bnZUOE1JNEJNWmxqWEF6M21zZ186SWRrMUVCQzdSMlMyUFdrS3lIaFZ4Zw=="
# )

# print("Connected. Fetching cluster info...")
# info = client.info()
# print(info)



# search_results = client.search(index="polisenfullcontrol", q="Hur bidrar Polisens IT-avdelning till hela Polismyndighetens behov av produkter och tjänster inom IT?")

# print(" \n Overall OUTPUT OF SEARCH")
# # Print the search results
# print(search_results)

# # Optionally, print the details of each hit
# count = 0
# for i, hit in enumerate(search_results['hits']['hits']):
#     if i >= 5: # Stop after the first three results
#         break
#     count += 1
#     print(f" \n\n\n  Single OUTPUT OF SEARCH {count}")
#     print(f"\n\n Document ID: {hit['_id']} \n ")
#     print(f"Document Source: {hit['_source']} \n")
#     print("\n\n\n --- \n\n\n")


from elasticsearch import Elasticsearch

# Connect to Elasticsearch cluster
client = Elasticsearch(
    "https://0b6d81aeba3343c3b48b4fd33bb1476d.us-central1.gcp.cloud.es.io:443",
    api_key="bnZUOE1JNEJNWmxqWEF6M21zZ186SWRrMUVCQzdSMlMyUFdrS3lIaFZ4Zw=="
)

# Define the inference pipeline name
inference_pipeline_name = "ml-inference-polisenfullcontrol-_elser_model_2_linux-x86_64"

# Define the search-optimized Elasticsearch index name
search_optimized_index = "polisenfullcontrol"  # Replace with your actual index name

# Execute search query with the specified ingestion pipeline
search_results = client.search(
    index=search_optimized_index,
    q="Hur bidrar Polisens IT-avdelning till hela Polismyndighetens behov av produkter och tjänster inom IT?",
    pipeline="ent-search-generic-ingestion"  # Use the search optimization pipeline
)

# Print the search results
print("Search Results:")
print(search_results)

# Process the search results
for hit in search_results['hits']['hits']:
    print("Document ID:", hit['_id'])
    print("Document Source:", hit['_source'])
    print("---")
