'''
Created on 13-Aug-2015

@author:  Venkatesh
'''

from collections import defaultdict


def read_int():
    return int(raw_input())


def get_second_row(row, n):
    d = defaultdict(int)
    for ch in row:
        d[ch] += 1
    for key, val in d.iteritems():
        if val == n:
            d.pop(key)
    result = ''
    for ele in row:
        pass

def main():
    n = read_int()
    first_row = raw_input()
    print get_second_row(first_row, n)


if __name__ == '__main__':
    main()
