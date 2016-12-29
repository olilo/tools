#!/usr/bin/python3

import sys

def main(argv):
    if len(argv) > 0:
        size = int(argv[0])
    else:
        size = 10

    for i in range(0, size):
        print('*', end='')
    print()

    for i in range(0, size - 2):
        print('*', end='')
        for j in range(0, size - 2):
            print(' ', end='')
        print('*')

    if size > 1:
        for i in range(0, size):
            print('*', end='')
        print()

if __name__ == "__main__":
    main(sys.argv[1:])
