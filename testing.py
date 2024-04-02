import json
import torch
import multiprocessing
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Check if CUDA is available
if torch.cuda.is_available():
    device = torch.device("cuda")
    print(f"Using {device} for computation.")

    # Define the file paths
    input_file_path = r"C:\Users\NItro\Desktop\Tulips_Projects\prv\prv\Removing_Repeat_Content\combine.json"
    output_file_path = r"translated_combine.json"

    # Load the data from the input JSON file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Extract summary and URLs from the data
    summary = [data_item["summary"] for data_item in data if "summary" in data_item]
    urls = [data_item["url"] for data_item in data if "url" in data_item]

    # Load the model and tokenizer on GPU
    model_name = "facebook/nllb-200-distilled-600M"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name, trust_remote_code=True)
    model.to(device)
    model.config.use_cache = False  # Disable the cache to save memory
    model.gradient_checkpointing_enable()  # Enable gradient checkpointing

    # Create a translation function
    def translate(summary_batch):
        translator = pipeline('translation', model=model, tokenizer=tokenizer, src_lang="swe_Latn", tgt_lang='eng_Latn', device=device)
        return [translator(summary)[0]['translation_text'] for summary in summary_batch]

    # Divide the summary into batches
    batch_size = 16
    num_batches = (len(summary) + batch_size - 1) // batch_size
    summary_batches = [summary[i * batch_size:(i + 1) * batch_size] for i in range(num_batches)]

    # Translate the summary batches in parallel
    translated_summary = []
    with tqdm(total=len(summary), desc='Translating Summaries') as pbar:
        for batch in summary_batches:
            translated_batch = multiprocessing.Pool().map(translate, [batch])[0]
            translated_summary.extend(translated_batch)
            pbar.update(len(batch))

    print("Translation completed.")

    # Create a new list of dictionaries with translated content and URLs
    translated_data = [{"summary": summary, "url": url} for summary, url in zip(translated_summary, urls)]

    # Write the translated data to a new JSON file
    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        json.dump(translated_data, outfile, ensure_ascii=False, indent=4)

    print("Translation and writing to JSON file completed.")
else:
    raise RuntimeError("CUDA is not available. Please ensure you have a compatible GPU installed.")
