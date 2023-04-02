#! /usr/bin/python3
import itertools
import sys


def parse_input(path):
    grid = set()
    waypoints = {}
    for y, line in enumerate(open(path)):
        for x, char in enumerate(line):
            if char != '#':
                grid.add((x, y))
                if char.isdigit():
                    waypoints[int(char)] = (x, y)
    return grid, waypoints


def path_length(grid, src, dst):
    steps = 0
    visited = set()
    frontier = {src}
    while True:
        assert frontier
        if dst in frontier:
            return steps
        new_frontier = set()
        for x, y in frontier:
            new_frontier |= {(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)}
        visited |= frontier
        frontier = (new_frontier & grid) - visited
        steps += 1


def compute_distances(grid, waypoints):
    distances = {}
    labels = sorted(waypoints)
    for i, src in enumerate(labels):
        for dst in labels[i+1:]:
            distance = path_length(grid, waypoints[src], waypoints[dst])
            distances[(src, dst)] = distances[(dst, src)] = distance
    return distances


def path_distance(distances, order):
    cost = 0
    for src, dst in zip(order, order[1:]):
        cost += distances[(src, dst)]
    return cost


def shortest_path(distances, return_home=False):
    n = max(a for a, b in distances)
    paths = [[0] + list(order)
             for order in itertools.permutations(range(1, n + 1))]
    if return_home:
        paths = [path + [0] for path in paths]
    costs = [path_distance(distances, path) for path in paths]
    return min(costs)


def main(input_file):
    grid, waypoints = parse_input(input_file)
    distances = compute_distances(grid, waypoints)
    print("Part 1:", shortest_path(distances, False))
    print("Part 2:", shortest_path(distances, True))


if __name__ == '__main__':
    main(sys.argv[1])
