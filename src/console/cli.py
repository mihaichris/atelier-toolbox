import typer

from console.sets.pdf import pdf_app
from console.sets.business import business_app

app = typer.Typer(name="Tools for various automations.")
app.add_typer(pdf_app, name="pdf")
app.add_typer(business_app, name="business")
command = typer.main.get_command(app)


def main():
    command()
