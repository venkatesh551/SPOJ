'''
Created on 21-Sep-2015

@author: Venkatesh

NSTEPS - Number Steps

'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def main():
    tc = read_int()
    for _ in xrange(tc):
        x, y = read_int_list()
        if x == y or x-2 == y:
            total = x + y
            print total if x % 2 == 0 else total - 1
        else:
            print "No Number"

if __name__ == '__main__':
    main()
