from __future__ import annotations
from pydantic import BaseModel, ValidationError, Field
from pydantic.dataclasses import dataclass
import dataclasses
from typing import Optional
from enum import Enum


@dataclass
class ProductRange:
    start: int
    end: int
    _index: Optional[int]

    def __post_init__(self):
        self._index = self.start

    @classmethod
    def from_string(cls, s: str) -> "ProductRange":
        pairs = s.split("-")
        if len(pairs) != 2:
            raise ValidationError(f"too many minus signs in input {s}")
        return cls(
            start=int(pairs[0]),
            end=int(pairs[1]),
            _index=None,
        )

    def __iter__(self):
        return self

    def __next__(self):
        if self._index <= self.end:
            result = self._index
            self._index += 1
            return result
        else:
            raise StopIteration


def is_valid(pid) -> bool:
    pid_s = str(pid)
    if pid_s[0] == "0":
        raise ValueError(f"Invalidly formatted pid {pid_s}")
    if len(pid_s) % 2 == 1:
        return True
    pid_half_len = len(pid_s) // 2
    if pid_s[0:pid_half_len] == pid_s[pid_half_len:]:
        return False
    return True

def is_repeating_sequence(pid_s, segment):
    '''
    Returns True if segment is composed of pid_s repeated multiple times.
    '''
    if len(pid_s) % len(segment) != 0: return False
    for i in range (len(pid_s) // len(segment)):
        base_idx = i * len(segment)
        if pid_s[base_idx:(base_idx + len(segment))] != segment:
            return False
    return True
        

def is_valid_p2(pid) -> bool:
    pid_s = str(pid)
    if pid_s[0] == "0":
        raise ValueError(f"Invalidly formatted pid {pid_s}")
    for i in range(2, len(pid_s) ):
        if is_repeating_sequence(pid_s, pid_s[i:]):        return False
    return True


def part1(product_ranges) -> int:
    result = 0
    for product_range in product_ranges:
        for product_id in product_range:
            if not is_valid(product_id):
                result += product_id
    return result


def part2(product_ranges) -> int:
    result = 0
    for product_range in product_ranges:
        for product_id in product_range:
            if not is_valid(product_id) or not is_valid_p2(product_id):
                result += product_id
    return result


def solve(part: int, data: str) -> str:
    values = [ProductRange.from_string(datum) for datum in data.strip().split(",")]
    if part == 1:
        ans = part1(values)
    elif part == 2:
        ans = part2(values)
    else:
        raise ValueError(f"Unsupported part: {part}")
    return ans
