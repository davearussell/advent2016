#! /usr/bin/python3
import hashlib
import sys

OFFSETS = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}


def open_doors(path, passcode):
    x = hashlib.md5(b'%s%s' % (passcode, path.encode())).hexdigest()
    for char, step in zip(x, 'UDLR'):
        if char in 'bcdef':
            yield step


def find_paths(passcode):
    pos = (0, 0)
    size = 4
    goal = (size - 1, size - 1)
    paths = {((0, 0), '')}
    shortest = longest = None

    while paths:
        new_paths = set()
        for (x, y), path in paths:
            for step in open_doors(path, passcode):
                dx, dy = OFFSETS[step]
                nx, ny = (x + dx, y + dy)
                new_path = path + step
                if (nx, ny) == goal:
                    if not shortest:
                        shortest = new_path
                    longest = new_path
                elif 0 <= nx < size and 0 <= ny < size:
                    new_paths.add(((nx, ny), new_path))
        paths = new_paths
    return shortest, longest


def main(input_file):
    passcode = open(input_file).read().strip().encode()
    shortest, longest = find_paths(passcode)
    print("Part 1:", shortest)
    print("Part 2:", len(longest))


if __name__ == '__main__':
    main(sys.argv[1])
