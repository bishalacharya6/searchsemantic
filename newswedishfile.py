import json
from translate import Translator
import time

def translate_json(input_file, output_file, batch_size=1000, max_retries=10, retry_delay=1):
    # Load the JSON data
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Initialize Translator
    translator = Translator(to_lang="en")
    
    # Translate each key-value pair in the JSON
    translated_data = []
    num_batches = len(data) // batch_size + 1
    for i in range(num_batches):
        start_idx = i * batch_size
        end_idx = min((i + 1) * batch_size, len(data))
        batch = data[start_idx:end_idx]
        translated_batch = translate_batch(translator, batch, max_retries, retry_delay)
        translated_data.extend(translated_batch)

    # Write translated data to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(translated_data, file, ensure_ascii=False, indent=4)

def translate_batch(translator, batch, max_retries, retry_delay):
    translated_batch = []
    for dictionary in batch:
        translated_dictionary = {}
        for key, value in dictionary.items():
            translated_key = translate_with_retry(translator, key, max_retries, retry_delay)
            translated_value = translate_with_retry(translator, value, max_retries, retry_delay)
            translated_dictionary[translated_key] = translated_value
        translated_batch.append(translated_dictionary)
    return translated_batch

def translate_with_retry(translator, text, max_retries, retry_delay):
    retries = 0
    while retries < max_retries:
        try:
            translation = translator.translate(text)
            return translation
        except Exception as e:
            print(f"Translation failed for '{text}'. Retrying...")
            retries += 1
            time.sleep(retry_delay)
    print(f"Failed to translate '{text}' after {max_retries} retries.")
    return text  # Return the original text if translation fails

# Example usage
translate_json(r"C:\Users\NItro\Desktop\Python_Learning\2_modified_migration_plus_polisen.json", "translated_data.json")

# Example usage

# Example usage
