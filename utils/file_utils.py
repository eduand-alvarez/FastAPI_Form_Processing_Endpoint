import csv
import os

def append_to_csv(payload_dict, filename="submissions.csv"):
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='') as file:
        fieldnames = payload_dict.keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()  # Write headers if the file is being created
        
        writer.writerow(payload_dict)
