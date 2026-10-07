#!/usr/bin/env python3
"""Module that converts CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert data from a CSV file to JSON format and write to data.json.

    Args:
        csv_filename (str): The filename of the input CSV file.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True
    except Exception:
        return False
