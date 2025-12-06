from __future__ import annotations

from textwrap import dedent

import pytest

from . import conftest


# Example "small input" tests taken from the Day 1 stub implementation.
# Add more dictionaries to EXAMPLE_CASES for each new example you want to
# validate. For each case you specify:
#
#   - day:      Advent of Code day number (int)
#   - part:     1 or 2
#   - input:    The small example input as a single string
#   - expected: The expected answer as a string (what the puzzle states)
#
# This makes it quick to paste the sample input from the site and record
# the known answers for regression.

DAY_1_INPUT = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
""".strip()

from dataclasses import dataclass


@dataclass
class Example:
    day: int
    part: int
    input_: str
    expected: any


EXAMPLE_CASES: list[dict[str, object]] = [
    Example(day=1, part=1, input_=DAY_1_INPUT, expected=3),
    Example(day=1, part=2, input_=DAY_1_INPUT, expected=6),
    Example(day=1, part=2, input_="R1000", expected=10),
]


@pytest.mark.parametrize(
    "case",
    EXAMPLE_CASES,
    ids=lambda case: f"day{case.day:02d}-part{case.part}",
)
def test_examples(case: dict[str, object]) -> None:
    result = conftest.run_solve(
        day=case.day,  # type: ignore[arg-type]
        part=case.part,  # type: ignore[arg-type]
        data=case.input_,  # type: ignore[arg-type]
    )
    assert result == case.expected
