# Advent of Code Python Scaffold

This project provides a excellent scaffold for solving
[Advent of Code](https://adventofcode.com/) puzzles using:

- Python
- [Click](https://click.palletsprojects.com/) for the command-line interface
- [Poetry](https://python-poetry.org/) for dependency management

## Installation

```bash
cd aoc_scaffold
poetry install
```

This will install dependencies and register the `aoc` CLI via Poetry.

You can run commands via:

```bash
poetry run aoc --help
```

## Running a day

By convention, inputs live in the `inputs/` directory as `dayXX.txt`.

Example:

```bash
poetry run aoc run 1 --part 1
poetry run aoc run 1 --part 2 --input path/to/custom_input.txt
```

Each day is implemented in a module `src/aoc_cli/days/dayXX.py` and must
expose a function:

```python
def solve(part: int, data: str) -> str:
    ...
```

The CLI will import this module and call `solve`.

## Adding a new day

Use the built-in scaffolding command:

```bash
poetry run aoc new 2
```

This will create:

- `src/aoc_cli/days/day02.py` (from `templates/day_template.py.txt`)
- `inputs/day02.txt`

You can override existing files with:

```bash
poetry run aoc new 2 --force
```

## Testing

You can add your own tests under a `tests/` directory and run them with:

```bash
poetry run pytest
```

## Notes

- No VCS (like git) is initialized by this scaffold.
- The template is intentionally minimal; customize it to your own style.
