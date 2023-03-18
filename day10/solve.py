#! /usr/bin/python3
import sys


def parse_input(path):
    bots = {}
    for line in open(path).read().strip().split('\n'):
        spl = line.split()
        if spl[0] == 'value':
            value = int(spl[1])
            bot_idx = int(spl[5])
            bot = bots.setdefault(bot_idx, {'i': bot_idx, 'chips': []})
            bot['chips'].append(value)
        else:
            assert spl[0] == 'bot'
            bot_idx = int(spl[1])
            lo_type = spl[5]
            lo_idx = int(spl[6])
            hi_type = spl[10]
            hi_idx = int(spl[11])
            bot = bots.setdefault(bot_idx, {'i': bot_idx, 'chips': []})
            bot['lo'] = (lo_type, lo_idx)
            bot['hi'] = (hi_type, hi_idx)
    return bots


def main(input_file):
    bots = parse_input(input_file)

    outputs = {}
    candidates = {bot for bot in bots if len(bots[bot]['chips']) > 1}

    while candidates:
        from_idx = candidates.pop()
        from_bot = bots[from_idx]
        lo, hi = sorted(from_bot['chips'])
        if (lo, hi) == (17, 61):
            print("Part 1:", from_idx)
        from_bot['chips'] = []
        for (dest, to_idx), chip in [(from_bot['lo'], lo), (from_bot['hi'], hi)]:
            if dest == 'output':
                outputs.setdefault(to_idx, []).append(chip)
            else:
                l = bots[to_idx]['chips']
                if l:
                    candidates.add(to_idx)
                l.append(chip)

    print("Part 2:", outputs[0][0] * outputs[1][0] * outputs[2][0])


if __name__ == '__main__':
    main(sys.argv[1])
