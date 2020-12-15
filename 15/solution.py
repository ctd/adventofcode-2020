#!/usr/bin/env python


def play(starting, limit):
    last = None
    seen = dict()
    for i in range(min(limit, len(starting))):
        n = starting[i]
        try:
            seen[n][-2] = seen[n][-1]
            seen[n][-1] = i
        except KeyError:
            seen[n] = {-1: i}
        last = n
    for i in range(len(starting), limit):
        n = None
        if -2 in seen[last]:
            n = seen[last][-1] - seen[last][-2]
        else:
            n = 0
        try:
            seen[n][-2] = seen[n][-1]
            seen[n][-1] = i
        except KeyError:
            seen[n] = {-1: i}
        last = n
    return last


def part1(starting):
    return play(starting, 2020)


def part2(starting):
    return play(starting, 30000000)


def testpart1():
    print("Part 1 tests: ", end="")
    for i, a in (
        ([0, 3, 6], 436),
        ([1, 3, 2], 1),
        ([2, 1, 3], 10),
        ([1, 2, 3], 27),
        ([2, 3, 1], 78),
        ([3, 2, 1], 438),
        ([3, 1, 2], 1836),
    ):
        assert part1(i) == a
        print(".", end="")
    print(" done.")


def testpart2():
    print("Part 2 tests: ", end="")
    for i, a in (
        ([0, 3, 6], 175594),
        ([1, 3, 2], 2578),
        ([2, 1, 3], 3544142),
        ([1, 2, 3], 261214),
        ([2, 3, 1], 6895259),
        ([3, 2, 1], 18),
        ([3, 1, 2], 362),
    ):
        assert part2(i) == a
        print(".", end="")
    print(" done.")


if __name__ == "__main__":
    starting = [int(i) for i in open("input", "r").read().strip().split(",")]
    print("Part 1: {}".format(part1(starting)))
    print("Part 2: {}".format(part2(starting)))
