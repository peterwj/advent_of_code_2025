from __future__ import annotations
from functools import reduce
import itertools
from dataclasses import dataclass
import dataclasses
from typing import List, Set, Optional
import math
from pprint import pprint

from collections import defaultdict


def _solve(data: str, part: int = 1) -> int:
    rows = data.splitlines()
    manifold_entry = rows[0]
    rest = rows[1:]
    initial_beam_index = manifold_entry.find("S")
    beams = defaultdict(set)
    beams[initial_beam_index].add((initial_beam_index,))
    n_splits = 0
    for row in rest:
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
    if part == 1:
        return n_splits
    else:
        unique_paths = set()
        for _, beam_paths in beams.items():
            for path in beam_paths:
                unique_paths.add(path)
        return len(unique_paths)
    raise ValueError("invalid part")


def solve(part: int, data: str) -> int:
    ans = None
    if part == 1:
        ans = _solve(data)
    elif part == 2:
        ans = _solve(data, part=2)
    else:
        raise ValueError(f"Unsupported part: {part}")
    return ans
