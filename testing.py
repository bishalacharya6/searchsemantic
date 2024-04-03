import json
import torch
import multiprocessing
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Check if CUDA is available
if not torch.cuda.is_available():
    raise RuntimeError("CUDA is not available. Please ensure you have a compatible GPU installed.")

# Define the device
device = torch.device("cuda")

# Define the file paths
input_file_path = r"C:\Users\NItro\Desktop\Tulips_Projects\prv\prv\Removing_Repeat_Content\combine.json"
output_file_path = r"translated_combine.json"

# Load the data from the input JSON file
with open(input_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract summery and URLs from the data
summery = [data_item["summery"] for data_item in data if "summery" in data_item]
urls = [data_item["url"] for data_item in data if "url" in data_item]

# Load the model and tokenizer
model_name = "facebook/nllb-200-distilled-600M"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name, trust_remote_code=True)

# Wrap the model with DataParallel
if torch.cuda.device_count() > 1:
    print("Using", torch.cuda.device_count(), "GPUs!")
    model = torch.nn.DataParallel(model)

# Move model to GPU
model.to(device)

# Create a translation function
def translate(summery_batch):
    translator = pipeline('translation', model=model, tokenizer=tokenizer, src_lang="swe_Latn", tgt_lang='eng_Latn', device=device)
    return [translator(summery)[0]['translation_text'] for summery in summery_batch]

# Divide the summery into batches
batch_size = 16
num_batches = (len(summery) + batch_size - 1) // batch_size
summery_batches = [summery[i * batch_size:(i + 1) * batch_size] for i in range(num_batches)]

# Create a pool of worker processes
pool = multiprocessing.Pool()

# Translate the summery batches in parallel on GPU
translated_summery = []
with tqdm(total=len(summery), desc='Translating Summaries') as pbar:
    for batch in summery_batches:
        translated_batch = pool.map(translate, [batch])[0]
        translated_summery.extend(translated_batch)
        pbar.update(len(batch))

print("Translation completed.")

# Create a new list of dictionaries with translated content and URLs
translated_data = [{"summery": summery, "url": url} for summery, url in zip(translated_summery, urls)]

# Write the translated data to a new JSON file
with open(output_file_path, 'w', encoding='utf-8') as outfile:
    json.dump(translated_data, outfile, ensure_ascii=False, indent=4)

print("Translation and writing to JSON file completed.")
