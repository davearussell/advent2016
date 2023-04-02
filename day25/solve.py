#! /usr/bin/python3
import sys

"""
cpy a d
cpy 4 c
  cpy 643 b
    inc d
    dec b
    jnz b -2
  dec c
  jnz c -5
cpy d a
jnz 0 0
cpy a b
cpy 0 a
  cpy 2 c
    jnz b 2
    jnz 1 6
    dec b
    dec c
    jnz c -4
  inc a
  jnz 1 -7
cpy 2 b
  jnz c 2
  jnz 1 4
  dec b
  dec c
  jnz 1 -4
jnz 0 0
out b
jnz a -19   # cpy a d
jnz 1 -21   # jnz c -5


This decompiles to:

d = a + 643 * 4
while True:
  a = d
  while a:
    OUT a % 2
    a //= 2

We want a sequence of numbers that when repeatedly divided by 2, alternate remainder 0/1.
Working up from 1:  
  1   2    5    10    21    42   85    170   341   682    1365   2730
Initial value for the register should thus be 2730 - 643 * 4 = 158
"""


def main(input_file):
    print("Part 1:", 158)
    pass


if __name__ == '__main__':
    main(sys.argv[1])
