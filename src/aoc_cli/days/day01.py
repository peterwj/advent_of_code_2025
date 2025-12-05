"""Example solution for Day 1.

Replace this with the real puzzle once available.
"""
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class State:
    position: int
    

def parse(data: str):
    """Parse the raw input string into a structured form.

    This is just an example that parses one integer per line.
    Adjust as needed for each day's puzzle.
    """
    return [int(line) for line in data.splitlines() if line.strip()]


def part1(values) -> int:
    """Solve part 1 of the puzzle.

    For demonstration, we'll just return the sum.
    """
    return sum(values)


def part2(values) -> int:
    """Solve part 2 of the puzzle.

    For demonstration, we'll return the product (or 0 if empty).
    """
    result = 1
    if not values:
        return 0
    for v in values:
        result *= v
    return result


def solve(part: int, data: str) -> str:
    """Entry point used by the CLI.

    :param part: 1 or 2
    :param data: Raw puzzle input
    :return: The answer as a string
    """
    values = parse(data)
    if part == 1:
        ans = part1(values)
    elif part == 2:
        ans = part2(values)
    else:
        raise ValueError(f"Unsupported part: {part}")
    return str(ans)
