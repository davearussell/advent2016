#! /usr/bin/python3
import sys


def supports_tls(ip):
    hyper = False
    match = False
    for i in range(len(ip) - 3):
        seq = ip[i : i + 4]
        if seq.endswith('['):
            hyper = True
        elif hyper and seq.startswith(']'):
            hyper = False
        elif seq == seq[::-1] and seq[0] != seq[1]:
            if hyper:
                return False
            match = True
    return match


def supports_ssl(ip):
    hyper = False
    abas = set()
    babs = set()
    for i in range(len(ip) - 2):
        seq = ip[i : i + 3]
        if seq.endswith('['):
            hyper = True
        elif hyper and seq.startswith(']'):
            hyper = False
        elif seq[1] != seq[0] == seq[2]:
            key = seq[:2]
            if hyper:
                key = key[::-1]
            (babs if hyper else abas).add(key)
    return bool(babs & abas)


def main(input_file):
    ips = open(input_file).read().split()
    print("Part 1:", len(list(filter(supports_tls, ips))))
    print("Part 2:", len(list(filter(supports_ssl, ips))))


if __name__ == '__main__':
    main(sys.argv[1])
