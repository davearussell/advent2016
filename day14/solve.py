#! /usr/bin/python3
import hashlib
import sys


def find_repeat(md5, count, target_char=None):
    c = target_char
    n = 0 if target_char else 1
    for char in md5:
        if char == c:
            n += 1
            if n == count:
                return char
        else:
            if not target_char:
                c = char
            n = 0 if target_char else 1
    return None


def make_hash(salt, n, stretch=0):
    x = hashlib.md5(b'%s%d' % (salt, n)).hexdigest()
    for i  in range(stretch):
        x = hashlib.md5(x.encode()).hexdigest()
    return x


def find_keys(salt, n, stretch):
    keys = []
    hashes = []
    i = 0
    while len(keys) < n:
        if len(hashes) == i:
            hashes.append(make_hash(salt, i, stretch))
        char = find_repeat(hashes[i], 3)
        if char:
            for j in range(i + 1, i + 1001):
                if len(hashes) == j:
                    hashes.append(make_hash(salt, j, stretch))
                if find_repeat(hashes[j], 5, char):
                    keys.append(i)
                    break
        i += 1
    return keys[-1]


def main(input_file):
    salt = open(input_file).read().strip().encode()
    print("Part 1:", find_keys(salt, 64, 0))
    print("Part 2:", find_keys(salt, 64, 2016))


if __name__ == '__main__':
    main(sys.argv[1])
