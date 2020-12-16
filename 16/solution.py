#!/usr/bin/env python

import re
import collections

TicketRule = collections.namedtuple("TicketRule", ["min", "max"])


def parse(puzzlein):
    sections_str = puzzlein.split("\n\n")
    sections = dict()
    for s in sections_str:
        if s.startswith("nearby tickets:") or s.startswith("your ticket:"):
            sections[s[: s.find(":")]] = parse_tickets(s)
        else:
            sections["rules"] = parse_rules(s)
    return sections


def parse_rules(sectionin):
    rules = dict()
    for m in re.findall("\n?([\w\s]+)\: (\d+)-(\d+) or (\d+)-(\d+)", puzzlein):
        r = list()
        for i in range(1, len(m), 2):
            r.append(TicketRule(int(m[i]), int(m[i + 1])))
        rules[m[0]] = r
    return rules


def parse_tickets(sectionin):
    return [[int(i) for i in l.strip().split(",")] for l in sectionin.splitlines()[1:]]


def valid_ticket(ticket, rules):
    for n in ticket:
        if all(map(lambda r: not r.min <= n <= r.max, rules)):
            return False
    return True


def part1(puzzle):
    errors = 0
    rules = [r for rule in puzzle["rules"].values() for r in rule]
    for ticket in puzzle["nearby tickets"]:
        for n in ticket:
            if all(map(lambda r: not r.min <= n <= r.max, rules)):
                errors += n
    return errors


def part2(puzzle):
    fields_possible = dict()
    fields = dict()
    all_rules = [r for rule in puzzle["rules"].values() for r in rule]
    tickets = list(
        filter(lambda t: valid_ticket(t, all_rules), puzzle["nearby tickets"])
    )
    for f in range(len(tickets[0])):
        for r in puzzle["rules"].keys():
            match = True
            for t in tickets:
                if all(map(lambda r: not r.min <= t[f] <= r.max, puzzle["rules"][r])):
                    match = False
                    break
            if match:
                try:
                    fields_possible[r].add(f)
                except KeyError:
                    fields_possible[r] = set([f])
    while max(map(len, fields_possible.values())) > 0:
        for k in fields_possible.keys():
            v = fields_possible[k]
            if len(v) == 1:
                fields[k] = v.pop()
                for s in fields_possible.values():
                    s.discard(fields[k])
    answer = 1
    for f in filter(lambda f: f.startswith("departure"), fields.keys()):
        answer *= puzzle["your ticket"][0][fields[f]]
    return answer


if __name__ == "__main__":
    puzzlein = open("input", "r").read()
    puzzle = parse(puzzlein)
    print("Part 1: {}".format(part1(puzzle)))
    print("Part 2: {}".format(part2(puzzle)))
