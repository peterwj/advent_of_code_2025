from __future__ import annotations
from functools import reduce
import itertools
from dataclasses import dataclass
import dataclasses
from typing import List, Set, Optional
import math
from pprint import pprint

from collections import defaultdict


def _solve(data: str) -> int:
    rows = data.splitlines()
    manifold_entry = rows[0]
    rest = rows[1:]
    initial_beam_index = manifold_entry.find("S")
    beams = defaultdict(set)
    beams[initial_beam_index].add((initial_beam_index,))
    n_splits = 0
    for row_idx, row in enumerate(rest):
        new_beams = defaultdict(set)
        for beam_idx, beam_paths in beams.items():
            if row[beam_idx] == ".":
                for path in beam_paths:
                    new_beams[beam_idx].add((*path, beam_idx))
            elif row[beam_idx] == "^":
                n_splits += 1
                for path in beam_paths:
                    new_beams[beam_idx + 1].add((*path, beam_idx + 1))
                    new_beams[beam_idx - 1].add((*path, beam_idx - 1))
            else:
                raise ValueError(f"invalid value {row[beam]}")
        beams = new_beams
    return n_splits


def dfs(rows: List[List[str]], row_idx: int, col_idx: int) -> int:
    # travel downwards from our starting index
    n_rows = len(rows)
    result = 0
    for i in range(row_idx, n_rows):
        if rows[i][col_idx] == ".":
            continue
        if rows[i][col_idx] == "^":
            return dfs(rows, i + 1, col_idx - 1) + dfs(rows, i + 1, col_idx + 1)
        raise ValueError("invalid character")
    return 1


def part2(data: str) -> int:
    rows = data.splitlines()
    manifold_entry = rows[0]
    rest = rows[1:]
    initial_beam_index = manifold_entry.find("S")
    return dfs(rest, 0, initial_beam_index)


def solve(part: int, data: str) -> int:
    ans = None
    if part == 1:
        ans = _solve(data)
    elif part == 2:
        ans = part2(data)
    else:
        raise ValueError(f"Unsupported part: {part}")
    return ans
