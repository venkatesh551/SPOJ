'''
Created on 17-Jun-2015

@author: Venkatesh
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def get_min_sum(lst_a, lst_b):
    lst_a.sort()
    lst_b.sort(reverse=True)
    return sum(p*q for p, q in zip(lst_a, lst_b))


def main():
    while True:
        n = read_int()
        if n == 0:
            return
        lst_a = read_int_list()
        lst_b = read_int_list()
        print get_min_sum(lst_a, lst_b)

if __name__ == '__main__':
    main()
