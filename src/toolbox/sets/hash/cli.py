"""Hashing set commands."""
from typing import List, Optional
import hashlib
import typer
from rich.table import Table
from toolbox.common.file import get_full_path
from toolbox.common.output import show_table, show_message
from toolbox.sets.hash.hash_algoritms_enum import HashingAlgorithms
from toolbox.sets.hash import __version__ as hash_package_version

app = typer.Typer(short_help="Hashing CLI Tool")


def version_callback(value: bool):
    """Version callback."""
    if value:
        show_message(f"Hash CLI Version: {hash_package_version.__version__}")
        raise typer.Exit()


@app.command(name="files", short_help="Hashing Files CLI Tool")
def files(hashing_files: Optional[List[str]] = typer.Option(..., '--file'),
          algorithm: HashingAlgorithms = typer.Option(HashingAlgorithms.SHA_512,
                                                      autocompletion=HashingAlgorithms.values)):
    """Hashing files method"""
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Algorithm", style="dim", width=12)
    table.add_column("Hash")
    table.add_column("Path")
    for file in hashing_files:
        hasher = hashlib.new(algorithm)
        with open(file, "rb") as hashing_file:
            content = hashing_file.read()
            hasher.update(content)
            table.add_row(algorithm, hasher.hexdigest(), get_full_path(hashing_file.name))
    show_table(table)


@app.callback()
def version(ver: bool = typer.Option(None, "--version",
                                     callback=version_callback,
                                     help="Get command version.",
                                     is_eager=True)):
    """Version Output."""
    return ver
