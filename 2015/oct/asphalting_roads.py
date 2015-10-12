'''
Created on 03-Oct-2015

@author: Venkatesh
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def read_all_pairs(n):
    return [read_int_list() for _ in xrange(n*n)]


def print_days(all_pairs, n):
    rows = [0] * (n + 1)
    cols = [0] * (n + 1)
    for idx, ele in enumerate(all_pairs):
        x, y = ele
        if rows[x] == 0 and cols[y] == 0:
            rows[x] = 1
            cols[y] = 1
            print (idx + 1),


def main():
    n = read_int()
    all_pairs = read_all_pairs(n)
    print_days(all_pairs, n)

if __name__ == '__main__':
    main()
