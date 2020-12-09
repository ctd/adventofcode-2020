#!/usr/bin/env python

import itertools


def valid(i, nums):
    return i in [sum(c) for c in itertools.permutations(nums, 2)]


def part1(nums):
    pre = 25
    for i in range(pre, len(nums)):
        if not valid(nums[i], nums[i - pre : i]):
            return nums[i]


def part2(nums):
    target = part1(nums)
    for x in range(len(nums)):
        for y in range(x, len(nums)):
            if sum(nums[x:y]) == target:
                return sum((min(nums[x:y]), max(nums[x:y])))


if __name__ == "__main__":
    nums = [int(i) for i in open("input", "r").readlines()]
    print("Part 1: {}".format(part1(nums)))
    print("Part 2: {}".format(part2(nums)))
