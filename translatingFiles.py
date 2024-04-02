import json
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Check if CUDA is available
if torch.cuda.is_available():
    device = torch.device("cuda")
    print("CUDA is available. Using GPU for acceleration.")
else:
    device = torch.device("cpu")
    print("CUDA is not available. Using CPU for computation.")

# Define your API key
api_key = "AIzaSyAk_v7lTp1RT-cOb-R7TmkM-wOMnZI6ct4"

# Define the file paths
input_file_path = r"C:\Users\NItro\Desktop\Tulips_Projects\prv\prv\Removing_Repeat_Content\combine.json"
output_file_path = r"translated_combine.json"

# Load the data from the input JSON file
with open(input_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract summery and URLs from the data
summery = [data_item["summery"] for data_item in data if "summery" in data_item]
urls = [data_item["url"] for data_item in data if "url" in data_item]

# Check if the model is already loaded
if 'model' not in globals():
    # Load the model and tokenizer
    model_name = "facebook/nllb-200-distilled-600M"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)

# Translate the summery from Swedish to English
translator = pipeline('translation', model=model, tokenizer=tokenizer, src_lang="swe_Latn", tgt_lang='eng_Latn', device=0 if torch.cuda.is_available() else -1)
translated_summery = [translator(summery)[0]['translation_text'] for summery in summery]

# Create a new list of dictionaries with translated content and URLs
translated_data = [{"summery": summery, "url": url} for summery, url in zip(translated_summery, urls)]

# Write the translated data to a new JSON file
with open(output_file_path, 'w', encoding='utf-8') as outfile:
    json.dump(translated_data, outfile, ensure_ascii=False, indent=4)

print("Translation and writing to JSON file completed.")
