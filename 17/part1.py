#!/usr/bin/env python
import itertools
import collections
import copy


def parse(puzzlein):
    z = 0
    d = collections.defaultdict(
        lambda: collections.defaultdict(lambda: collections.defaultdict(lambda: False))
    )
    for y, l in enumerate(puzzlein.splitlines()):
        for x, c in enumerate(l.strip()):
            d[z][y][x] = c == "#"
    return d


def print_grid(p):
    minz = min(p.keys())
    maxz = max(p.keys()) + 1
    miny = min([y for zval in p.values() for y in zval.keys()])
    maxy = max([y for zval in p.values() for y in zval.keys()]) + 1
    minx = min([x for zval in p.values() for yval in zval.values() for x in yval])
    maxx = max([x for zval in p.values() for yval in zval.values() for x in yval]) + 1
    for z in range(minz, maxz):
        print(f"z = {z}:")
        for y in range(miny, maxy):
            for x in range(minx, maxx):
                print("#" if p[z][y][x] else ".", end="")
            print()
        print()


def part1(puzzle, cycles=6):
    p = puzzle
    neighbours = set(itertools.combinations([-1, 0, 1] * 3, 3))
    neighbours.discard((0, 0, 0))
    answer = 0
    for _ in range(cycles):
        np = copy.deepcopy(p)
        answer = 0
        minz = min(p.keys()) - 1
        maxz = max(p.keys()) + 2
        miny = min([y for zval in p.values() for y in zval.keys()]) - 1
        maxy = max([y for zval in p.values() for y in zval.keys()]) + 2
        minx = (
            min([x for zval in p.values() for yval in zval.values() for x in yval]) - 1
        )
        maxx = (
            max([x for zval in p.values() for yval in zval.values() for x in yval]) + 2
        )
        for z in range(minz, maxz):
            for y in range(miny, maxy):
                for x in range(minx, maxx):
                    neighboursActive = 0
                    for o in neighbours:
                        neighboursActive += p[z + o[0]][y + o[1]][x + o[2]]
                    if neighboursActive == 3:
                        np[z][y][x] = True
                    elif p[z][y][x] is True and neighboursActive == 2:
                        np[z][y][x] = True
                    else:
                        np[z][y][x] = False
                    answer += np[z][y][x]
        p = np
    return answer


if __name__ == "__main__":
    puzzlein = open("input", "r").read()
    puzzle = parse(puzzlein)
    print("Part 1: {}".format(part1(puzzle)))
