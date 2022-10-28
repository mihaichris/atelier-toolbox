import click
import typer

import console.sets.pdf.cli as pdf
import console.sets.business.cli as business
import console.sets.dm.cli as dm

app = typer.Typer(name="Tools for various automations.")
app.add_typer(pdf.app, name="pdf")
app.add_typer(business.app, name="business")
app.add_typer(dm.app, name="dm")
typer_click_object = typer.main.get_command(app)


def main():
    typer_click_object()
