'''
Created on 01-Sep-2015

@author: venkatesh

SBANK - Sorting Bank Accounts
'''

from collections import defaultdict


def read_int():
    return int(raw_input())


def print_sorted_acnts(acnts):
    d = defaultdict(int)
    for ele in acnts:
        d[ele] += 1
    for word, count in sorted(d.items()):
        print word, count


def main():
    tc = read_int()
    for _ in xrange(tc):
        n = read_int()
        acnts = [raw_input() for _ in xrange(n)]
        raw_input()  # empty line
        print_sorted_acnts(acnts)

if __name__ == '__main__':
    main()
