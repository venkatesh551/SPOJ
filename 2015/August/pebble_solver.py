'''
Created on 25-Aug-2015

@author: Venkatesh

PEBBLE - Pebble Solver

'''

import sys


def get_min_op(bit_str):
    cnt, flip = 0, False
    for ch in bit_str:
        if flip:
            ch = '1' if ch == '0' else '0'
        if ch == '1':
            flip = not flip
            cnt += 1
    return cnt


def main():
    tc = 0
    while True:
        tc += 1
        line = sys.stdin.readline()
        if not line:
            return
        print "Game #" + str(tc) + ":", get_min_op(line)


if __name__ == '__main__':
    main()
