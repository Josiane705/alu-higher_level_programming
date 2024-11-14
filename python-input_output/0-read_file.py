#!/usr/bin/python3

"""
This module contains a function to read a text file and print its contents to stdout.
"""

def read_file(filename=""):
    """
    Reads a text file and prints its content to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string,
                         meaning no file will be opened unless a valid filename is provided.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")

