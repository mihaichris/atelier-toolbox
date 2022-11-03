from typing import Optional
import click
import typer
from common.file import load_toml
from common.output import show_message, abort
from random import randrange
from enum import Enum

app = typer.Typer(name="DM (Direct Message) Framework CLI Tool")

TEMPLATES = load_toml('src/console/sets/dm/templates.toml')


class Languages(str, Enum):
    ro = "ro"
    en = "en"


class MessageType(str, Enum):
    simple = "simple"
    complex = "complex"


@app.command()
def templates():
    """Lists all available templates."""
    pass


@app.command()
def connect_message(
        message_type: MessageType = typer.Option(
            MessageType.simple, case_sensitive=False),
        lang: Languages = typer.Option(Languages.en, case_sensitive=False),
        number: Optional[int] = typer.Argument(None)):
    """Get a connect message."""
    if number is None:
        number = randrange(1, len(get_connect_messages()))
    connect_message = get_connect_message(number, lang, message_type)
    if connect_message is None:
        abort('No connect message found with id: {0} and language {1} and language {2}'.format(
            number, lang, message_type))
    show_message(connect_message)


def get_connect_messages():
    return TEMPLATES['connect_messages']


def get_connect_message(id: int, lang: str, message_type: str):
    for connect_message in get_connect_messages():
        if connect_message['id'] == id and connect_message['lang'] == lang and connect_message['type'] == message_type:
            return connect_message
