# --- Day 6: Custom Customs ---
# https://adventofcode.com/2020/day/6

import time
import string
simple = False
verbose = 0

if simple:
    file = open('06_simple.txt', 'r')  # make sure it ends in a blank line
    data = file.read().splitlines()
else:
    file = open('06_input.txt', 'r')  # make sure it ends in a blank line
    data = file.read().splitlines()


def main():
    start_time = time.time()

    g1 = set()
    g2 = set(list(string.ascii_lowercase))
    c1 = c2 = 0
    for row in data:
        if len(row) > 0:
            g1 |= set(list(row))
            g2 &= set(list(row))
        else:
            c1 += len(g1)
            c2 += len(g2)
            if verbose > 0:
                print('{}'.format(len(g1)))
                print('{}'.format(len(g2)))
            g1.clear()
            g2 = set(list(string.ascii_lowercase))

    print('part one: {}, part two: {}'.format(c1, c2))

    middle_time = time.time()
    print("time elapsed: %s" % (middle_time - start_time))

    end_time = time.time()
    print("time elapsed: %s" % (end_time - middle_time))


if __name__ == '__main__':
    main()
