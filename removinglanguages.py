# import json
# import re

# # Define the patterns to be removed from the URLs
# patterns = [
#     r"https://polisen\.se/yi/",
#     r"https://polisen\.se/fi/",
#     r"https://polisen\.se/de/",
#     r"https://polisen\.se/fr/",
#     r"https://polisen\.se/es/",
#     r"https://polisen\.se/se/",
#     r"https://polisen\.se/fit/",
#     r"https://polisen\.se/ar/",
#     r"https://polisen\.se/fa/",
#     r"https://polisen\.se/rom/",
#     r"https://polisen\.se/bks/"
# ]

# # Read the input JSON file
# input_file = r"C:\Users\NItro\Desktop\Python_Learning\polisenfulldata.json"
# output_file = "output.json"

# with open(input_file, "r", encoding="utf-8") as f:
#     data = json.load(f)

# # Function to check if a URL contains any of the specified patterns
# def contains_pattern(url):
#     for pattern in patterns:
#         if re.search(pattern, url):
#             return True
#     return False

# # Remove content containing the specified patterns from the data
# filtered_data = [item for item in data if not contains_pattern(item['url'])]

# # Write the filtered data to a new JSON file
# with open(output_file, "w", encoding="utf-8") as f:
#     json.dump(filtered_data, f, indent=4, ensure_ascii=False)

# print("Filtered data saved to", output_file)




import json
from langdetect import detect

# Function to check if the text is in Swedish or English
def is_swedish_or_english(text):
    try:
        lang = detect(text)
        return lang == 'sv' or lang == 'en'
    except:
        # If language detection fails, assume it's not Swedish or English
        return False

# Read the input JSON file
input_file = r"C:\Users\NItro\Desktop\Tulips_Projects\prv\prv\ALL_Sites_Data\trafikverket.json"
output_file = "trafikverket.json"


with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Remove content with languages other than Swedish or English
filtered_data = [item for item in data if is_swedish_or_english(item['content'])]

# Write the filtered data to a new JSON file
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(filtered_data, f, indent=4, ensure_ascii=False)

print("Filtered data saved to", output_file)
