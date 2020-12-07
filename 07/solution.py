#!/usr/bin/env python

import re


def parse_rule(l):
    return re.findall("^([\w\s]+) bags contain", l)[0], dict(
        [(c, int(q)) for q, c in re.findall("\s(\d+) ([\w\s]+) bags?[,\.]", l)]
    )


def can_contain(colour, target, rules):
    return any(
        [target in rules[colour].keys()]
        + [can_contain(c, target, rules) for c in rules[colour].keys()]
    )


def must_contain(colour, rules):
    return sum(
        (
            sum(rules[colour].values()),
            sum(
                [
                    rules[colour][c] * must_contain(c, rules)
                    for c in rules[colour].keys()
                ]
            ),
        )
    )


def part1(rules):
    return sum([can_contain(c, "shiny gold", rules) for c in rules.keys()])


def part2(rules):
    return must_contain("shiny gold", rules)


if __name__ == "__main__":
    f = open("input", "r")
    rules = dict(map(parse_rule, f.readlines()))
    f.close()
    print("Part 1: {}".format(part1(rules)))
    print("Part 2: {}".format(part2(rules)))
