#!/usr/bin/env python

import math


def count_trees(m, start_x, start_y, step_x, step_y):
    x = start_x + step_x
    y = start_y + step_y
    trees = 0
    while y < len(m):
        trees += getpos(m, x, y) == "#"
        x += step_x
        y += step_y
    return trees


def getpos(m, x, y):
    return m[y][x % len(m[y])]


def part1(m):
    return count_trees(m, 0, 0, 3, 1)


def part2(m):
    return math.prod(
        (
            count_trees(m, 0, 0, 1, 1),
            count_trees(m, 0, 0, 3, 1),
            count_trees(m, 0, 0, 5, 1),
            count_trees(m, 0, 0, 7, 1),
            count_trees(m, 0, 0, 1, 2),
        )
    )


if __name__ == "__main__":
    f = open("input", "r")
    m = [l.rstrip() for l in f]
    f.close()
    print("Part 1: {}".format(part1(m)))
    print("Part 2: {}".format(part2(m)))
