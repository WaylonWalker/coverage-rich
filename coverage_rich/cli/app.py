import typer

from coverage_rich.cli.common import verbose_callback
from coverage_rich.cli.config import config_app
from coverage_rich.cli.report import report_app

app = typer.Typer(
    name="coverage_rich",
    help="A rich terminal report for coveragepy.",
)
app.add_typer(config_app)
app.add_typer(report_app)


def version_callback(value: bool) -> None:
    """Callback function to print the version of the coverage-rich package.

    Args:
        value (bool): Boolean value to determine if the version should be printed.

    Raises:
        typer.Exit: If the value is True, the version will be printed and the
        program will exit.

    Example:
        version_callback(True)
    """
    if value:
        from coverage_rich.__about__ import __version__

        typer.echo(f"{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        callback=version_callback,
        is_eager=True,
    ),
    verbose: bool = typer.Option(
        False,
        callback=verbose_callback,
        help="show the log messages",
    ),
) -> None:
    return


if __name__ == "__main__":
    typer.run(main)
