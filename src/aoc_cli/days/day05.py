from __future__ import annotations
from pydantic import BaseModel, ValidationError, Field
from pydantic.dataclasses import dataclass
import dataclasses
from typing import List, Set
import math
from copy import deepcopy

@dataclass
class IngredientIDs():
    min_id: int
    max_id: int
    fresh_ids: Set[int]

    @classmethod
    def from_string(cls, data: str) -> "IngredientIDs":
        min_id = math.inf
        max_id = -math.inf
        fresh_ids = set()
        for row in data.split('\n'):
            start, end = map( (lambda x: int(x)), row.split('-'))
            if start < min_id: min_id = start
            if end > max_id: max_id = end
            fresh_ids |= set(range(start, end+1))
        return cls(min_id, max_id, fresh_ids)
            

def part1(data:str) -> int:
    fresh_ranges, available_ids = data.split('\n\n')
    fresh_ranges = IngredientIDs.from_string(fresh_ranges)
    
    result = 0
    for row in available_ids.split('\n'):
        row = row.strip()
        if not row: continue
        if int(row) in fresh_ranges.fresh_ids:
            result +=1 
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
