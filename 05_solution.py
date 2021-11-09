import time
simple = False
verbose = 0

if simple:
    data = 'FBFBBFFRLR\nBFFFBBFRRR\nFFFBBBFRRR\nBBFFBBFRLL'.splitlines()
else:
    file = open('05_input.txt', 'r')
    data = file.read().splitlines()


def main():
    start_time = time.time()
    seats = []
    for row in data:
        fb = 128
        lr = 8
        r = c = 0
        if verbose > 0:
            print('{}'.format(row))
        for d in list(row):
            if d in 'FB':
                fb /= 2
                if d == 'B':
                    r += fb
            if d in 'LR':
                lr /= 2
                if d == 'R':
                    c += lr
        rc = int(r * 8 + c)
        seats.append(rc)
        if verbose > 0:
            print('seat id: {} (row {}, col {})'.format(rc, r, c))

    print('max seat id: {}'.format(max(seats)))

    middle_time = time.time()
    print("time elapsed: %s" % (middle_time - start_time))

    seats.sort()
    i = seats[0]
    for j in seats:
        if j > i + 1:
            print('available seat: {}'.format(j-1))
        i = j

    end_time = time.time()
    print("time elapsed: %s" % (end_time - middle_time))


if __name__ == '__main__':
    main()
