#! /usr/bin/python3
import sys


def parse_input(path):
    ops = []
    for line in open(path).read().strip().split('\n'):
        words = line.split()
        action = words[0]
        if action == 'swap':
            args = words[2], words[5]
            if words[1] == 'letter':
                action = 'swapi'
            else:
                args = tuple(map(int, args))
        elif action == 'move':
            args = int(words[2]), int(words[5])
        elif action == 'rotate':
            if words[1] == 'based':
                action = 'rotatei'
                args = (words[-1],)
            else:
                sign = 1 if words[1] == 'right' else -1
                args = (int(words[2]) * sign,)
        elif action == 'reverse':
            args = int(words[2]), int(words[4])
        else:
            assert 0, action
        ops.append((action, args))
    return ops


def swap(chars, i, j):
    chars[i], chars[j] = chars[j], chars[i]
    return chars


def swapi(chars, a, b):
    i = chars.index(a)
    j = chars.index(b)
    return swap(chars, i, j)


def rotate(chars, n):
    n %= len(chars)
    if not n:
        return chars
    return chars[-n:] + chars[:-n]


def rotatei(chars, x):
    i = chars.index(x)
    n = i + 1 if i < 4 else i + 2
    return rotate(chars, n)


def move(chars, src, dst):
    chars.insert(dst, chars.pop(src))
    return chars


def reverse(chars, lo, hi):
    assert lo <= hi
    if lo == 0:
        swapped = chars[hi :: -1]
    else:
        swapped = chars[hi : lo - 1 : -1]
    return chars[:lo] + swapped + chars[hi + 1:]


ACTION_MAP = {
    'swap': swap,
    'swapi': swapi,
    'rotate': rotate,
    'rotatei': rotatei,
    'move': move,
    'reverse': reverse,
}

REV_ROTATEI = {0: -1, 1: -1, 2: 2, 3: -2, 4: 1, 5: -3, 6: 0, 7: 4}

def scramble(password, ops):
    chars = list(password)
    for action, args in ops:
        chars = ACTION_MAP[action](chars, *args)
    return ''.join(chars)


def unscramble(password, ops):
    chars = list(password)
    for action, args in ops[::-1]:
        if action == 'rotate':
            args = [-args[0]]
        elif action == 'move':
            args = args[::-1]
        elif action == 'rotatei':
            action = 'rotate'
            args = [REV_ROTATEI[chars.index(args[0])]]
        chars = ACTION_MAP[action](chars, *args)
    return ''.join(chars)


def main(input_file):
    ops = parse_input(input_file)
    print("Part 1:", scramble('abcdefgh', ops))
    print("Part 2:", unscramble('fbgdceah', ops))


if __name__ == '__main__':
    main(sys.argv[1])
