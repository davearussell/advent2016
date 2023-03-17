#! /usr/bin/python3
import sys


def is_triangle(shape):
    return max(shape) * 2 < sum(shape)


def transpose(shapes):
    new_shapes = []
    while shapes:
        x, shapes = shapes[:3], shapes[3:]
        new_shapes += [[x[i][j] for i in range(3)] for j in range(3)]
    return new_shapes


def main(input_file):
    shapes = [[int(x) for x in line.split()] for line in open(input_file) if line.strip()]
    print("Part 1:", len(list(filter(is_triangle, shapes))))
    new_shapes = transpose(shapes)
    print("Part 1:", len(list(filter(is_triangle, new_shapes))))


if __name__ == '__main__':
    main(sys.argv[1])
