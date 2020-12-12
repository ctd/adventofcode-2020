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


def follow(instructions, start, waypoint_start):
    x, y = start
    wpx, wpy = waypoint_start
    for inst_d, inst_i in instructions:
        if inst_d in ("L", "R"):
            xm = -1 if inst_d == "R" else 1
            ym = -1 if inst_d == "L" else 1
            for i in range(inst_i // 90):
                wpx, wpy = wpy * ym, wpx * xm
        elif inst_d == "F":
            x += wpx * inst_i
            y += wpy * inst_i
        else:
            dir = Direction[inst_d]
            dm = DirectionMultiplier[dir.name]
            wpx += dm.value[0] * inst_i
            wpy += dm.value[1] * inst_i
    return x, y


def part2(instructions):
    start = (0, 0)
    end = follow(instructions, start, (10, 1))
    assert abs(start[0] - end[0]) + abs(start[1] - end[1]) < 81745
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


if __name__ == "__main__":
    instructions = [
        (d, int(i))
        for d, i in re.findall("([NSEWLRF])(\d+)", open("input", "r").read())
    ]
    print("Part 2: {}".format(part2(instructions)))
