import os


def get_filename(file: str) -> str:
    return os.path.splitext(file)[0]
