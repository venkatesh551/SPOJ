'''
Created on 20-Sep-2015

@author: venkat
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_lst(n):
    return [read_int() for _ in xrange(n)]


def read_int():
    return int(raw_input())


def main():
    tc = read_int()
    for _ in xrange(tc):
        n, m, D = read_int_list()
        h_lst = read_lst(n)
        val = sum([(x - 1)/D for x in h_lst])
        print "YES" if val >= m else "NO"

if __name__ == '__main__':
    main()
