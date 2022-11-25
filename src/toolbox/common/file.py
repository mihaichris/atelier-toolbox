"""Module for file."""
import os
import tomli


def get_filename(file: str) -> str:
    """Return the filename of the file"""
    return os.path.splitext(file)[0]


def load_toml(path: str):
    """Load TOML file"""
    with open(path, mode='rb') as toml_file:
        return tomli.load(toml_file)