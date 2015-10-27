'''
Created on 14-Oct-2015

@author: Venkatesh
'''


def read_lists(n):
    return [read_int_list() for _ in xrange(n)]


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def get_max_amount(inp):
    a = [(ele[1], ele[0], ele[2]) for ele in inp]
    a.sort(key=None)
    


def main():
    tc = read_int()
    for _ in xrange(tc):
        n = read_int()
        print get_max_amount(read_lists(n))


if __name__ == '__main__':
    main()
