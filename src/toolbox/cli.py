"""Main command."""
from typing import List, Optional
import hashlib
import typer
from rich.table import Table
from toolbox.common.file import get_full_path
from toolbox.common.output import show_table, show_message
from toolbox.sets.pdf import pdf_app
from toolbox.sets.business import business_app
from toolbox.sets.hash import HashingAlgorithms
from toolbox.sets.hash import __version__ as hash_package_version

app = typer.Typer(short_help="Tools for various automations. 🧰")
app.add_typer(pdf_app, name="pdf")
app.add_typer(business_app, name="business")


def version_callback(value: bool):
    if value:
        show_message(f"Hash CLI Version: {hash_package_version.__version__}")
        raise typer.Exit()


@app.command(name="hash", short_help="Hashing Files CLI Tool")
def hashing(files: Optional[List[str]] = typer.Option(..., '--file'),
            algorithm: HashingAlgorithms = typer.Option(HashingAlgorithms.SHA_512,
                                                        autocompletion=HashingAlgorithms.values),
            version: Optional[bool] = typer.Option(None, "--version", help="Get command version",
                                                   callback=version_callback)):
    """Hashing files method"""
    if version:
        return hash_package_version
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Algorithm", style="dim", width=12)
    table.add_column("Hash")
    table.add_column("Path")
    for file in files:
        hasher = hashlib.new(algorithm)
        with open(file, "rb") as hashing_file:
            content = hashing_file.read()
            hasher.update(content)
            table.add_row(algorithm, hasher.hexdigest(), get_full_path(hashing_file.name))
    show_table(table)


command = typer.main.get_command(app)


def main():
    """Main input command."""
    command()


if __name__ == '__main__':
    main()
