#! /usr/bin/python3
import sys
import string


def parse_input(path):
    rooms = []
    for line in open(path).read().strip().split('\n'):
        name, rhs = line.rsplit('-', 1)
        sid, xsum = rhs.rstrip(']').split('[')
        rooms.append((name, int(sid), xsum))
    return rooms


def make_xsum(name):
    counts = {}
    for char in name.replace('-', ''):
        counts[char] = counts.get(char, 0) + 1
    letters = list(counts.items())
    letters.sort()
    letters.sort(key=lambda x:-x[1])
    return ''.join(x[0] for x in letters[:5])


def decrypt(text, sid):
    x = string.ascii_lowercase
    encrypted = ''
    for char in text:
        if char == '-':
            encrypted += ' '
        else:
            assert char in x, char
            i = x.index(char)
            encrypted += x[(i + sid) % len(x)]
    return encrypted


def main(input_file):
    rooms = parse_input(input_file)
    real_rooms = [(name, sid) for (name, sid, xsum) in rooms if xsum == make_xsum(name)]
    print("Part 1:", sum(sid for name, sid in real_rooms))

    for name, sid in real_rooms:
        if 'north' in decrypt(name, sid):
            print("Part 2", sid)


if __name__ == '__main__':
    main(sys.argv[1])
