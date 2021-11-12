# --- Day 12: Rain Risk ---
# https://adventofcode.com/2020/day/12

import time
simple = False
verbose = 1

if simple:
    data = 'F10\nN3\nF7\nR90\nF11'.splitlines()
else:
    file = open('12_input.txt', 'r')
    data = file.read().splitlines()


class Ship(object):
    def __init__(self, d=0, x=0, y=0, m=0, wx=0, wy=0):
        self.dir = d  # 0=N, 1=E, 2=S, 3=W
        self.dirAsc = ['north', 'east', 'south', 'west']
        self.x = x  # +N / -S
        self.wx = wx
        self.y = y  # +E / -W
        self.wy = wy
        self.m = m  # ship mode: 0=part1, 1=part2
        self.validCmd = ['N', 'S', 'E', 'W', 'L', 'R', 'F']

    def reset(self, d=0, x=0, y=0, m=0, wx=0, wy=0):
        self.dir = d
        self.m = m
        self.x = x
        self.wx = wx
        self.y = y
        self.wy = wy

    def command(self, cmd):
        if len(cmd) > 1:
            if cmd[0] in self.validCmd:
                dist = int(cmd[1:])
                if self.m == 0:  # part1
                    if cmd[0] == 'N':
                        self.x += dist
                    elif cmd[0] == 'S':
                        self.x -= dist
                    elif cmd[0] == 'E':
                        self.y += dist
                    elif cmd[0] == 'W':
                        self.y -= dist
                    elif cmd[0] == 'L':
                        self.dir -= int(dist/90)
                        self.dir %= 4
                    elif cmd[0] == 'R':
                        self.dir += int(dist/90)
                        self.dir %= 4
                    elif cmd[0] == 'F':
                        if self.dir == 0:
                            self.x += dist
                        elif self.dir == 1:
                            self.y += dist
                        elif self.dir == 2:
                            self.x -= dist
                        else:
                            self.y -= dist
                else:  # part2
                    if cmd[0] == 'N':
                        self.wx += dist
                    elif cmd[0] == 'S':
                        self.wx -= dist
                    elif cmd[0] == 'E':
                        self.wy += dist
                    elif cmd[0] == 'W':
                        self.wy -= dist
                    elif cmd[0] == 'L':
                        self.dir = -int(dist/90) % 4
                    elif cmd[0] == 'R':  # todo
                        self.dir = int(dist/90) % 4
                    elif cmd[0] == 'F':
                        self.x += dist * self.wx
                        self.y += dist * self.wy
                    if self.dir > 0:
                        if self.dir == 1:  # 90 CW
                            tmp = self.wx
                            self.wx = -self.wy
                            self.wy = tmp
                        elif self.dir == 2:  # 180
                            self.wx = -self.wx
                            self.wy = -self.wy
                        else:  # 90 CCW
                            tmp = self.wx
                            self.wx = self.wy
                            self.wy = -tmp
                        self.dir = 0
            else:
                print('invalid command')
        else:
            print('command too short')

    def print(self):
        if self.m == 0:
            print('Ship position: {} units {}, {} units {}, facing {}'
                  .format(abs(self.y), self.dirAsc[1] if self.y >= 0 else self.dirAsc[3],
                          abs(self.x), self.dirAsc[0] if self.x >= 0 else self.dirAsc[2],
                          self.dirAsc[self.dir]))
        else:
            print('Ship position: {} units {}, {} units {}\n'
                  'Waypoint position: {} units {}, {} units {}'
                  .format(abs(self.y), self.dirAsc[1] if self.y >= 0 else self.dirAsc[3],
                          abs(self.x), self.dirAsc[0] if self.x >= 0 else self.dirAsc[2],
                          abs(self.wy), self.dirAsc[1] if self.wy >= 0 else self.dirAsc[3],
                          abs(self.wx), self.dirAsc[0] if self.wx >= 0 else self.dirAsc[2]))


def main():
    start_time = time.time()

    # part 1
    ship = Ship(d=1)
    for row in data:
        ship.command(row)
        if verbose > 1:
            print('cmd: {}'.format(row))
            ship.print()
    if verbose > 0:
        ship.print()
    print('distance {}'.format(abs(ship.x) + abs(ship.y)))

    middle_time = time.time()
    print("time elapsed: %s" % (middle_time - start_time))

    # part 2
    ship.reset(m=1, wx=1, wy=10)
    for row in data:
        ship.command(row)
        if verbose > 1:
            print('cmd: {}'.format(row))
            ship.print()
    if verbose > 0:
        ship.print()
    print('distance {}'.format(abs(ship.x) + abs(ship.y)))

    end_time = time.time()
    print("time elapsed: %s" % (end_time - middle_time))


if __name__ == '__main__':
    main()
