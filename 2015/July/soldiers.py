'''
SOLDIERS - SOLDIERS

Created on 22-Jul-2015

@author: Venkatesh
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def max_no_of_soldiers(m, n):
    pass


def main():
    tc = read_int()
    for _ in xrange(tc):
        m, n = read_int_list()
        print max_no_of_soldiers(m, n)

if __name__ == '__main__':
    main()
