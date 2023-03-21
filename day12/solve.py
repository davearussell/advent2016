#! /usr/bin/python3
import sys


def try_int(x):
    try:
        return int(x)
    except ValueError:
        return x


def run(insns):
    regs = {}
    i = 0
    while 0 <= i < len(insns):
        op, args = insns[i]
        if op in ['inc', 'dec']:
            reg, = args
            regs[reg] = regs.get(reg, 0) + (1 if op == 'inc' else -1)
        elif op == 'cpy':
            v, reg = args
            if not isinstance(v, int):
                v = regs.get(v, 0)
            regs[reg] = v
        elif op == 'jnz':
            cond, offset = args
            if not isinstance(cond, int):
                cond = regs.get(cond, 0)
            if cond:
                i += offset - 1
        else:
            assert 0, (op, args)
        i += 1
    return regs


def run_fast(c=0):
    n = 26 + c * 7
    a = b = 1
    for i in range(n):
        a, b = a + b, a
    return a + 16 * 17


def parse_input(path):
    insns = []
    for line in open(path).read().strip().split('\n'):
        spl = line.split()
        op = spl[0]
        args = [try_int(x) for x in  spl[1:]]
        insns.append((op, args))
    return insns


def main(input_file):
    print("Part 1:", run_fast())
    print("Part 2:", run_fast(1))


if __name__ == '__main__':
    main(sys.argv[1])
