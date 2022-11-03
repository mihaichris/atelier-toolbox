import os
import tomli


def get_filename(file: str) -> str:
    return os.path.splitext(file)[0]


def load_toml(path: str):
    with open(path, mode='rb') as toml_file:
        return tomli.load(toml_file)
