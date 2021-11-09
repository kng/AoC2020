import time
simple = False
verbose = 1

if simple:
    data = '1721\n979\n366\n299\n675\n1456'.splitlines()
else:
    file = open('01_input.txt', 'r')
    data = file.read().splitlines()


def main():
    start_time = time.time()
    for i in data:
        for j in data:
            if int(i) + int(j) == 2020:
                print('{}'.format(int(i) * int(j)))

    middle_time = time.time()
    print("time elapsed: %s" % (middle_time - start_time))

    for i in data:
        for j in data:
            for k in data:
                if int(i) + int(j) + int(k) == 2020:
                    print('{}'.format(int(i) * int(j) * int(k)))

    end_time = time.time()
    print("time elapsed: %s" % (end_time - middle_time))


if __name__ == '__main__':
    main()
