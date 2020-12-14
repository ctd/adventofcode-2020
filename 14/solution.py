#!/usr/bin/env python


def apply_mask(val, mask):
    l = len(mask)
    v = [c for c in format(int(val), "b").zfill(l)]
    for i, m in enumerate(mask):
        if m == "X":
            continue
        else:
            v[i] = m
    return int("".join(v), 2)


def apply_mask_v2(val, mask):
    if len(mask) < 1:
        return [""]
    values = apply_mask_v2(val[1:], mask[1:])
    if mask[0] == "0":
        values = [val[0] + v for v in values]
    elif mask[0] == "1":
        values = ["1" + v for v in values]
    elif mask[0] == "X":
        values = [i + v for i in ["0", "1"] for v in values]
    return values


def mad(val, mask):
    v = [c for c in format(int(val), "b").zfill(len(mask))]
    return map(lambda x: int(x, 2), apply_mask_v2(v, mask))


def part1(program):
    mem = dict()
    mask = None
    for inst, val in program:
        if inst == "mask":
            mask = val
        else:
            mem[int(inst[4:-1])] = apply_mask(val, mask)
    return sum(mem.values())


def part2(program):
    mem = dict()
    mask = None
    for inst, val in program:
        if inst == "mask":
            mask = val
        else:
            v = int(val)
            for addr in mad(int(inst[4:-1]), mask):
                mem[addr] = v
    return sum(mem.values())


if __name__ == "__main__":
    program = [l.strip().split(" = ") for l in open("input", "r").readlines()]
    print("Part 1: {}".format(part1(program)))
    print("Part 2: {}".format(part2(program)))
