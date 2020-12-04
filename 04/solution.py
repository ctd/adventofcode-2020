#!/usr/bin/env python

import re

REQUIRED_FIELDS = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")


def parse_batch(b):
    kv_pattern = re.compile("(\S+):(\S+)")
    passports = list()
    pp = dict()
    for l in b:
        if l == "":
            passports.append(pp)
            pp = dict()
        else:
            for f in kv_pattern.findall(l):
                pp[f[0]] = f[1]
    if len(pp.keys()) > 0:
        passports.append(pp)
    return passports


def valid_height(h):
    try:
        m, u = re.findall("(\d+)(cm|in)", h)[0]
    except IndexError:
        return False

    return any(
        ((u == "cm" and 150 <= int(m) <= 193), (u == "in" and 59 <= int(m) <= 76))
    )


def p1_valid(pp):
    return all(k in pp.keys() for k in REQUIRED_FIELDS)


def p2_valid(pp):
    try:
        return all(
            (
                1920 <= int(pp["byr"]) <= 2002,
                2010 <= int(pp["iyr"]) <= 2020,
                2020 <= int(pp["eyr"]) <= 2030,
                valid_height(pp["hgt"]),
                re.match("^#[0-9a-f]{6}$", pp["hcl"]),
                any(
                    c in pp["ecl"]
                    for c in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
                ),
                re.match("^\d{9}$", pp["pid"]),
            )
        )
    except KeyError:
        return False


def part1(batch):
    return sum([p1_valid(pp) for pp in parse_batch(batch)])


def part2(batch):
    return sum([p2_valid(pp) for pp in parse_batch(batch)])


if __name__ == "__main__":
    f = open("input", "r")
    batch = [l.rstrip() for l in f]
    f.close()
    print("Part 1: {}".format(part1(batch)))
    print("Part 2: {}".format(part2(batch)))
