from __future__ import annotations
from pydantic import BaseModel, ValidationError, Field
from pydantic.dataclasses import dataclass
import dataclasses
from typing import List, Set
import math
from copy import deepcopy


@dataclass
class Range:
    start: int
    end: int

    def is_in(self, x: int) -> bool:
        return x > self.start and x < self.end


@dataclass
class IngredientIDs:
    min_id: int
    max_id: int
    id_ranges: List[Range]

    @classmethod
    def from_string(cls, data: str) -> "IngredientIDs":
        min_id = math.inf
        max_id = -math.inf
        id_ranges = []

        for row in data.split("\n"):
            start, end = map((lambda x: int(x)), row.split("-"))
            if start < min_id:
                min_id = start
            if end > max_id:
                max_id = end
            id_ranges.append(Range(start, end + 1))

        return cls(min_id, max_id, id_ranges)


def part1(data: str) -> int:
    fresh_ranges, available_ids = data.split("\n\n")
    fresh_ranges = IngredientIDs.from_string(fresh_ranges)

    result = 0
    for row in available_ids.split("\n"):
        row = row.strip()
        if not row:
            continue
        row = int(row)
        for r in fresh_ranges.id_ranges:
            if r.is_in(row):
                result += 1
                break
    return result


def solve(part: int, data: str) -> int:
    ans = None
    if part == 1:
        ans = part1(data)
    elif part == 2:
        ans = part2(data)
    else:
        raise ValueError(f"Unsupported part: {part}")
    return ans
