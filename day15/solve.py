#! /usr/bin/python3
import sys


def parse_input(path):
    discs = []
    for line in open(path).read().strip().split('\n'):
        spl = line.rstrip('.').split()
        discs.append((int(spl[3]), int(spl[-1])))
    return discs


def first_alignment(discs):
    t = 0
    while True:
        for i, (n, s) in enumerate(discs):
            if (s + t + i + 1) % n:
                break
        else:
            return t
        t += 1


def main(input_file):
    discs = parse_input(input_file)
    print("Part 1:", first_alignment(discs))

    discs.append((11, 0))
    print("Part 2:", first_alignment(discs))


if __name__ == '__main__':
    main(sys.argv[1])
