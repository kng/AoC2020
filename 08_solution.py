# --- Day 8: Handheld Halting ---
# https://adventofcode.com/2020/day/8

import time
simple = False
verbose = 0

if simple:
    data = 'nop +0\nacc +1\njmp +4\nacc +3\njmp -3\nacc -99\nacc +1\njmp -4\nacc +6'.splitlines()
else:
    file = open('08_input.txt', 'r')
    data = file.read().splitlines()


def main():
    start_time = time.time()

    valid = ('nop', 'acc', 'jmp')
    prg = []
    for row in data:
        a = row.split(' ')
        if a[0] in valid:
            prg.append([a[0], int(a[1]), 0])
        else:
            print('invalid op {}'.format(a))

    pp = acc = 0
    if simple:
        prg[7][0] = 'nop'
    print('program len {}, code {}'.format(len(prg), prg))
    while 0 <= pp < len(prg):
        if prg[pp][2] > 0:
            print('Stop {}: {} {}'.format(pp, prg[pp][0], prg[pp][1]))
            break
        if verbose > 1:
            print('Exec {}: {} {}'.format(pp, prg[pp][0], prg[pp][1]))
        prg[pp][2] += 1
        if prg[pp][0] == 'acc':
            acc += prg[pp][1]
        elif prg[pp][0] == 'jmp':
            pp += prg[pp][1]
            continue
        pp += 1
        if pp >= len(prg):
            print('Exit')
    print('pp {}, acc {}'.format(pp, acc))
    if simple:  # restore program
        prg[7][0] = 'jmp'

    middle_time = time.time()
    print("time elapsed: %s" % (middle_time - start_time))

    toggle = 0
    while toggle < len(prg):
        # find the next op to swap
        while toggle < len(prg) and prg[toggle][0] == 'acc':
            toggle += 1
        if toggle >= len(prg):
            print('did not find solution')
            break
        if verbose > 0:
            print('toggle {}'.format(toggle))
        if prg[toggle][0] == 'jmp':
            prg[toggle][0] = 'nop'
        else:
            prg[toggle][0] = 'jmp'

        pp = acc = 0
        for p in prg:  # clear execution counter
            p[2] = 0
        if verbose > 1:
            print('program len {}, code {}'.format(len(prg), prg))
        while 0 <= pp < len(prg):
            if prg[pp][2] > 0:
                if verbose > 1:
                    print('Stop {}: {} {}'.format(pp, prg[pp][0], prg[pp][1]))
                break
            if verbose > 1:
                print('Exec {}: {} {}'.format(pp, prg[pp][0], prg[pp][1]))
            prg[pp][2] += 1
            if prg[pp][0] == 'acc':
                acc += prg[pp][1]
            elif prg[pp][0] == 'jmp':
                pp += prg[pp][1]
                continue
            pp += 1
            if pp >= len(prg):
                print('Exit OOB')
        if verbose > 0:
            print('acc {}'.format(acc))
        if pp >= len(prg):
            print('we have a winner: {}'.format(acc))
            break
        # toggle back the op for the next run
        if prg[toggle][0] == 'jmp':
            prg[toggle][0] = 'nop'
        else:
            prg[toggle][0] = 'jmp'
        toggle += 1

    end_time = time.time()
    print("time elapsed: %s" % (end_time - middle_time))


if __name__ == '__main__':
    main()
