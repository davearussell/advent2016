#! /usr/bin/python3
import sys


def part1(n):
    l = [(x + 1) % n for x in range(n)]
    x = 0
    while x != l[x]:
        l[x] = l[l[x]]
        x = l[x]
    return x + 1


def part2(n):
    elves = [i + 1 for i in range(n)]
    while len(elves) > 1:
        rem = len(elves) % 6
        m = len(elves) // 2
        if rem == 0:
            elves = elves[2 :: 3]
        elif rem == 1:
            elves = elves[: m : 3] + [elves[m - 1]] + elves[m + 1 :: 3]
        elif rem == 2:
            elves = elves[1: m : 3] + [elves[m - 1]] + elves[m + 2 :: 3]
        elif rem == 3:
            elves = elves[2 : m : 3] + elves[m + 1 :: 3]
        elif rem == 4:
            elves = elves[: m : 3] + [elves[m - 1]] + elves[m + 2 :: 3]
        elif rem == 5:
            elves = elves[1 : m : 3] + elves[m + 1 :: 3]
        else:
            assert 0, rem
    return elves[0]


def main(input_file):
    n = int(open(input_file).read())
    print("Part 1:", part1(n))
    print("Part 2:", part2(n))

if __name__ == '__main__':
    main(sys.argv[1])
