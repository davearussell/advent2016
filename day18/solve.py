#! /usr/bin/python3
import sys


def safe_tiles(row0, height):
    width = len(row0)
    traps = {x for (x, cell) in enumerate(row0) if cell == '^'}
    safe = width - len(traps)
    for y in range(1, height):
        traps = {x for x in range(width)
                 if len(traps & {x - 1, x + 1}) == 1}
        safe += width - len(traps)
    return safe


def main(input_file):
    row0 = open(input_file).read().strip()
    print("Part 1:", safe_tiles(row0, 40))
    print("Part 1:", safe_tiles(row0, 400000))


if __name__ == '__main__':
    main(sys.argv[1])
