#!/usr/bin/env python

import re
import enum


@enum.unique
class Direction(enum.Enum):
    N = 0
    E = 90
    S = 180
    W = 270


@enum.unique
class DirectionMultiplier(enum.Enum):
    N = (0, 1)
    E = (1, 0)
    S = (0, -1)
    W = (-1, 0)


def follow(instructions, start):
    facing = Direction.E
    x, y = start
    for inst_d, inst_i in instructions:
        if inst_d == "L":
            facing = Direction((facing.value - inst_i) % 360)
        elif inst_d == "R":
            facing = Direction((facing.value + inst_i) % 360)
        else:
            dir = facing if inst_d == "F" else Direction[inst_d]
            dm = DirectionMultiplier[dir.name]
            x += dm.value[0] * inst_i
            y += dm.value[1] * inst_i
    return x, y


def part1(instructions):
    start = (0, 0)
    end = follow(instructions, start)
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


if __name__ == "__main__":
    instructions = [
        (d, int(i))
        for d, i in re.findall("([NSEWLRF])(\d+)", open("input", "r").read())
    ]
    print("Part 1: {}".format(part1(instructions)))
