from __future__ import annotations
from dataclasses import dataclass
import dataclasses
from typing import List, Set, Optional
import math
from copy import deepcopy


@dataclass
class Range:
    start: int
    end: int

    def contains(self, x: int) -> bool:
        return x >= self.start and x <= self.end

    def __and__(self, other: "Range") -> Optional["Range"]:
        """
        Returns None if the ranges do not overlap.

        Otherwise returns the intersection.
        """
        lesser = self if self.start < other.start else other
        other = self if other is lesser else other

        # contained-within case-- lesser has the lower start value.  if one
        # range is contained within the other, then lesser's end will
        # be greater.
        if lesser.end >= other.end:
            return Range(other.start, other.end)

        # partial overlap case
        if lesser.end >= other.start:
            return Range(other.start, lesser.end)

        # no overlap case.
        return None

    def merge(self, other: "Range") -> Sequence["Range"]:
        # returns one or more ranges
        overlap = self & other
        if (overlap) is None:
            return (self, other)

        return (self | other,)

    def __or__(self, other: "Range") -> "Range":
        if (self & other) is None:
            raise ValueError("nonoverlapping ranges")

        start = self.start if self.start < other.start else other.start
        end = self.end if self.end > other.end else other.end
        return Range(start, end)

    @property
    def count(self) -> int:
        return self.end - self.start + 1


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
            id_ranges.append(Range(start, end))

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
            if r.contains(row):
                result += 1
                break
    return result


def part2(data: str) -> int:
    fresh_ranges, available_ids = data.split("\n\n")
    fresh_ranges = IngredientIDs.from_string(fresh_ranges)
    fresh_ids = []
    for i, new_range in enumerate(fresh_ranges.id_ranges):
        if i == 0:
            fresh_ids.append(new_range)
            continue

        # first, try to find an existing range overlapping with this rnage.
        merged_range = None
        merged_index = None
        for j, old_range in enumerate(fresh_ids):
            if old_range & new_range:
                (merged_range,) = old_range.merge(new_range)
                merged_index = j
                fresh_ids[j] = merged_range
                break

        # no overlap.  just add the new_range in.
        if merged_range is None:
            fresh_ids.append(new_range)
        else:
            # otherwise...merged_range may overlap ANOTHER range.
            for j, old_range in enumerate(fresh_ids):
                if old_range is merged_range:
                    continue
                if old_range & merged_range:
                    (new_merged_range,) = old_range.merge(merged_range)
                    fresh_ids.pop(j)
                    fresh_ids.pop(merged_index)
                    fresh_ids.append(new_merged_range)
                    break

    result = 0
    for r in fresh_ids:
        result += r.count

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
