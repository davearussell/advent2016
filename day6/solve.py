#! /usr/bin/python3
import sys


def main(input_file):
    messages = open(input_file).read().split()
    print(len(messages), len(messages[0]))

    freqs = {}
    for message in messages:
        for i, char in enumerate(message):
            freqs.setdefault(i, {}).setdefault(char, 0)
            freqs[i][char] += 1

    part1 = part2 = ''
    for i, char_freqs in sorted(freqs.items()):
        part1 += max(char_freqs, key=char_freqs.get)
        part2 += min(char_freqs, key=char_freqs.get)

    print("Part 1:", part1)
    print("Part 1:", part2)


if __name__ == '__main__':
    main(sys.argv[1])
