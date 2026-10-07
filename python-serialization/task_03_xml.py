#!/usr/bin/env python3
"""Module that provides serialization and deserialization using XML."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary into XML and save it to a file.

    Args:
        dictionary (dict): The Python dictionary to serialize.
        filename (str): The filename of the output XML file.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserialize XML data from a file into a Python dictionary.

    Args:
        filename (str): The filename of the input XML file.

    Returns:
        dict: A Python dictionary with the deserialized XML data.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    return {child.tag: child.text for child in root}
