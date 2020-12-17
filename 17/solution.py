#!/usr/bin/env python

import collections
import copy


def parse_part1(puzzlein):
    z = 0
    d = dict()
    for y, l in enumerate(puzzlein.splitlines()):
        for x, c in enumerate(l.strip()):
            if c == "#":
                d[(z, y, x)] = True
    return d


def parse_part2(puzzlein):
    w = z = 0
    d = dict()
    for y, l in enumerate(puzzlein.splitlines()):
        for x, c in enumerate(l.strip()):
            if c == "#":
                d[(w, z, y, x)] = True
    return d


def neighbours(t, filter_t=True):
    if len(t) == 1:
        return [tuple([t[0] + i]) for i in range(-1, 2)]
    r = [((t[0] + i), *c) for c in neighbours(t[1:], False) for i in range(-1, 2)]
    if filter_t:
        r = list(filter(lambda x: x != t, r))
    return r


def solve(puzzle, cycles=6):
    answer = 0
    p = copy.deepcopy(puzzle)
    for _ in range(cycles):
        np = dict()
        for c in set([n for a in p.keys() for n in neighbours(a, False)]):
            neighboursActive = sum(map(lambda x: x in p.keys(), neighbours(c)))
            if (neighboursActive == 3) or (c in p.keys() and neighboursActive == 2):
                np[c] = True
        answer = len(np.keys())
        p = np
    return answer


def part1(puzzlein):
    return solve(parse_part1(puzzlein))


def part2(puzzlein):
    return solve(parse_part2(puzzlein))


if __name__ == "__main__":
    puzzlein = open("input", "r").read()
    print("Part 1: {}".format(part1(puzzlein)))
    print("Part 2: {}".format(part2(puzzlein)))
