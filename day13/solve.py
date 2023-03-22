#! /usr/bin/python3
import sys


def is_wall(pos, m):
    x, y = pos
    if x < 0 or y < 0:
        return True
    n = x*x + 3*x + 2*x*y + y + y*y + m
    bits = 0
    while n:
        if n & 1:
            bits += 1
        n >>= 1
    return bits & 1


def path_length(start, goal, m):
    visited = set()
    frontier = {start}
    steps = 1
    while True:
        new_frontier = set()
        for x, y in frontier:
            for pos in {(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)} - visited:
                if not is_wall(pos, m):
                    if pos == goal:
                        return steps
                    new_frontier.add(pos)

        visited |= frontier
        frontier = new_frontier
        steps += 1


def reachable_locations(start, n_steps, m):
    visited = set()
    frontier = {start}
    for i in range(n_steps):
        new_frontier = set()
        for x, y in frontier:
            for pos in {(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)} - visited:
                if not is_wall(pos, m):
                    new_frontier.add(pos)
        visited |= frontier
        frontier = new_frontier
    return len(visited | frontier)
        


def main(input_file):
    m = int(open(input_file).read())
    print("Part 1:", path_length((1, 1), (31, 39), m))
    print("Part 2:", reachable_locations((1, 1), 50, m))


if __name__ == '__main__':
    main(sys.argv[1])
