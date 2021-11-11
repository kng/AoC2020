# --- Day 2: Password Philosophy ---
# https://adventofcode.com/2020/day/2

import time
import re
simple = False
verbose = 0

if simple:
    data = '1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc'.splitlines()
else:
    file = open('02_input.txt', 'r')
    data = file.read().splitlines()

p = re.compile(r'^(\d+)-(\d+) (\w): (\w*)$')


def main():
    start_time = time.time()
    validpass = 0
    for row in data:
        a = p.split(row)
        c = a[4].count(a[3])
        r = (int(a[1]) <= c <= int(a[2]))
        if r:
            validpass += 1
        if verbose > 0:
            print('testing if {} contains {} to {} of {} ({}) = {}'.format(a[4], a[1], a[2], a[3], c, r))

    print('part 1: valid passwords = {}'.format(validpass))
    middle_time = time.time()
    print("time elapsed: %s" % (middle_time - start_time))

    validpass = 0
    for row in data:
        (a, pos1, pos2, policy, pwd, b) = p.split(row)
        pos1 = int(pos1) - 1
        pos2 = int(pos2) - 1
        i = 0
        if pos1 < len(pwd):
            if pwd[pos1] == policy:
                i += 1
        if pos2 < len(pwd):
            if pwd[pos2] == policy:
                i += 1
        if i == 1:
            validpass += 1
        if verbose > 0:
            print('testing if {} has {} at positions, {} {} = {}'.format(pwd, policy, pos1, pos2, i))

    print('part 2: valid passwords = {}'.format(validpass))

    end_time = time.time()
    print("time elapsed: %s" % (end_time - middle_time))


if __name__ == '__main__':
    main()
