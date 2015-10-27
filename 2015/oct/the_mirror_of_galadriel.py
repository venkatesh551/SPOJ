'''
Created on 23-Oct-2015

@author: Venkatesh
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def is_magical(s):
    n = len(s)
    substrs = set()
    for L in xrange(2, n+1):
        for k in xrange(n-L+1):
            substrs.add(s[k:k+L])
    for ele in substrs:
        rev_str = ele[::-1]
        if rev_str not in substrs:
            return False
    return True


def main():
    tc = read_int()
    for _ in xrange(tc):
        s = raw_input()
        print "YES" if is_magical(s) else "NO"

if __name__ == '__main__':
    main()
