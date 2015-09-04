'''
Created on 02-Sep-2015

@author: Venkatesh

EGYPIZZA - Pizza
'''

from collections import defaultdict


def read_int():
    return int(raw_input())


def read_str_list(n):
    return [raw_input() for _ in xrange(n)]


def get_min_pizza_cnt(inp_lst):
    d = defaultdict(int)
    for ele in inp_lst:
        d[ele] += 1
    req, parts = 1, 0
    for key, val in d.iteritems():
        if key == '1/2':
            req += (val + 1) / 2
            parts += 2 if val % 2 != 0 else 0
        elif key == '3/4':
            req += val
            parts += val
    # print parts, d['1/4']
    need = (d['1/4'] - parts + 3) / 4
    # print need, req
    if need < 0:
        return req
    else:
        return req + need


def main():
    n = read_int()
    inp_lst = read_str_list(n)
    print get_min_pizza_cnt(inp_lst)


if __name__ == '__main__':
    main()
