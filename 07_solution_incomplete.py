import time
import re
simple = 0  # 0 = puzzle input, 1 = part one, 2 = part two
verbose = 0

if simple == 1:
    file = open('07_simple1.txt', 'r')
elif simple == 2:
    file = open('07_simple2.txt', 'r')
else:
    file = open('07_input.txt', 'r')
data = file.read().splitlines()


def main():
    start_time = time.time()

    bags = re.compile(r'\d+ (\w+\s\w+) bag', re.IGNORECASE)
    rules = {}
    for row in data:
        a = row.split(' bags contain ')
        rules[a[0]] = bags.findall(a[1])
        if verbose > 2:
            print('{}'.format(row))
        if verbose > 2:
            print('{} {}'.format(a[0], rules[a[0]]))
    if verbose > 1:
        print('{}'.format(rules))

    bag = {'shiny gold'}
    holds = set()
    while bag:
        b = bag.pop()
        if verbose > 1:
            print('searching for \'{}\''.format(b))
        for k, v in rules.items():
            if b in v:
                holds |= {k}
                bag |= {k}
                if verbose > 0:
                    print('found \'{}\' holding {}'.format(k, v))

    print('it can be found in {} bags'.format(len(holds)))
    # only works with simple = 1 or 0

    middle_time = time.time()
    print("time elapsed: %s" % (middle_time - start_time))

    print('second part does NOT work yet!')
    bags = re.compile(r'(\d+) (\w+\s\w+) bag', re.IGNORECASE)
    rules = {}
    for row in data:
        a = row.split(' bags contain ')
        rules[a[0]] = bags.findall(a[1])
        if verbose > 2:
            print('{}'.format(row))
        if verbose > 2:
            print('{} {}'.format(a[0], rules[a[0]]))
    if verbose > 0:
        print('{}'.format(rules))

    bag = {(1, 'shiny gold')}
    stack = ''
    while bag:
        b = bag.pop()
        if verbose > 0:
            print('searching for \'{}\''.format(b[1]))
        for k, v in rules.items():
            if b[1] in k:
                stack += str(b[0]) + '*'
                bag |= set(v)
                if verbose > 0:
                    print('found \'{}\' holding {}'.format(k, v))

    print('it requires {} bags'.format(stack))
    # only works with simple = 2 or 0

    end_time = time.time()
    print("time elapsed: %s" % (end_time - middle_time))


if __name__ == '__main__':
    main()
