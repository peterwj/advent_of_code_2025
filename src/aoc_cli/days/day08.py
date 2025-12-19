from __future__ import annotations
from functools import reduce
import itertools
import math
from dataclasses import dataclass
import dataclasses
from typing import List, Set, Optional
import math
from pprint import pprint

from collections import defaultdict


@dataclass(frozen=True)
class JunctionBox:
    x: int
    y: int
    z: int

    @classmethod
    def from_s(cls, s: str) -> "JunctionBox":
        return cls(*(int(x) for x in s.split(",")))

    def distance_to(self, other: "JunctionBox") -> float:
        return math.sqrt(
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2
        )


@dataclass
class JunctionBoxCollection:
    all_boxes: List[JunctionBox]
    box_to_network: Mapping[JunctionBox, Set[JunctionBox]]

    @classmethod
    def from_s(cls, rows: List[str]) -> "JunctionBoxCollection":
        all_boxes = [JunctionBox.from_s(s) for s in rows]
        box_to_network = {box: {box} for box in all_boxes}
        return cls(all_boxes, box_to_network)

    def find_closest_unconnected_pair(self) -> Tuple[JunctionBox, JunctionBox]:
        closest_distance = math.inf
        result = None
        for i, b1 in enumerate(self.all_boxes):
            for j, b2 in enumerate(self.all_boxes):
                if i >= j:
                    continue
                distance = b1.distance_to(b2)
                b1_network = self.box_to_network[b1]
                if distance < closest_distance and b2 not in b1_network:
                    result = (b1, b2)
                    closest_distance = distance
        assert result is not None
        return result

    def connect_two_boxes(self, b1: JunctionBox, b2: JunctionBox) -> None:
        b1_net = self.box_to_network[b1]
        b2_net = self.box_to_network[b2]
        for box in b2_net:
            b1_net.add(box)
            self.box_to_network[box] = b1_net


def part1(n_connections: int, jb_data: JunctionBoxCollection) -> int:
    # connect the networks.
    for _ in range(n_connections - 1):
        closest_pair = jb_data.find_closest_unconnected_pair()
        jb_data.connect_two_boxes(*closest_pair)

    # find the three largest.
    all_networks = set()
    for network in jb_data.box_to_network.values():
        all_networks.add(frozenset(network))
    return math.prod(sorted([len(x) for x in all_networks], reverse=True)[0:3])


def solve(part: int, data: str) -> int:
    ans = None
    rows = data.splitlines()
    n_connections = int(rows[0])
    rows = rows[1:]
    jb_data = JunctionBoxCollection.from_s(rows)
    # pprint(jb_data)
    if part == 1:
        ans = part1(n_connections, jb_data)
    elif part == 2:
        ans = part2(data)
    else:
        raise ValueError(f"Unsupported part: {part}")
    return ans
