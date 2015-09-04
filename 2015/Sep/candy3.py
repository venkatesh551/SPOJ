'''
Created on 02-Sep-2015

@author: Venkatesh

CANDY3 - Candy III
'''


def read_int():
    return int(raw_input())


def read_int_list(n):
    return [read_int() for _ in xrange(n)]


def main():
    tc = read_int()
    for _ in xrange(tc):
        raw_input()  # empty line
        n = read_int()
        nums_lst = read_int_list(n)
        print "YES" if sum(nums_lst) % n == 0 else "NO"


if __name__ == '__main__':
    main()
