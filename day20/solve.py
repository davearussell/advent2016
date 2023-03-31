#! /usr/bin/python3
import sys


def parse_input(path):
    blacklist = []
    for line in open(path).read().strip().split('\n'):
        lo, hi = map(int, line.split('-'))
        blacklist.append([lo, hi])
    return merge_ranges(sorted(blacklist))


def merge_ranges(blacklist):
    merged = blacklist[:1]
    for lo, hi in blacklist[1:]:
        m = merged[-1][-1]
        if lo >= m + 2:
            merged.append([lo, hi])
        elif hi > m:
            merged[-1][-1] = hi
    return merged


def first_allowed_ip(blacklist):
    lo, hi = blacklist[0]
    return 0 if lo > 0 else hi + 1


def count_allowed_ips(blacklist):
    return (1 << 32) - sum(hi - lo + 1 for lo, hi in blacklist)


def main(input_file):
    blacklist = parse_input(input_file)
    print("Part 1:", first_allowed_ip(blacklist))
    print("Part 2:", count_allowed_ips(blacklist))


if __name__ == '__main__':
    main(sys.argv[1])
