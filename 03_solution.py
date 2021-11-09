import time
simple = False
verbose = 0

if simple:
    data = '..##.......\n#...#...#..\n.#....#..#.\n..#.#...#.#\n.#...##..#.\n' \
           '..#.##.....\n.#.#.#....#\n.#........#\n#.##...#...\n#...##....#\n.#..#...#.#'.splitlines()
else:
    file = open('03_input.txt', 'r')
    data = file.read().splitlines()


def main():
    start_time = time.time()
    dl = len(data[0])
    x = tree = 0

    for row in data:
        if row[x % dl] == '#':
            tree += 1
        if verbose > 0:
            print('{}'.format(row))
        x += 3
    print('part one: {}'.format(tree))

    middle_time = time.time()
    print("time elapsed: %s" % (middle_time - start_time))

    x1 = x2 = x3 = x4 = x5 = y = 0
    t1 = t2 = t3 = t4 = t5 = 0

    for row in data:
        if row[x1 % dl] == '#':
            t1 += 1
        if row[x2 % dl] == '#':
            t2 += 1
        if row[x3 % dl] == '#':
            t3 += 1
        if row[x4 % dl] == '#':
            t4 += 1
        if y % 2 == 0:
            if row[x5 % dl] == '#':
                t5 += 1
            x5 += 1
        if verbose > 0:
            print('{}'.format(row))
        y += 1
        x1 += 1
        x2 += 3
        x3 += 5
        x4 += 7
    trees = t1 * t2 * t3 * t4 * t5
    print('part two: {} from {} {} {} {} {}'.format(trees, t1, t2, t3, t4, t5))

    end_time = time.time()
    print("time elapsed: %s" % (end_time - middle_time))


if __name__ == '__main__':
    main()
