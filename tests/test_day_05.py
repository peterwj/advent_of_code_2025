from aoc_cli.days.day05 import Range
import pytest


class TestRange:

    def test_left_range_overlap(self):
        r = Range(1, 3) & Range(2, 4)
        assert r.start == 2
        assert r.end == 3

    def test_right_range_overlap(self):
        r = Range(2, 4) & Range(1, 3)
        assert r.start == 2
        assert r.end == 3

    def test_left_range_bigger_overlap(self):
        r = Range(1, 5) & Range(2, 4)
        assert r.start == 2
        assert r.end == 4

    def test_right_range_bigger_overlap(self):
        r = Range(2, 4) & Range(1, 5)
        assert r.start == 2
        assert r.end == 4

    def test_range_nonoverlap(self):
        assert (Range(1, 3) & Range(4, 5)) is None

    def test_simple_merge(self):
        (merged,) = Range(1, 5).merge(Range(2, 7))
        assert merged.start == 1
        assert merged.end == 7

    def test_nonoverlapping_merge(self):
        m1, m2 = Range(1, 5).merge(Range(6, 7))
        assert m1.start == 1
        assert m1.end == 5
        assert m2.start == 6
        assert m2.end == 7
