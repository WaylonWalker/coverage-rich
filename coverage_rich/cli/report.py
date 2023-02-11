import typer

from coverage_rich.cli.common import verbose_callback
from coverage_rich.report import report as run_report

report_app = typer.Typer()


@report_app.callback(invoke_without_command=True)
def report(
    verbose: bool = typer.Option(
        False,
        callback=verbose_callback,
        help="show the log messages",
    ),
):
    "coverage_rich report"
    run_report()
