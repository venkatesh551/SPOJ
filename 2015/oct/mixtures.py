'''
Created on 15-Oct-2015

@author: Venkatesh
'''

import sys


INFINITY = 99999999999999L


def read_int_list():
    return [int(x) for x in raw_input().split()]


def get_min_smoke(colors, n):
    m, c = {}, {}
    for i in xrange(n):
        m[(i, i)] = 0
        c[(i, i)] = colors[i]
    for length in xrange(2, n+1):
        for i in xrange(n-length+1):
            j = i + length - 1
            m[(i, j)] = INFINITY
            c[(i, j)] = INFINITY
            for k in xrange(i, j):
                smoke = m[(i, k)] + m[(k+1, j)] + c[(i, k)] * c[(k+1, j)]
                c[(i, j)] = (c[(i, k)] + c[(k+1, j)]) % 100
                if smoke < m[(i, j)]:
                    m[(i, j)] = smoke
    return m[(0, n-1)]


def get_min_smoke_top_down(colors, i, j, m, c):
    if i == j:
        c[(i, i)] = colors[i]
        m[(i, i)] = 0
    else:
        m[(i, j)] = INFINITY
        for k in xrange(i, j):
            cost = get_min_smoke_top_down(colors, i, k, m, c) + \
                get_min_smoke_top_down(colors, k+1, j, m, c) \
                + c[(i, k)] * c[(k+1, j)]
            c[(i, j)] = (c[(i, k)] + c[(k+1, j)]) % 100
            m[(i, j)] = min(cost, m[(i, j)])
    return m[(i, j)]


def main():
    while True:
        n = sys.stdin.readline()
        if not n:
            return
        else:
            n = int(n)
        nums = read_int_list()
        # print get_min_smoke(nums, n)
        print get_min_smoke_top_down(nums, 0, n-1, dict(), dict())

if __name__ == '__main__':
    main()
