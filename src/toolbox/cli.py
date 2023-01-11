"""Main command."""
import typer
from toolbox.sets.pdf import pdf_app
from toolbox.sets.business import business_app
from toolbox.sets.hash import hash_app
from toolbox.sets.dw import dw_app

app = typer.Typer(short_help="Tools for various automations. 🧰")
app.add_typer(business_app, name="business")
app.add_typer(dw_app, name="dw")
app.add_typer(pdf_app, name="pdf")
app.add_typer(hash_app, name="hash")

command = typer.main.get_command(app)


def main():
    """Main input command."""
    command()


if __name__ == '__main__':
    main()
