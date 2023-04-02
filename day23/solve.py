#! /usr/bin/python3
import math
import sys

"""
cpy X Y: y = X
jnz X Y: jmp by Y if X

tgl:
  inc -> dec
  dec -> inc
  tgl -> inc
  jnz -> cpy
  cpy -> jnz


cpy a b
dec b
cpy a d
cpy 0 a
  cpy b c
    inc a
    dec c
    jnz c -2
  dec d
  jnz d -5
dec b
cpy b c
cpy c d
  dec d
  inc c
  jnz d -2
tgl c
cpy -16 c
jnz 1 c        # now "cpy 1 c"
cpy 80 c
  jnz 77 d     # now "cpy 77 d"
    inc a
    inc d      # now "dec d"
    jnz d -2
  inc c        # now "dec c"
  jnz c -5


b = a - 1  # 6

a *= b     # 7 * 6
b--        # 5
TGL b * 2  # 10, noop

a *= b     # 210
b--        # 4
TGL b * 2  # 8, "inc c" -> "dec c"

a *= b     # 840
b--        # 3
TGL b * 2  # 6, "inc d" -> "dec d"

a *= b     # 2520
b--        # 2
TGL b * 2  # 4, "jnz 77 d" -> "cpy 77 d"

a *= b     # 5040
b--        # 1
TGL b * 2  # 2, "jnz 1 c" -> "cpy 1 c"

c = 80
d = 77
a += d * c

For all a >= 5, the result is a! + 80 * 77
(I imagine constants will vary between inputs)
"""


def run(a):
    return math.factorial(a) + 80 * 77


def main(input_file):
    print("Part 1:", run(7))
    print("Part 2:", run(12))


if __name__ == '__main__':
    main(sys.argv[1])
