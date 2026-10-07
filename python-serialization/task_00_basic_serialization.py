#!/usr/bin/env python3
"""Module that provides basic serialization and deserialization using JSON."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): A Python dictionary containing data to serialize.
        filename (str): The filename of the output JSON file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize JSON data from a file to a Python dictionary.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: Deserialized Python dictionary with JSON data from the file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
