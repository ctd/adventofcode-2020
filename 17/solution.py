#!/usr/bin/env python

import collections
import copy
import functools


def parse(puzzlein, pad):
    padding = tuple([0] * pad)
    d = dict()
    for y, l in enumerate(puzzlein.splitlines()):
        for x, c in enumerate(l.strip()):
            if c == "#":
                d[(*padding, y, x)] = True
    return d


@functools.lru_cache(maxsize=None)
def neighbours(t, filter_t=True):
    if len(t) == 1:
        return [tuple([t[0] + i]) for i in range(-1, 2)]
    r = [((t[0] + i), *c) for c in neighbours(t[1:], False) for i in range(-1, 2)]
    if filter_t:
        r = list(filter(lambda x: x != t, r))
    return r


def solve(puzzle, cycles=6):
    p = puzzle
    for _ in range(cycles):
        np = dict()
        for c in set([n for a in p.keys() for n in neighbours(a, False)]):
            neighboursActive = sum(map(lambda x: p.get(x, False), neighbours(c)))
            if (neighboursActive == 3) or (p.get(c, False) and neighboursActive == 2):
                np[c] = True
        p = np
    return len(p.keys())


def part1(puzzlein):
    return solve(parse(puzzlein, 1))


def part2(puzzlein):
    return solve(parse(puzzlein, 2))


if __name__ == "__main__":
    puzzlein = open("input", "r").read()
    print("Part 1: {}".format(part1(puzzlein)))
    print("Part 2: {}".format(part2(puzzlein)))
