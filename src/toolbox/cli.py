"""Main command."""
from typing import List, Optional
import hashlib
from enum import Enum
import typer
from rich.console import Console
from rich.table import Table
from toolbox.common.file import get_full_path
from toolbox.sets.pdf import pdf_app
from toolbox.sets.business import business_app

app = typer.Typer(short_help="Tools for various automations. 🧰")
app.add_typer(pdf_app, name="pdf")
app.add_typer(business_app, name="business")


class HashingAlgorithms(str, Enum):
    """Hasing Algorithms enums"""
    SHA_512 = "sha512"
    SHA_256 = "sha256"
    MD5 = "md5"

    @classmethod
    def values(cls) -> list:
        """Get all values from class as list"""
        return list(map(lambda c: c.value, cls))


@app.command(name="hash", short_help="Hashing Files CLI Tool")
def hashing(files: Optional[List[str]] = typer.Option(..., '--file'),
            algorithm: HashingAlgorithms = typer.Option(HashingAlgorithms.SHA_512,
                                                        autocompletion=HashingAlgorithms.values)):
    """Hashing files method"""
    console = Console()
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
    console.print(table)


command = typer.main.get_command(app)


def main():
    """Main input command."""
    command()


if __name__ == '__main__':
    main()
