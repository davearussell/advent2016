#! /usr/bin/python3
import sys

import numpy


def parse_input(path):
    ops = []
    for line in open(path).read().strip().split('\n'):
        args = line.split()
        if args[0] == 'rect':
            x, y = map(int, args[1].split('x'))
            ops.append(('rect', (x, y)))
        else:
            assert args[0] == 'rotate', repr(line)
            axis = args[1]
            idx = int(args[2].split('=')[1])
            n = int(args[4])
            ops.append(('rotate', (axis, idx, n)))
    return ops



def main(input_file):
    ops = parse_input(input_file)
    grid = numpy.zeros([6, 50], dtype=numpy.uint8)
    for op, args in ops:
        if op == 'rect':
            x, y = args
            grid[:y, :x] = 1
        else:
            assert op == 'rotate'
            axis, idx, n = args
            if axis == 'row':
                grid[idx] = numpy.roll(grid[idx], n)
            else:
                assert axis == 'column'
                grid[:, idx] = numpy.roll(grid[:, idx], n)

    print("Part 1:", numpy.sum(grid))

    print("Part 2:")
    display = ''
    for row in grid:
        for cell in row:
            display += ' █'[cell]
        display += '\n'
    print(display)
            
            
            


if __name__ == '__main__':
    main(sys.argv[1])
