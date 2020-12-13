#!/usr/bin/env python

import numpy

def part1(earliest, busses):
    departures = dict()
    eb = None
    for bus in map(int, filter(lambda c: c != "x", busses)):
        departures[bus] = ((earliest // bus) + (earliest % bus > 0)) * bus
        if eb is None or departures[bus] < departures[eb]:
            eb = bus
    return (departures[eb] - earliest) * eb


def part2(busses):
    b = [(i, int(x)) for i, x in filter(lambda x: x[1] != "x", enumerate(busses))]
    t = b[0][1]
    for i, (wait, bus) in enumerate(b):
        s = numpy.lcm.reduce([x for _, x in b[:i]] or (1,1))
        while (t + wait) % bus != 0:
            t += s
    return t


def testpart2():
    print("Testing part 2: ", end="")
    assert part2(["17", "x", "13", "19"]) == 3417
    print(".", end="")
    assert part2(["67", "7", "59", "61"]) == 754018
    print(".", end="")
    assert part2(["67", "x", "7", "59", "61"]) == 779210
    print(".", end="")
    assert part2(["67", "7", "x", "59", "61"]) == 1261476
    print(".", end="")
    assert part2(["7", "13", "x", "x", "59", "x", "31", "19"]) == 1068781
    print(".", end="")
    assert part2(["1789", "37", "47", "1889"]) == 1202161486
    print(". done.")


if __name__ == "__main__":
    f = open("input", "r")
    earliest = int(f.readline())
    busses = f.readline().strip().split(",")
    f.close()

    print("Part 1: {}".format(part1(earliest, busses)))
    print("Part 2: {}".format(part2(busses)))
