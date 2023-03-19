#! /usr/bin/python3
import itertools
import sys


def parse_input(path):
    floors = []
    for line in open(path).read().strip().split('\n'):
        floor = {'generator': [], 'microchip': []}
        body = line.split(' contains ', 1)[1]
        for x in ['and ', 'a ', '.', '-compatible', ',']:
            body = body.replace(x, '')
        words = body.split()
        while words:
            material, obj_type = words[:2]
            words = words[2:]
            if material == 'nothing':
                continue
            floor[obj_type].append(material)
        floors.append(floor)

    materials = sorted([material for floor in floors for material in floor['generator']])
    state = [1] * (len(materials) * 2 + 1)
    for i, floor in enumerate(floors):
        for material in floor['generator']:
            idx = materials.index(material) * 2
            state[idx] = i + 1
        for material in floor['microchip']:
            idx = materials.index(material) * 2 + 1
            state[idx] = i + 1

    return tuple(state)


def dump_state(state):
    n_mats = len(state) // 2
    lines = []
    for floor in range(1, 5):
        line = ['F%d' % (floor), 'E' if floor == state[-1] else '|']
        for i in range(len(state) - 1):
            mat_idx = i // 2
            if state[i] == floor:
                label = chr(ord('a') + mat_idx)
                code = 34 if i & 1 else 31
                symbol = '\x1b[%dm%s\x1b[0m' % (code, label)
            else:
                symbol = '.'
            line.append(symbol)
        lines.insert(0, ' '.join(line))
    print('\n'.join(lines))


def is_safe(objs):
    generator = solo_chip = False
    for obj in objs:
        if obj & 1:
            if obj - 1 not in objs:
                solo_chip = True
        else:
            generator = True
    return not (generator and solo_chip)


def next_states(state):
    floor = state[-1]
    present_objs = [i for i in range(len(state) - 1) if state[i] == floor]
    assert present_objs, state
    candidates = [tuple([obj]) for obj in present_objs]
    if len(present_objs) > 1:
        candidates += itertools.combinations(present_objs, 2)

    for objs in candidates:
        remaining = [obj for obj in present_objs if obj not in objs]
        if not is_safe(remaining):
            continue
        for target in [floor - 1, floor + 1]:
            if not 1 <= target <= 4:
                continue
            at_target = list(objs) + [i for i in range(len(state) - 1) if state[i] == target]
            if is_safe(at_target):
                new_state = list(state)
                new_state[-1] = target
                for obj in objs:
                    new_state[obj] = target
                yield tuple(new_state)


def solve(state):
    goal = tuple(4 for _ in range(len(state)))
    seen = set([state])
    t = 0
    states = set([state])
    while True:
        t += 1
        states = set(ns for s in states for ns in next_states(s)) - seen
        seen |= states
        print("t=%d have %d states" % (t, len(states)))
        if goal in states:
            return t


def main(input_file):
    state = parse_input(input_file)
    print("Part 1:", solve(state))
    new_state = tuple(list(state) + [1, 1, 1, 1])
    print("Part 2:", solve(new_state))


if __name__ == '__main__':
    main(sys.argv[1])
