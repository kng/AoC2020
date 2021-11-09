import time
simple = False
verbose = 0

if simple:
    file = open('04_simple.txt', 'r')  # make sure it ends in a blank line
    data = file.read().splitlines()
else:
    file = open('04_input.txt', 'r')  # make sure it ends in a blank line
    data = file.read().splitlines()


def main():
    start_time = time.time()
    req = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']  # 'cid'

    pp = ''
    valid = 0
    for row in data:
        if len(row) > 0:
            pp += row + ' '
        else:
            pd = [pi.split(':')[0] for pi in pp.split()]
            if verbose > 1:
                print('{}'.format(pd))
            if all(elem in pd for elem in req):
                valid += 1
            pp = ''
    print('valid: {}'.format(valid))

    middle_time = time.time()
    print("time elapsed: %s" % (middle_time - start_time))

    pp = ''
    ecls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    valid = 0
    score = 0
    for row in data:
        if len(row) > 0:
            pp += row + ' '
        else:
            pd = [pi.split(':') for pi in pp.split()]
            for pdv in pd:
                if verbose > 1:
                    print('{}'.format(pdv))
                if pdv[0] == 'byr' and 1920 <= int(pdv[1]) <= 2002:
                    score += 1
                if pdv[0] == 'iyr' and 2010 <= int(pdv[1]) <= 2020:
                    score += 1
                if pdv[0] == 'eyr' and 2020 <= int(pdv[1]) <= 2030:
                    score += 1
                if pdv[0] == 'hgt':
                    if 'cm' in pdv[1]:
                        if 150 <= int(''.join([i for i in pdv[1] if i.isdigit()])) <= 193:
                            score += 1
                    elif 'in' in pdv[1]:
                        if 59 <= int(''.join([i for i in pdv[1] if i.isdigit()])) <= 76:
                            score += 1
                if pdv[0] == 'hcl' and len(''.join(i for i in pdv[1] if i.isdigit() or i in '#abcdef')) == 7:
                    score += 1
                if pdv[0] == 'ecl' and pdv[1] in ecls:
                    score += 1
                if pdv[0] == 'pid' and len(''.join(i for i in pdv[1] if i.isdigit())) == 9:
                    score += 1
            if score >= 7:
                valid += 1
            if verbose > 0:
                print('{} {}'.format(score, pp))
            score = 0
            pp = ''
    print('valid: {}'.format(valid))

    end_time = time.time()
    print("time elapsed: %s" % (end_time - middle_time))


if __name__ == '__main__':
    main()
