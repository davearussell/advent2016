#! /usr/bin/python3
import sys


def parse_size(s):
    assert s.endswith('T'), s
    return int(s[:-1])


def parse_input(path):
    nodes = {}
    for line in open(path):
        if line.startswith('/dev'):
            node, size, used = line.split()[:3]
            _, _x, _y = node.split('-')
            x = int(_x[1:])
            y = int(_y[1:])
            nodes[(x, y)] = {
                'path': (x, y),
                'size': parse_size(size),
                'used': parse_size(used),
            }
    return nodes


def viable_pairs(nodes):
    pairs = set()
    for dst in nodes.values():
        capacity = dst['size'] - dst['used']
        for src in nodes.values():
            if src is not dst and 0 < src['used'] <= capacity:
                pairs.add((src['path'], dst['path']))
    return pairs


def path_length(src, dst, pathable):
    steps = 0
    visited = set()
    frontier = {src}
    while True:
        if dst in frontier:
            return steps
        steps += 1
        new_frontier = set()
        for x, y in frontier:
            new_frontier |= {(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)}
        visited |= frontier
        frontier = (new_frontier & pathable) - visited


def main(input_file):
    nodes = parse_input(input_file)

    pairs = viable_pairs(nodes)
    print("Part 1:", len(pairs))

    pathable = {src for src, dst in pairs}
    free_nodes = {dst for src, dst in pairs}
    assert len(free_nodes) == 1, free_nodes

    free_node = free_nodes.pop()
    goal = (max(x for x, y in nodes), 0)
    target = (0, 0)

    steps = 0
    while goal != target:
        swap_with = (goal[0] - 1, goal[1])
        steps += path_length(free_node, swap_with, pathable - {goal}) + 1
        free_node = goal
        goal = swap_with
    print("Part 2:", steps)


if __name__ == '__main__':
    main(sys.argv[1])
