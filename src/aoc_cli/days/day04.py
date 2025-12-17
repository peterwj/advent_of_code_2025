from __future__ import annotations
from pydantic import BaseModel, ValidationError, Field
from pydantic.dataclasses import dataclass
import dataclasses
from typing import List, Tuple
from copy import deepcopy


@dataclass
class Room:
    grid: List[List[bool]]

    @classmethod
    def from_string(cls, s: str) -> "Room":
        grid = []
        for row in s.split("\n"):
            cells = []
            for col in row:
                cells.append(col == "@")
            grid.append(cells)
        return cls(grid)


def part1(room: Room) -> int:
    result = 0
    n_rows = len(room.grid)
    n_cols = len(room.grid[0])
    for i in range(n_rows):
        for j in range(n_cols):

            # skip cells without stack of paper
            if not room.grid[i][j]:
                continue

            count = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if (
                        x < 0
                        or y < 0
                        or x >= n_rows
                        or y >= n_cols
                        or (x == i and y == j)
                    ):
                        continue
                    count += 1 if room.grid[x][y] else 0
            if count < 4:
                result += 1
    return result


def _part2_pass(room: Room) -> Tuple[Room, int]:
    result = 0
    new_room = deepcopy(room)
    n_rows = len(room.grid)
    n_cols = len(room.grid[0])
    for i in range(n_rows):
        for j in range(n_cols):

            # skip cells without stack of paper
            if not room.grid[i][j]:
                continue

            count = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if (
                        x < 0
                        or y < 0
                        or x >= n_rows
                        or y >= n_cols
                        or (x == i and y == j)
                    ):
                        continue
                    count += 1 if room.grid[x][y] else 0
            if count < 4:
                result += 1
                new_room.grid[i][j] = False
    return (new_room, result)


def part2(room: Room) -> int:
    result = 0
    while True:
        new_room, count = _part2_pass(room)
        result += count
        if count == 0:
            return result
        room = new_room


def solve(part: int, data: str) -> str:
    room = Room.from_string(data.strip())
    if part == 1:
        ans = part1(room)
    elif part == 2:
        ans = part2(room)
    else:
        raise ValueError(f"Unsupported part: {part}")
    return ans
