import json
import subprocess

from rich.console import Console
from rich.table import Table

from coverage_rich.config import config


def report(coverage_data=None):
    if coverage_data is None:
        coverage_data = json.loads(
            subprocess.check_output(["coverage", "json", "-o", "-"])
        )
    meta = coverage_data.get("meta", {})

    table = Table(title=f"pytest-{meta.get('version')} {meta.get('timestamp')}")
    table.add_column("Name", style="blue")
    table.add_column("Stmts", justify="right", style="green")
    table.add_column("Miss", justify="right", style="red")
    table.add_column("Branch", justify="right", style="green")
    table.add_column("BrPart", justify="right", style="green")
    table.add_column("Cover", justify="right", style="green")
    table.add_column("Missing", justify="right", style="green")

    for filename, row in coverage_data.get("files", {}).items():
        if row.get("summary", {}).get("percent_covered", 0) < 80:
            color = "red"
            name_color = "red"
        else:
            color = "green"
            name_color = "blue"
        table.add_row(
            f"[{name_color}]{filename}[/]",
            str(row.get("summary", {}).get("num_statements", "")),
            f'{row.get("summary", {}).get("missing_lines", "")}',
            str(row.get("summary", {}).get("missing_branches", "")),
            str(row.get("summary", {}).get("num_partial_branches", "")),
            f'[{color}]{row.get("summary", {}).get("percent_covered_display", "")}%[/]',
            f'[{color}]{", ".join([str(i) for i in row.get("missing_lines", [])])}[/]',
        )

    row = coverage_data.get("totals", {})

    if row.get("percent_covered", 0) < 80:
        color = "red"
        name_color = "red"
    else:
        color = "green"
        name_color = "blue"
    filename = "overall"
    table.add_row(
        f"[{name_color}]{filename}[/]",
        str(row.get("num_statements", "")),
        f'{row.get("missing_lines", "")}',
        str(row.get("missing_branches", "")),
        str(row.get("num_partial_branches", "")),
        f'[{color}]{row.get("percent_covered_display", "")}%[/]',
    )

    console = Console()
    console.print(table)
    if coverage_data.get("totals", {}).get("percent_covered", 0) < config.get(
        "fail-under", 80
    ):
        raise SystemExit(f"test coverage under {config.get('fail-under', 80)}")
