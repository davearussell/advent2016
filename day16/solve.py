#! /usr/bin/python3
import sys


def fill(s):
    t = str.maketrans({'0': '1', '1': '0'})
    return s + '0' + s[::-1].translate(t)


def xsum(data):
    d = {'00': '1', '01': '0', '10': '0', '11': '1'}
    while not len(data) & 1:
        data = ''.join(d[data[i:i+2]] for i in range(0, len(data), 2))
    return data


def fill_and_xsum(data, length):
    while len(data) < length:
        data = fill(data)
    return xsum(data[:length])


def main(input_file):
    data = open(input_file).read().strip()
    print("Part 1:", fill_and_xsum(data, 272))
    print("Part 2:", fill_and_xsum(data, 35651584))


if __name__ == '__main__':
    main(sys.argv[1])
