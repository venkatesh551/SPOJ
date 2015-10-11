'''
Created on 24-Aug-2015

@author: venkat
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def is_power_of_2(num):
    return num & (num-1) == 0


def get_count(a, b):
    op = 0
    while not is_power_of_2(a) or a > b:
        a /= 2
        op += 1
    while a < b:
        a *= 2
        op += 1
    return op


def main():
    tc = read_int()
    for _ in xrange(tc):
        a, b = read_int_list()
        print get_count(a, b)

if __name__ == '__main__':
    main()
