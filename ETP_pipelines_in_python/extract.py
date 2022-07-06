#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: shaunahan
"""

import os
import requests

# Paths
base_path = "/home/repl/workspace"
source_url = "https://assets.datacamp.com/production/repositories/5899/datasets/66691278303f789ca4acd3c6406baa5fc6adaf28/PPR-ALL.zip"
source_path =  f"{base_path}/data/source/downloaded_at=2021-01-01/ppr-all.zip"

# Create a directory at the `path` passed as an argument
def create_directory_if_not_exists(path):
    """
    Create a new directory if it doesn't exists
    """
    # os.path.dirname() returns up to the directory path.
    # In this case it is: f"{base_path}/downloaded_at=2021-01-01"
    # "ppr-all.zip" is excluded
    os.____(os.path.dirname(path), exist_ok=True)

# Write the file obtained to the specified directory
def download_snapshot():
    """
    Download the new dataset from the source
    """
    create_directory_if_not_exists(source_path)
    # Open the .zip file in binary mode
    with open(source_path, "____") as source_ppr:
        # 'verify=False' skips the verification the SSL certificate
        response = requests.____(source_url, verify=False)
        source_ppr.write(response.____)

# Download the new dataset
download_snapshot()




def save_new_raw_data():
    """
    Save new raw data from the source
    """

    create_folder_if_not_exists(raw_path)
    with tempfile.TemporaryDirectory() as dirpath:
        with ZipFile(
            source_path,
            "r",
        ) as zipfile:
            names_list = zipfile.namelist()
            csv_file_path = zipfile.extract(names_list[0], path=dirpath)
            # Open the CSV file in read mode
            with open(csv_file_path, mode="r", encoding="windows-1252") as csv_file:
                reader = csv.DictReader(csv_file)

                row = next(reader)  # Get first row from reader
                print("[Extract] First row example:", row)

                # Open the CSV file in write mode
                with open(
                    raw_path,
                    mode="w",
                    encoding="windows-1252"
                ) as csv_file:
                    # Rename field names so they're ready for the next step
                    fieldnames = {
                        "Date of Sale (dd/mm/yyyy)": "date_of_sale",
                        "Address": "address",
                        "Postal Code": "postal_code",
                        "County": "county",
                        "Price (€)": "price",
                        "Description of Property": "description",
                    }
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    # Write headers as first line
                    writer.writerow(fieldnames)
                    for row in reader:
                        # Write all rows in file
                        writer.writerow(row)

# Main function called inside the execute.py script
def main():
    print("[Extract] Start")
    print("[Extract] Downloading snapshot")
    ____
    print(f"[Extract] Saving data from '{source_path}' to '{raw_path}'")
    ____
    print(f"[Extract] End")
    