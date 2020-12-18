#!/usr/bin/env python

import re


def calcop(a, op, b):
    a = int(a)
    b = int(b)
    if op == "+":
        return a + b
    elif op == "*":
        return a * b


def calc(l, part2):
    while True:
        sub = re.search("\([\s\d\+\*\-]+\)", l)
        if sub is None:
            break
        l = l[: sub.start()] + calc(sub.group()[1:-1], part2) + l[sub.end() :]
    eq = l.split(" ")
    while len(eq) > 1:
        i = eq.index("+") - 1 if part2 and "+" in eq else 0
        eq = [*eq[:i], calcop(*eq[i : i + 3]), *eq[i + 3 :]]
    return str(eq[0])


def part1(homework):
    sum = 0
    for l in homework:
        sum += int(calc(l, False))
    return sum


def part2(homework):
    sum = 0
    for l in homework:
        sum += int(calc(l, True))
    return sum


def testpart1():
    print("Testing Part 1: ", end="")
    for i, a in [
        (["1 + 2 * 3 + 4 * 5 + 6"], 71),
        (["1 + (2 * 3) + (4 * (5 + 6))"], 51),
        (["2 * 3 + (4 * 5)"], 26),
        (["5 + (8 * 3 + 9 + 3 * 4 * 3)"], 437),
        (["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"], 12240),
        (["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"], 13632),
    ]:
        assert part1(i) == a
        print(".", end="")
    print()


def testpart2():
    print("Testing Part 2: ", end="")
    for i, a in [
        (["1 + 2 * 3 + 4 * 5 + 6"], 231),
        (["1 + (2 * 3) + (4 * (5 + 6))"], 51),
        (["2 * 3 + (4 * 5)"], 46),
        (["5 + (8 * 3 + 9 + 3 * 4 * 3)"], 1445),
        (["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"], 669060),
        (["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"], 23340),
    ]:
        assert part2(i) == a
        print(".", end="")
    print()


if __name__ == "__main__":
    homework = [l.strip() for l in open("input", "r").readlines()]
    print("Part 1: {}".format(part1(homework)))
    print("Part 2: {}".format(part2(homework)))
