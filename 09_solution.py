import time
import itertools
simple = False
verbose = 0

if simple:
    data = '35\n20\n15\n25\n47\n40\n62\n55\n65\n95\n102\n117\n150\n182\n127\n219\n299\n277\n309\n576'.splitlines()
    data = [int(i) for i in data]
    preamble = 5
else:
    file = open('09_input.txt', 'r')
    data = file.read().splitlines()
    data = [int(i) for i in data]
    preamble = 25


def main():
    start_time = time.time()

    buf = []
    inv = 0
    for row in data:
        if len(buf) <= preamble:
            buf.append(row)
        else:
            buf.append(row)
            i = itertools.combinations(buf, 2)
            if row not in [sum(x) for x in list(i)]:
                inv = row
                break
            del buf[0]
    print('found invalid number: {}'.format(inv))

    middle_time = time.time()
    print("time elapsed: %s" % (middle_time - start_time))

    for length in range(2, 20):
        if verbose > 0:
            print('searching length: {}'.format(length))
        buf = []
        for row in data:
            if len(buf) <= length:
                buf.append(row)
            else:
                buf.append(row)
                if inv == sum(buf):
                    if verbose > 0:
                        print('found list: {}'.format(buf))
                    break
                del buf[0]
        else:
            continue
        break

    print('found smallest: {}, largest: {}, sum: {}'.format(min(buf), max(buf), min(buf) + max(buf)))

    end_time = time.time()
    print("time elapsed: %s" % (end_time - middle_time))


if __name__ == '__main__':
    main()
