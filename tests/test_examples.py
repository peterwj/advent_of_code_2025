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
EXAMPLE_INPUT_DAY1 = dedent(
    """\
    1
    2
    3
    4
    5
    """
).strip()


EXAMPLE_CASES: list[dict[str, object]] = [
    {
        "day": 1,
        "part": 1,
        "input": EXAMPLE_INPUT_DAY1,
        "expected": "15",  # 1+2+3+4+5
    },
    {
        "day": 1,
        "part": 2,
        "input": EXAMPLE_INPUT_DAY1,
        "expected": "120",  # 1*2*3*4*5
    },
]


@pytest.mark.parametrize(
    "case",
    EXAMPLE_CASES,
    ids=lambda case: f"day{case['day']:02d}-part{case['part']}",
)
def test_examples(case: dict[str, object]) -> None:
    result = conftest.run_solve(
        day=case["day"],   # type: ignore[arg-type]
        part=case["part"], # type: ignore[arg-type]
        data=case["input"],# type: ignore[arg-type]
    )
