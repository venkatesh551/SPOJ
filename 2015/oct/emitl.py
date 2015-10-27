'''
Created on 26-Oct-2015

@author: Venkatesh
'''

from collections import defaultdict


def read_int():
    return int(raw_input())


def is_suffix_and_prefix(s):
    d = defaultdict(int)
    for ch in s:
        d[ch] += 1
    if d['L'] > 1 and d['T'] > 1 and d['I'] > 1 and d['M'] > 1:
        if len(s) == 9 and d['E'] == 1:
            return True
        if d['E'] > 1:
            return True
    return False


def main():
    tc = read_int()
    for _ in xrange(tc):
        s = raw_input()
        print "YES" if is_suffix_and_prefix(s) else "NO"


if __name__ == '__main__':
    main()
