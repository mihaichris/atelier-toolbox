"""Download set commands."""
from typing import Optional
import typer
from toolbox.common.output import show_message
from toolbox.sets.dw import __version__ as dw_package_version
from toolbox.sets.dw.download import Download

app = typer.Typer(short_help="Download CLI Tool")


def version_callback(value: bool):
    """Version callback."""
    if value:
        show_message(f"Hash CLI Version: {dw_package_version.__version__}")
        raise typer.Exit()


@app.command(short_help="Download from url")
def url(url_link: str,
        destination: Optional[str] = typer.Argument(None,
                                                    help="Target filepath"),
        force: bool = typer.Option(False, '--force', '-f', '-o',
                                   help="Overwrite if the file already exists.", is_flag=True),
        resume: bool = typer.Option(False, '--resume', '-c',
                                    help="Resume failed or cancelled download.", is_flag=True),
        echo: bool = typer.Option(False, '--echo', '-e',
                                  help="Print the filepath to stdout after downloading.",
                                  is_flag=True),
        quiet: bool = typer.Option(False, '--quiet', '-q',
                                   help="Suppress filesize and progress info.", is_flag=True),
        batch: bool = typer.Option(False, '--batch', '-b',
                                   help="Download files in batch.",
                                   is_flag=True)):
    """Download from url."""
    downloader = Download(url=url_link, des=destination, overwrite=force,
                          continue_download=resume, echo=echo,
                          quiet=quiet, batch=batch)
    downloader.download()
    if echo:
        print(downloader.des)


@app.callback()
def version(ver: bool = typer.Option(None, "--version",
                                     callback=version_callback, help="Get command version.",
                                     is_eager=True)):
    """Version Output."""
    return ver
