'''
Created on 17-Jul-2015

@author: Venkatesh
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def get_max(h, a, state, d):
    if h <= 0 or a <= 0:
        return 0
    tup = (h, a)
    if tup in d:
        return d[tup]
    elif state == 0:
        d[tup] = 1 + max(get_max(h-5, a-10, 1, d), get_max(h-20, a+5, 1, d))
    else:
        d[tup] = 1 + get_max(h + 3, a + 2, 0, d)
    return d[tup]


def main():
    tc = read_int()
    for _ in xrange(tc):
        h, a = read_int_list()
        print get_max(h+3, a+2, 0, dict())


if __name__ == '__main__':
    main()
