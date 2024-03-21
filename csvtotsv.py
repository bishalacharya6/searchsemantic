# import csv

# def convert_csv_to_tsv(csv_file, tsv_file):
#     # Open CSV file for reading and TSV file for writing
#     with open(csv_file, 'r', encoding='utf-8') as csv_in, open(tsv_file, 'w' , encoding='utf-8') as tsv_out:
#         # Create CSV reader object
#         csv_reader = csv.reader(csv_in)
        
#         # Create TSV writer object
#         tsv_writer = csv.writer(tsv_out, delimiter='\t')
        
#         # Iterate through each row in the CSV file
#         for row in csv_reader:
#             # Write the row to the TSV file
#             tsv_writer.writerow(row)

# # Provide the file names
# csv_file = r'C:\Users\NItro\Desktop\Python_Learning\migration.csv'
# tsv_file = 'migration.tsv'

# # Convert CSV to TSV
# convert_csv_to_tsv(csv_file, tsv_file)




import csv
import json

def convert_csv_to_jsonl(csv_file, jsonl_file):
    # Open CSV file for reading and JSONL file for writing
    with open(csv_file, 'r', encoding="utf-8") as csv_in, open(jsonl_file, 'w', encoding='utf-8') as jsonl_out:
        # Create a CSV reader object
        csv_reader = csv.DictReader(csv_in)
        
        # Iterate through each row in the CSV file
        for row in csv_reader:
            # Write each row as a JSON object to the JSONL file
            json.dump(row, jsonl_out, ensure_ascii=False)
            jsonl_out.write('\n')  # Add newline after each JSON object

# Provide the file names
csv_file = r'C:\Users\NItro\Desktop\Python_Learning\migration.csv'
jsonl_file = 'migration.jsonl'

# Convert CSV to JSONL
convert_csv_to_jsonl(csv_file, jsonl_file)





