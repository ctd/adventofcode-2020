#!/usr/bin/env python


class BoardingPass:
    def __init__(self, seat):
        self.seat = seat

    def row(self):
        return bin_decode(self.seat[:7], "F", "B")

    def col(self):
        return bin_decode(self.seat[7:11], "L", "R")

    def id(self):
        return (self.row() * 8) + self.col()


def bin_decode(sequence, lower_c, upper_c):
    return int(sequence.replace(lower_c, "0").replace(upper_c, "1"), 2)


def part1(passes):
    return max(map(lambda p: p.id(), passes))


def part2(passes):
    ids = set(map(lambda p: p.id(), passes))
    for i in set(range(min(ids), max(ids) + 1)) - ids:
        if all([n in ids for n in (i - 1, i + 1)]):
            return i
    return None


if __name__ == "__main__":
    f = open("input", "r")
    passes = list(map(BoardingPass, [l.rstrip() for l in f]))
    f.close()
    print("Part 1: {}".format(part1(passes)))
    print("Part 2: {}".format(part2(passes)))
