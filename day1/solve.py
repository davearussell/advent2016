#! /usr/bin/python3
import sys

R = {
    (0, -1): (1, 0),
    (1, 0): (0, 1),
    (0, 1): (-1, 0),
    (-1, 0): (0, -1),
}
L = {v: k for (k, v) in R.items()}
TURNS = {'L': L, 'R': R}


def parse_input(path):
    data = open(path).read().strip().split(', ')
    return [(word[0], int(word[1:])) for word in data]


def main(input_file):
    steps = parse_input(input_file)
    pos = (0, 0)
    facing = (0, -1)

    visited = {pos}
    part2 = None
    for turn, distance in steps:
        facing = TURNS[turn][facing]
        for i in range(distance):
            pos = (pos[0] + facing[0], pos[1] + facing[1])
            if pos in visited and part2 is None:
                part2 = sum(map(abs, pos))
            visited.add(pos)

    print("Part 1:", sum(map(abs, pos)))
    print("Part 2:", part2)


if __name__ == '__main__':
    main(sys.argv[1])
