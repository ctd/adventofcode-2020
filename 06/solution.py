#!/usr/bin/env python
def answers_in_group(group):
    return set([c for c in group.replace("\n", "")])


def common_answers_in_group(group):
    return common_answers(group.splitlines())


def common_answers(l):
    if len(l) == 1:
        return set(l[0])
    else:
        return set(l[0]) & common_answers(l[1:])


def part1(groups):
    return sum([len(answers_in_group(g)) for g in groups])


def part2(groups):
    return sum([len(common_answers_in_group(g)) for g in groups])


if __name__ == "__main__":
    f = open("input", "r")
    groups = f.read().split("\n\n")
    f.close()
    print("Part 1: {}".format(part1(groups)))
    print("Part 2: {}".format(part2(groups)))
