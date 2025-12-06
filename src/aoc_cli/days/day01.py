"""Example solution for Day 1.

Replace this with the real puzzle once available.
"""

from __future__ import annotations
from pydantic import BaseModel, ValidationError, Field
from pydantic.dataclasses import dataclass
import dataclasses
from enum import Enum


class Direction(Enum):
    LEFT = 1
    RIGHT = 2


@dataclass
class State:
    position: int = Field(default=50, ge=0, lt=100)

    def apply(self, m: Move) -> None:
        """
        Apply Move m to the current state.
        """
        self.position = (
            self.position + (m.clicks
            if m.direction == Direction.RIGHT
            else -1 * m.clicks)
        ) % 100

@dataclass
class Move:
    direction: Direction
    clicks: int = Field(gt=0)

    @classmethod
    def from_string(cls, s: str) -> self:
        if s[0] == "L":
            direction = Direction.LEFT
        elif s[0] == "R":
            direction = Direction.RIGHT
        else:
            raise ValidationError(f"Invalid direction {s[0]}")
        clicks = int(s[1:])
        return cls(direction=direction, clicks=clicks)


def part1(values) -> int:
    """Solve part 1 of the puzzle.

    For demonstration, we'll just return the sum.
    """
    state = State()
    result = 0
    for move in values:
        state.apply(move)
        result += 1 if state.position == 0 else 0
    return result


def part2(values) -> int:
    """Solve part 2 of the puzzle.

    For demonstration, we'll return the product (or 0 if empty).
    """
    raise NotImplementedError()


def solve(part: int, data: str) -> str:
    """Entry point used by the CLI.

    :param part: 1 or 2
    :param data: Raw puzzle input
    :return: The answer as a string
    """
    values = [Move.from_string(datum) for datum in data.split("\n")]
    if part == 1:
        ans = part1(values)
    elif part == 2:
        ans = part2(values)
    else:
        raise ValueError(f"Unsupported part: {part}")
    return ans
