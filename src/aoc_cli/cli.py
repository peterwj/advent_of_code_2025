from __future__ import annotations

import importlib
from pathlib import Path
from typing import Optional

import click


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUTS_DIR = PROJECT_ROOT / "inputs"
DEFAULT_TEMPLATES_DIR = PROJECT_ROOT / "templates"


@click.group()
@click.version_option()
def cli():
    """Advent of Code CLI scaffold.

    Run solutions, add new days, and manage puzzle inputs.
    """
    pass


def _load_day_module(day: int):
    module_name = f"aoc_cli.days.day{day:02d}"
    try:
        return importlib.import_module(module_name)
    except ModuleNotFoundError as exc:
        raise click.ClickException(
            f"Day {day} is not implemented yet. " f"Expected module '{module_name}'."
        ) from exc


def _read_input(day: int, input_path: Optional[Path]) -> str:
    if input_path is None:
        candidate = DEFAULT_INPUTS_DIR / f"day{day:02d}.txt"
    else:
        candidate = input_path

    if not candidate.exists():
        raise click.ClickException(
            f"Input file not found: {candidate}. "
            "Use --input to specify a file, or create the default one."
        )
    return candidate.read_text(encoding="utf-8")


@cli.command()
@click.argument("day", type=int)
@click.option(
    "--part",
    "-p",
    type=click.IntRange(1, 2),
    default=1,
    show_default=True,
    help="Puzzle part to run (1 or 2).",
)
@click.option(
    "--input",
    "-i",
    "input_path",
    type=click.Path(exists=False, dir_okay=False, path_type=Path),
    help="Path to the input file. " "Defaults to inputs/dayXX.txt in the project root.",
)
def run(day: int, part: int, input_path: Optional[Path]):
    """Run the solution for a given DAY.

    Example:

        aoc run 1 -p 2
    """
    module = _load_day_module(day)
    data = _read_input(day, input_path)
    if not hasattr(module, "solve"):
        raise click.ClickException(
            f"Module {module.__name__} has no 'solve(part, data)' function."
        )

    try:
        result = module.solve(part=part, data=data)
    except Exception as exc:  # noqa: BLE001
        raise click.ClickException(f"Error while solving: {exc}") from exc

    click.echo(result)


@cli.command()
@click.argument("day", type=int)
@click.option(
    "--force",
    "-f",
    is_flag=True,
    help="Overwrite existing files if they already exist.",
)
@click.option(
    "--inputs-dir",
    type=click.Path(file_okay=False, path_type=Path),
    default=DEFAULT_INPUTS_DIR,
    show_default=True,
    help="Directory where input files are stored.",
)
@click.option(
    "--templates-dir",
    type=click.Path(file_okay=False, path_type=Path),
    default=DEFAULT_TEMPLATES_DIR,
    show_default=True,
    help="Directory containing the day template.",
)
def new(day: int, force: bool, inputs_dir: Path, templates_dir: Path):
    """Scaffold a new DAY module and input file.

    Creates:

    \b
      - src/aoc_cli/days/dayXX.py
      - inputs/dayXX.txt

    using the template in templates/day_template.py.txt.
    """
    day_module_path = Path(__file__).resolve().parent / "days" / f"day{day:02d}.py"
    input_file_path = inputs_dir / f"day{day:02d}.txt"
    template_file = templates_dir / "day_template.py.txt"

    if not template_file.exists():
        raise click.ClickException(f"Template file not found: {template_file}")

    if day_module_path.exists() and not force:
        raise click.ClickException(
            f"{day_module_path} already exists. Use --force to overwrite."
        )
    if input_file_path.exists() and not force:
        raise click.ClickException(
            f"{input_file_path} already exists. Use --force to overwrite."
        )

    inputs_dir.mkdir(parents=True, exist_ok=True)

    template = template_file.read_text(encoding="utf-8")
    day_module_contents = template.format(day_num=day)
    day_module_path.write_text(day_module_contents, encoding="utf-8")

    if not input_file_path.exists() or force:
        input_file_path.write_text("", encoding="utf-8")

    click.echo(f"Created {day_module_path}")
    click.echo(f"Created {input_file_path}")


if __name__ == "__main__":
    cli()
