# --- Day 10: Adapter Array ---
# https://adventofcode.com/2020/day/10

import time
simple = 0
verbose = 0

if simple == 1:
    data = [int(i) for i in '16\n10\n15\n5\n1\n11\n7\n19\n6\n12\n4'.splitlines()]
elif simple == 2:
    data = [int(i) for i in
            '28\n33\n18\n42\n31\n14\n46\n20\n48\n47\n24\n23\n49\n45\n19\n38\n'
            '39\n11\n1\n32\n25\n35\n8\n17\n7\n9\n4\n2\n34\n10\n3'.splitlines()]
else:
    file = open('10_input.txt', 'r')
    data = [int(i) for i in file.read().splitlines()]


def main():
    start_time = time.time()

    data.sort()
    built_in = 3 + max(data)
    data.append(built_in)
    if verbose > 0:
        print('data: {}'.format(data))

    joltdiff = {'1': 0, '2': 0, '3': 0}
    prev = 0
    for row in data:
        joltdiff[str(row - prev)] += 1
        prev = row
    print('jolt product: {}, max: {}, diff: {}'.format(joltdiff['1'] * joltdiff['3'], max(data), joltdiff))
    # notice how the diff of 2 is never used
    # limiting the branching to the 1 jolts in a row

    middle_time = time.time()
    print("time elapsed: %s" % (middle_time - start_time))

    prev = ones = 0
    branches = 1
    coeff = [1, 1, 2, 4, 7, 11]  # the Lazy Caterer's sequence ? 11 never used in my pyzzle input
    for row in data:
        if row - prev == 1:
            ones += 1
        else:
            if verbose > 1:
                print('previous ones: {}'.format(ones + 1))
            branches *= coeff[ones]
            ones = 0
        prev = row
    print('jolt branches: {}'.format(branches))

    end_time = time.time()
    print("time elapsed: %s" % (end_time - middle_time))


if __name__ == '__main__':
    main()
