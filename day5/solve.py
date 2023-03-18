#! /usr/bin/python3
import hashlib
import sys


def main(input_file):
    input_data = open(input_file).read().strip()

    part1 = 0
    n = 0
    i = 0
    while n < 8:
        key = ('%s%d' % (input_data, i)).encode()
        md5 = int(hashlib.md5(key).hexdigest()[:6], base=16)
        if md5 < 0x10:
            part1 = (part1 << 4) | md5
            n += 1
        i += 1
    print("Part 1:", '%08x' % part1)

    part2 = 0
    mask = 0
    i = 0
    while mask != 0xff:
        key = ('%s%d' % (input_data, i)).encode()
        md5 = int(hashlib.md5(key).hexdigest()[:7], base=16)
        if md5 < 0x100:
            pos = md5 >> 4
            if pos < 8 and not mask & (1 << pos):
                mask |= (1 << pos)
                part2 |= (md5 & 0xf) << (4 * (7 - pos))
        i += 1
    print("Part 2:", '%08x' % part2)


if __name__ == '__main__':
    main(sys.argv[1])
