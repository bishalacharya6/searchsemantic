# import json
# import csv


# JSON TO CSV
# # Define the input and output file paths
# json_file_path = r'C:\Users\NItro\Desktop\Python_Learning\combine.json'
# csv_file_path = r'C:\Users\NItro\Desktop\Python_Learning\Datas\overalldata.csv'

# # Read JSON data from the input file
# with open(json_file_path, 'r', encoding='utf-8') as json_file:
#     json_data = json.load(json_file)

# # Extract the keys to be used as column headers in the CSV file
# fieldnames = list(json_data[0].keys())

# # Write JSON data to CSV file
# with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
#     # Write the header row
#     writer.writeheader()
    
#     # Write the data rows
#     for row in json_data:
#         writer.writerow(row)

# print("Conversion from JSON to CSV completed successfully!")




###### JSON TO NEWDELIMITED JSON    

# import json

# def convert_to_ndjson(input_file, output_file):
#     # Step 1: Read the JSON file
#     with open(input_file, 'r', encoding='utf-8') as file:
#         data = json.load(file)
    
#     # Step 2: Ensure data is a list (for iteration)
#     if not isinstance(data, list):
#         data = [data]
    
#     # Step 3: Convert each object to a JSON string and write to the output file
#     with open(output_file, 'w', encoding='utf-8') as file:
#         for item in data:
#             file.write(json.dumps(item, ensure_ascii=False) + '\n')

# # Example usage
# convert_to_ndjson(r'C:\Users\NItro\Desktop\Python_Learning\combine.json', r'C:\Users\NItro\Desktop\Python_Learning\Datas\output.ndjson')




#### JSON TO JSONLINES 
import json

def convert_to_jsonlines(input_file, output_file):
    # Step 1: Read the JSON file
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Step 2: Ensure data is a list (for iteration)
    if not isinstance(data, list):
        data = [data]
    
    # Step 3: Convert each object to a JSON string and write to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(json.dumps(item, ensure_ascii=False) + '\n')

# Example usage
convert_to_jsonlines(r'C:\Users\NItro\Desktop\Python_Learning\Datas\combine.json', r'C:\Users\NItro\Desktop\Python_Learning\Datas\output.jsonL')
