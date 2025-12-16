from __future__ import annotations
from pydantic import BaseModel, ValidationError, Field
from pydantic.dataclasses import dataclass
import dataclasses
from typing import List


@dataclass
class BatteryBank:
    batteries: List[str]

    @classmethod
    def from_string(cls, s: str) -> "BatteryBank":
        return cls([(d) for d in s])

    @property
    def max_voltage_for_2(self) -> int:
        return self.max_voltage_for_n(2)

    #        max_voltage = 0
    #        for i, b1 in enumerate(self.batteries):
    #            for j, b2 in enumerate(self.batteries):
    #                if i >= j:
    #                    continue
    #                voltage = int(b1 + b2)
    #                if voltage > max_voltage:
    #                    max_voltage = voltage
    #        return max_voltage

    def max_voltage_for_n_bitvector(
        self, n: int, i_min: Optional[int] = None, i_max: Optional[int] = None
    ) -> List[bool]:
        if n == 1:
            max_idx = 0
            for i, b in enumerate(self.batteries):
                if int(b) > int(self.batteries[max_idx]):
                    max_idx = i
            result = [False] * len(self.batteries)
            result[max_idx] = True
            return result

        bv = self.max_voltage_for_n_bitvector(n - 1)
        # now we turn on one battery in each "span" of off batteries and find the one that is the max
        max_value = 0
        result = None
        for i, on in enumerate(bv):
            if on:
                continue
            bv[i] = True
            voltage = self._voltage_for_bitvector(bv)
            if voltage  > max_value:
                max_value = voltage
                result = [x for x in bv] # deep copy
            bv[i] = False
        return result

    def _voltage_for_bitvector(self, bv: List[bool]) -> int:
        result = ""
        for i, b in enumerate(bv):
            if b:
                result += self.batteries[i]
        return int(result)

    def max_voltage_for_n(self, n: int) -> int:
        bv = self.max_voltage_for_n_bitvector(n)
        assert n == len([x for x in bv if x])
        return self._voltage_for_bitvector(bv)


def part0(banks: List[BatteryBank]) -> int:
    return sum(bank.max_voltage_for_n(1) for bank in banks)


def part1(banks: List[BatteryBank]) -> int:
    print('meow2',[bank.max_voltage_for_2 for bank in banks])
    return sum(bank.max_voltage_for_2 for bank in banks)


def part2(banks: List[BatteryBank]):
    pass


def solve(part: int, data: str) -> str:
    values = [BatteryBank.from_string(datum) for datum in data.strip().split("\n")]
    if part == 0:
        ans = part0(values)
    elif part == 1:
        ans = part1(values)
    elif part == 2:
        ans = part2(values)
    else:
        raise ValueError(f"Unsupported part: {part}")
    return ans
