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
    """solve the math problem!"""
    lines = [line for line in data.split("\n") if line]
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


def part2(data: str) -> int:
    lines = [line for line in data.split("\n") if line]
    char_matrix = [list(line) for line in lines]
    transposed_matrix = [list(row) for row in zip(*char_matrix)]

    # chop up into problems
    problems = [
        list(group)
        for k, group in itertools.groupby(
            transposed_matrix, lambda x: all((y == " " for y in x))
        )
        if not k
    ]

    # solve the problems
    result = 0
    for problem in problems:
        operation = problem[0][-1]
        problem[0][-1] = " "
        operands = [int("".join(operand)) for operand in problem]
        f = None
        if operation == "*":
            base = 1
            f = lambda x, y: x * y
        elif operation == "+":
            base = 0
            f = lambda x, y: x + y
        else:
            raise ValueError()
        op_result = reduce(f, operands, base)
        result += op_result

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
