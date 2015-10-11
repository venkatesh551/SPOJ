'''
Created on 11-Oct-2015

@author: venkat
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def get_max_prod(a_lst, b_lst, n):
    a_lst.sort()
    b_lst.sort()
    result = 0
    for idx in xrange(n):
        result += a_lst[idx] * b_lst[idx]
    return result


def main():
    tc = read_int()
    for _ in xrange(tc):
        n = read_int()
        a_lst = read_int_list()
        b_lst = read_int_list()
        print get_max_prod(a_lst, b_lst, n)


if __name__ == '__main__':
    main()
