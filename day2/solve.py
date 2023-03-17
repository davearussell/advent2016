#! /usr/bin/python3
import sys

OFFSETS = {
    'U': (0, -1),
    'R': (1, 0),
    'D': (0, 1),
    'L': (-1, 0),
}

SANE_KEYPAD = {
    (-1, -1): '1',
    ( 0, -1): '2',
    ( 1, -1): '3',
    (-1,  0): '4',
    ( 0,  0): '5',
    ( 1,  0): '6',
    (-1,  1): '7',
    ( 0,  1): '8',
    ( 1,  1): '9',
}

INSANE_KEYPAD = {
    ( 0, -2): '1',
    (-1, -1): '2',
    ( 0, -1): '3',
    ( 1, -1): '4',
    (-2,  0): '5',
    (-1,  0): '6',
    ( 0,  0): '7',
    ( 1,  0): '8',
    ( 2,  0): '9',
    (-1,  1): 'A',
    ( 0,  1): 'B',
    ( 1,  1): 'C',
    ( 0,  2): 'D',
}


def solve_keypad(instructions, layout):
    pos = [x for x in layout if layout[x] == '5'][0]
    code = ''
    for line in instructions:
        for offset in map(OFFSETS.get, line):
            new_pos = (pos[0] + offset[0], pos[1] + offset[1])
            if new_pos in layout:
                pos = new_pos
        code += layout[pos]
    return code


def main(input_file):
    instructions = open(input_file).read().strip().split('\n')
    print("Part 1:", solve_keypad(instructions, SANE_KEYPAD))
    print("Part 2:", solve_keypad(instructions, INSANE_KEYPAD))


if __name__ == '__main__':
    main(sys.argv[1])
