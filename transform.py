#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: shaunahan
"""

# use functions to transform data
# use transform_case() to lowercase strings, taking a generic string as an argument
# update_date_of_sale() to update the date format, taking a date format string as an argument

# Import the submodule required
from datetime import datetime

def transform_case(input_string):
    """
    Lowercase string fields
    """
    # Return the string lowercase
    return input_string.lower()
  
def update_date_of_sale(date_input):
    """
    Update date format from DD/MM/YYYY to YYYY-MM-DD
    """
    # Create a datetime object
    current_format = datetime.strptime(date_input, "%d/%m/%Y")
    # Convert to the expected date format
    new_format = current_format.strftime("%Y-%m-%d")
    return new_format

# develop functions to clean the price and description columns
# update_price() function takes a string like value as input returns an integer
# update_description(), which gets a description as input and returns a new/second hand


def update_price(price_input):
    """
    Returns price as an integer by removing:
    - "€" and "," symbol
    - Converting to float first then to integer
    """
    # Replace € with an empty string
    price_input = price_input.replace("€", "")
    # Replace comma with an empty string
    price_input = price_input.replace(",", "")
    # Convert to float
    price_input = float(price_input)
    # Return price_input as integer
    return int(price_input)
  
def update_description(description_input):
    """
    Simplifies the description field for future analysis. Returns:
    - "new" if string contains "new" substring
    - "second-hand" if string contains "second-hand" substring
    """
    description_input = transform_case(description_input)
    # Check description and return "new" or "second-hand"
    if "new" in description_input:
        return "new"
    elif "second-hand" in description_input:
        return "second-hand"
    return description_input




def update_price(price_input):
    """
    Return price as integer by removing:
    - "€" symbol
    - "," to convert the number into float first (e.g. from "€100,000.00" to "100000.00")
    """
    price_input = price_input.replace("€", "")
    price_input = float(price_input.replace(",", ""))
    return int(price_input)


def truncate_table():
    """
    Ensure that "ppr_raw_all" table is always in empty state before running any transformations.
    And primary key (id) restarts from 1.
    """
    session.execute(
        text("TRUNCATE TABLE ppr_raw_all;ALTER SEQUENCE ppr_raw_all_id_seq RESTART;")
    )
    session.commit()

# apply all transformations and save the newly updated rows into the database table PprRawAll.
def transform_new_data():
    """
    Apply all transformations for each row in the .csv file before saving it into database
    """
    with open(raw_path, mode="r", encoding="windows-1252") as csv_file:
        # Read the new CSV snapshot ready to be processed
        reader = csv.DictReader(csv_file)
        # Initialize an empty list for our PprRawAll objects
        ppr_raw_objects = []
        for row in reader:
            # Apply transformations and save as PprRawAll object
            ppr_raw_objects.append(
                PprRawAll(
                    date_of_sale=update_date_of_sale(row["date_of_sale"]),
                    address=transform_case(row["address"]),
                    postal_code=transform_case(row["postal_code"]),
                    county=transform_case(row["county"]),
                    price=update_price(row["price"]),
                    description=update_description(row["description"]),
                )
            )
        # Save all new processed objects and commit
        session.bulk_save_objects(ppr_raw_objects)
        session.commit()


def main():
    print("[Transform] Start")
    print("[Transform] Remove any old data from ppr_raw_all table")
    ____
    print("[Transform] Transform new data available in ppr_raw_all table")
    ____
    print("[Transform] End")