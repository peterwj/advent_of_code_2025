from __future__ import annotations

import importlib


def load_day_module(day: int):
    """Import and return the module for a given day.

    Example: day=1 -> aoc_cli.days.day01
    """
    module_name = f"aoc_cli.days.day{day:02d}"
    return importlib.import_module(module_name)


def run_solve(day: int, part: int, data: str) -> any:
    """Utility to call the standard solve(part, data) entrypoint for a day."""
    module = load_day_module(day)
    if not hasattr(module, "solve"):
        raise AttributeError(f"Module {module.__name__} has no 'solve' function")
    result = module.solve(part=part, data=data)
    return result 
