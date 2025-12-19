from __future__ import annotations

from dataclasses import dataclass

from textwrap import dedent

import pytest

from . import conftest


DAY_1_INPUT = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
""".strip()

DAY_2_INPUT = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
""".strip()

DAY_03_INPUT = """
987654321111111
811111111111119
234234234234278
818181911112111
""".strip()

DAY_04_INPUT = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
""".strip()

DAY_05_INPUT = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
""".strip()

DAY_06_INPUT = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

DAY_07_INPUT = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
""".strip()
DAY_07_INPUT_MINI = """
....S....
.........
....^....
.........
...^.^...
.........
..^.^.^..
.........
.^.^...^.
.........
""".strip()

DAY_08_INPUT = """
10
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
""".strip()


@dataclass
class Example:
    day: int
    part: int
    input_: str
    expected: any


EXAMPLE_CASES: list[dict[str, object]] = [
    Example(day=1, part=1, input_=DAY_1_INPUT, expected=3),
    Example(day=1, part=2, input_=DAY_1_INPUT, expected=6),
    Example(day=1, part=2, input_="R1000", expected=10),
    Example(day=2, part=1, input_=DAY_2_INPUT, expected=1227775554),
    Example(day=2, part=2, input_=DAY_2_INPUT, expected=4174379265),
    Example(day=3, part=0, input_=DAY_03_INPUT, expected=35),
    Example(day=3, part=1, input_=DAY_03_INPUT, expected=357),
    Example(day=3, part=3, input_=DAY_03_INPUT, expected=987 + 819 + 478 + 921),
    Example(day=3, part=4, input_=DAY_03_INPUT, expected=9876 + 8119 + 4478 + 9211),
    Example(day=3, part=2, input_=DAY_03_INPUT, expected=3121910778619),
    Example(day=4, part=1, input_=DAY_04_INPUT, expected=13),
    Example(day=4, part=2, input_=DAY_04_INPUT, expected=43),
    Example(day=5, part=1, input_=DAY_05_INPUT, expected=3),
    Example(day=5, part=2, input_=DAY_05_INPUT, expected=14),
    Example(day=6, part=1, input_=DAY_06_INPUT, expected=4277556),
    Example(day=6, part=2, input_=DAY_06_INPUT, expected=3263827),
    Example(day=7, part=1, input_=DAY_07_INPUT, expected=21),
    Example(day=7, part=2, input_=DAY_07_INPUT, expected=40),
    Example(day=7, part=2, input_=DAY_07_INPUT_MINI, expected=13),
    Example(day=8, part=1, input_=DAY_08_INPUT, expected=40),
    Example(day=8, part=2, input_=DAY_08_INPUT, expected=25272),
]


@pytest.mark.parametrize(
    "case",
    EXAMPLE_CASES,
    ids=lambda case: f"day{case.day:02d}-part{case.part}",
)
def test_examples(case: dict[str, object]) -> None:
    result = conftest.run_solve(
        day=case.day,  # type: ignore[arg-type]
        part=case.part,  # type: ignore[arg-type]
        data=case.input_,  # type: ignore[arg-type]
    )
    assert result == case.expected
