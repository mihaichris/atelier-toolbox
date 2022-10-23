import click


def show_message(message: str) -> None:
    click.echo(click.style(message, fg='blue'))
