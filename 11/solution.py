#!/usr/bin/env python

import enum
import collections
import copy
import itertools


Coordinate = collections.namedtuple("Coordinate", ["x", "y"])


@enum.unique
class Legend(enum.Enum):
    EMPTY = "L"
    OCCUPIED = "#"
    FLOOR = "."


STEPS = [
    step
    for step in filter(
        lambda x: x != (0, 0),
        [Coordinate(x, y) for x in range(-1, 2) for y in range(-1, 2)],
    )
]


def seats_occupied(seats, depth, occupied_tolerance):
    cur = seats
    prev = None
    while cur != prev:
        prev = cur
        cur = sit(prev, depth, occupied_tolerance)
    return sum(map(lambda c: c == Legend.OCCUPIED, itertools.chain(*cur)))


def sit(seats, depth, occupied_tolerance):
    s = copy.deepcopy(seats)
    for y in range(len(s)):
        for x in range(len(s[y])):
            if (
                seats[y][x] == Legend.EMPTY
                and qty_visible(seats, Coordinate(x, y), depth) == 0
            ):
                s[y][x] = Legend.OCCUPIED
            elif (
                seats[y][x] == Legend.OCCUPIED
                and qty_visible(seats, Coordinate(x, y), depth) >= occupied_tolerance
            ):
                s[y][x] = Legend.EMPTY
    return s


def qty_visible(seats, coordinate, depth):
    return sum([visible(seats, coordinate, step, depth) for step in STEPS])


def visible(seats, coordinate, step, depth):
    c = Coordinate(coordinate.x + step.x, coordinate.y + step.y)
    if not (depth != 0 and 0 <= c.y < len(seats) and 0 <= c.x < len(seats[c.y])):
        return False
    if seats[c.y][c.x] == Legend.OCCUPIED:
        return True
    if seats[c.y][c.x] == Legend.EMPTY:
        return False
    return visible(seats, c, step, depth - 1)


def part1(seats):
    return seats_occupied(seats, 1, 4)


def part2(seats):
    return seats_occupied(seats, -1, 5)


if __name__ == "__main__":
    seats = [[Legend(c) for c in l.strip()] for l in open("input", "r").readlines()]
    print("Part 1: {}".format(part1(seats)))
    print("Part 2: {}".format(part2(seats)))
