#!/usr/bin/env python

import collections
import copy


class Handheld:
    InstructionSet = collections.namedtuple("InstructionSet", ("inst", "val"))

    def __init__(self):
        self.program = [self.InstructionSet("nop", 0)]

    def load_program_str(self, p):
        self.program = [
            self.InstructionSet(inst, int(val))
            for inst, val in [l.rstrip().split(" ") for l in p]
        ]

    def load_program(self, p):
        self.program = p

    def repair(self):
        tr = {"jmp": "nop", "nop": "jmp"}
        pos = 0
        while pos < len(self.program):
            inst, val = self.program[pos]
            if inst in tr.keys():
                p = copy.deepcopy(self.program)
                p[pos] = self.InstructionSet(tr[inst], val)
                h = Handheld()
                h.load_program(p)
                _, r = h.execute()
                if r:
                    self.program = p
                    return True
            pos += 1
        return False

    def execute(self):
        acc = 0
        pos = 0
        executed = set()
        while all((pos not in executed, pos < len(self.program))):
            inst, val = self.program[pos]
            executed.add(pos)
            if inst == "nop":
                pos += 1
            elif inst == "jmp":
                pos += val
            elif inst == "acc":
                acc += val
                pos += 1
        return acc, pos >= len(self.program)


def part1(p):
    h = Handheld()
    h.load_program_str(p)
    r, _ = h.execute()
    return r


def part2(p):
    h = Handheld()
    h.load_program_str(p)
    h.repair()
    r, _ = h.execute()
    return r


if __name__ == "__main__":
    f = open("input", "r")
    p = f.readlines()
    f.close()
    print("Part 1: {}".format(part1(p)))
    print("Part 2: {}".format(part2(p)))
