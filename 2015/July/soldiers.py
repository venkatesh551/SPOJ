'''
SOLDIERS - SOLDIERS

Created on 22-Jul-2015

@author: Venkatesh
'''


def read_long_list():
    return [long(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def max_no_of_soldiers(m, n):
    last_term = m + n - 1
    first_term = last_term - 4 * (last_term/4)
    n = 1 + (last_term - first_term)/4
    return n * (last_term + first_term) / 2


def main():
    tc = read_int()
    for _ in xrange(tc):
        m, n = read_long_list()
        print max_no_of_soldiers(m, n)

if __name__ == '__main__':
    main()
