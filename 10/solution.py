#!/usr/bin/env python


def arrangements(chain, cache):
    """
    Assumptions - chain is sorted, and values are unique.
    """
    if chain[0] in cache.keys():
        return cache[chain[0]]
    if len(chain) == 1:
        return 1
    c = 0
    i = 1
    while i < len(chain) and (chain[i] - chain[0]) <= 3:
        c += arrangements(chain[i:], cache)
        i += 1
    cache[chain[0]] = c
    return c


def part1(adapters):
    a = sorted(adapters)
    diffs = {a[0]: 1, 3: 1}
    i = 1
    while i < len(a):
        d = a[i] - a[i - 1]
        try:
            diffs[d] += 1
        except KeyError:
            diffs[d] = 1
        i += 1
    return diffs[1] * diffs[3]


def part2(adapters):
    return arrangements(sorted(adapters + [0, max(adapters) + 3]), dict())


if __name__ == "__main__":
    adapters = [int(i) for i in open("input", "r").readlines()]
    print("Part 1: {}".format(part1(adapters)))
    print("Part 2: {}".format(part2(adapters)))
