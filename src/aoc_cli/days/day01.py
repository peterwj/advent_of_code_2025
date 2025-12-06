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


N_CLICKS = 100


@dataclass
class State:
    position: int = Field(default=50, ge=0, lt=N_CLICKS)
    times_crossing_zero: int = Field(default=0, ge=0)
    times_terminating_at_zero: int = Field(default=0, ge=0)

    def apply(self, m: Move) -> None:
        """
        Apply Move m to the current state.
        """
        for _ in range(m.clicks):
            # click, click, click
            self.position = (
                (1 if m.direction == Direction.RIGHT else -1) + self.position
            ) % N_CLICKS
            if self.position == 0:
                self.times_crossing_zero += 1
        if self.position == 0:
            self.times_terminating_at_zero += 1


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
    state = State()
    for move in values:
        state.apply(move)
    return state.times_terminating_at_zero


def part2(values) -> int:
    state = State()
    for move in values:
        state.apply(move)
    return state.times_crossing_zero


def solve(part: int, data: str) -> str:
    values = [Move.from_string(datum) for datum in data.strip().split("\n")]
    if part == 1:
        ans = part1(values)
    elif part == 2:
        ans = part2(values)
    else:
        raise ValueError(f"Unsupported part: {part}")
    return ans
