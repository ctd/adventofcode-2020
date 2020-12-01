#!/usr/bin/env python

import itertools
import math

TARGET_INT = 2020


def part1(intinput):
    for num1 in intinput:
        for num2 in intinput:
            if num1 == num2:
                pass
            if num1 + num2 == TARGET_INT:
                print(num1 * num2)
                return


def part2(intinput, entries=3):
    r = filter(
        lambda x: sum(x) == TARGET_INT, itertools.combinations(intinput, entries)
    )
    for result in r:
        print(math.prod(result))


if __name__ == "__main__":
    f = open("input", "r")
    intinput = list(map(lambda x: int(x), f.readlines()))
    f.close()
    print("Part 1:")
    part1(intinput)
    print("Part 2:")
    part2(intinput)
