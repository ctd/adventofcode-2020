#!/usr/bin/env python
import re


class Password:
    def __init__(self, password, policies):
        self.password = password
        self.policies = policies

    def valid(self):
        for p in self.policies:
            if p.valid(self.password) is False:
                return False
        return True


class PasswordPolicy:
    def __init__(self, character, minimum, maximum):
        self.character = character
        self.minimum = minimum
        self.maximum = maximum

    def valid(self, password):
        return self.maximum >= len(re.findall(self.character, password)) >= self.minimum


def parse_passwords(lines):
    passwords = []
    matcher = re.compile("^(\d+)-(\d+) (\w): (\w+)")
    for l in lines:
        m = matcher.findall(l)[0]
        passwords.append(Password(m[3], [PasswordPolicy(m[2], int(m[0]), int(m[1]))]))
    return passwords


def part1(passwords):
    return len(list(filter(lambda x: x.valid(), passwords)))


if __name__ == "__main__":
    f = open("input", "r")
    passwords = parse_passwords(f.readlines())
    f.close()
    print("Part 1: {}".format(part1(passwords)))
