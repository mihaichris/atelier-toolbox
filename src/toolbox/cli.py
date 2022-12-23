"""Main command."""
import typer
import hashlib
from toolbox.common.file import get_full_path
from enum import Enum
from rich.console import Console
from rich.table import Table
from typing import List, Optional
from toolbox.sets.pdf import pdf_app
from toolbox.sets.business import business_app

app = typer.Typer(short_help="Tools for various automations. 🧰")
app.add_typer(pdf_app, name="pdf")
app.add_typer(business_app, name="business")


class HashingAlgorithms(str, Enum):
    sha512 = "sha512"
    sha256 = "sha256"
    md5 = "md5"

    @classmethod
    def values(cls):
        return list(map(lambda c: c.value, cls))


@app.command(name="hash", short_help="Hashing Files CLI Tool")
def hashing(file: Optional[List[str]] = typer.Option(...),
            algorithm: HashingAlgorithms = typer.Option(HashingAlgorithms.sha256,
                                                        autocompletion=HashingAlgorithms.values)):
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Algorithm", style="dim", width=12)
    table.add_column("Hash")
    table.add_column("Path")
    for f in file:
        h = hashlib.new(algorithm)
        with open(f, "rb") as hashing_file:
            content = hashing_file.read()
            h.update(content)
            table.add_row(algorithm, h.hexdigest(), get_full_path(hashing_file.name))
    console.print(table)


command = typer.main.get_command(app)


def main():
    """Main input command."""
    command()


if __name__ == '__main__':
    main()
