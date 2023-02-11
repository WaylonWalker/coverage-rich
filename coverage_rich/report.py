import json
from pathlib import Path

from rich.console import Console
from rich.table import Table

from coverage_rich.config import config


def report():
    coverage_data = json.loads(Path("coverage.json").read_text())
    meta = coverage_data["meta"]

    table = Table(title=f"pytest-{meta.get('version')} {meta.get('timestamp')}")
    table.add_column("Name", style="blue")
    table.add_column("Stmts", justify="right", style="green")
    table.add_column("Miss", justify="right", style="red")
    table.add_column("Branch", justify="right", style="green")
    table.add_column("BrPart", justify="right", style="green")
    table.add_column("Cover", justify="right", style="green")
    table.add_column("Missing", justify="right", style="green")

    for filename, row in coverage_data["files"].items():
        if row["summary"]["percent_covered"] < 80:
            color = "red"
            name_color = "red"
        else:
            color = "green"
            name_color = "blue"
        table.add_row(
            f"[{name_color}]{filename}[/]",
            str(row["summary"]["num_statements"]),
            f'{row["summary"]["missing_lines"]}',
            str(row["summary"]["missing_branches"]),
            str(row["summary"]["num_partial_branches"]),
            f'[{color}]{row["summary"]["percent_covered_display"]}%[/]',
            f'[{color}]{", ".join([str(i) for i in row["missing_lines"]])}[/]',
        )

    row = coverage_data["totals"]
    filename = "overall"
    table.add_row(
        f"[{name_color}]{filename}[/]",
        str(row["num_statements"]),
        f'{row["missing_lines"]}',
        str(row["missing_branches"]),
        str(row["num_partial_branches"]),
        f'[{color}]{row["percent_covered_display"]}%[/]',
    )

    console = Console()
    console.print(table)
    if coverage_data["totals"]["percent_covered"] < config.get("fail-under", 80):
        raise SystemExit(f"test coverage under {config.get('fail-under', 80)}")
