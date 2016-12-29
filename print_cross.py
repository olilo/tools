#!/usr/bin/python3

import sys
import time

def build_line(current, size, repeat):
    line = ''
    while repeat > 0:
        for i in range(0, current):
            line += ' '
        line += '*'
        for i in range(current, 2 * size - current - 1):
            line += ' '
        if not (repeat > 1 and current == 0) and current < size:
            line += '*'
        for i in range(2 * size - current, 2 * size - 1):
            line += ' '
        repeat -= 1
    return line


def main(argv):
    if len(argv) > 0:
        size = int(argv[0])
    else:
        size = 10

    if len(argv) > 1:
        repeat = int(argv[1])
    else:
        repeat = 1

    current = 0
    current_increasing = True

    while True:
        print(build_line(current, size, repeat))

        if current_increasing:
            current += 1
            if current == size:
                current_increasing = False
        else:
            current -= 1
            if current == 0:
                current_increasing = True

        time.sleep(0.03)

if __name__ == "__main__":
    main(sys.argv[1:])
