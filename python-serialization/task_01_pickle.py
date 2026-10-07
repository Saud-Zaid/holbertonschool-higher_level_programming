#!/usr/bin/env python3
"""Module defining CustomObject for pickle serialization."""
import pickle


class CustomObject:
    """A custom class that can serialize and deserialize itself with pickle."""

    def __init__(self, name, age, is_student):
        """Initialize a new CustomObject instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print out the object's attributes in a formatted manner."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance and save it to the specified file.

        Args:
            filename (str): The filename of the output pickle file.

        Returns:
            None: If an exception occurs during serialization.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return an instance of CustomObject from the specified file.

        Args:
            filename (str): The filename of the input pickle file.

        Returns:
            CustomObject or None: Deserialized instance, or None on failure.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                if not isinstance(obj, cls):
                    return None
                return obj
        except Exception:
            return None
