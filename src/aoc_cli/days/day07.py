from __future__ import annotations
from functools import reduce
import itertools
from dataclasses import dataclass
import dataclasses
from typing import List, Set, Optional
import math
from copy import deepcopy
import numpy as np


def part1(data: str) -> int:
    rows = data.splitlines()
    manifold_entry = rows[0]
    rest = rows[1:]
    initial_beam_index = manifold_entry.find("S")
    beams = set([initial_beam_index])
    result = 0
    for row in rest:
        new_beams = set()
        for beam in beams:
            if row[beam] == ".":
                new_beams.add(beam)
            elif row[beam] == "^":
                result += 1
                new_beams.add(beam - 1)
                new_beams.add(beam + 1)
            else:
                raise ValueError(f"invalid value {row[beam]}")
        beams = new_beams
    return result


def part2(data: str) -> int:
    pass


def solve(part: int, data: str) -> int:
    ans = None
    if part == 1:
        ans = part1(data)
    elif part == 2:
        ans = part2(data)
    else:
        raise ValueError(f"Unsupported part: {part}")
    return ans
