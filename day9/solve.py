#! /usr/bin/python3
import sys


def get_length(compressed, recurse=False):
    i = 0
    length = 0
    while i < len(compressed):
        if compressed[i] == '(':
            j = compressed.index(')', i)
            marker = compressed[i + 1 : j]
            n_chars, count = map(int, marker.split('x'))
            if recurse:
                substring = compressed[j + 1 : j + 1 + n_chars]
                substring_length = get_length(substring, True)
            else:
                substring_length = n_chars
            length += substring_length * count
            i = j + n_chars + 1
        else:
            length += 1
            i += 1
    return length


def main(input_file):
    compressed = open(input_file).read().strip()
    print("Part 1:", get_length(compressed, False))
    print("Part 2:", get_length(compressed, True))


if __name__ == '__main__':
    main(sys.argv[1])
