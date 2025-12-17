from __future__ import annotations
from dataclasses import dataclass
import dataclasses
from typing import List, Set, Optional
import math
from copy import deepcopy
import numpy as np


def part1(data: str) -> int:
    """solve the math problem!"""
    lines = data.strip().split("\n")
    operations = [x for x in lines[-1].split(" ") if x]
    operands = []
    for line in lines[:-1]:
        these_operands = [int(x) for x in line.split(" ") if x]
        operands.append(these_operands)
    operands = np.array(operands).T
    if len(operands) != len(operations):
        raise ValueError("too many or too few operands")
    result = 0
    for row, operation in zip(operands, operations):
        if operation == "*":
            result += row.prod()
        elif operation == "+":
            result += row.sum()
        else:
            raise ValueError(f"invalid operation {operation}")
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
