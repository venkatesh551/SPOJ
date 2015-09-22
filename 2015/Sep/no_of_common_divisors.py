'''
Created on 22-Sep-2015

@author: Venkatesh
'''

from fractions import gcd


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def no_of_factors(g):
    factors = 1
    i = 2
    copy_g = g
    while i * i <= copy_g and g > 1:
        pwr = 0
        while g % i == 0:
            g /= i
            pwr += 1
        factors *= (pwr + 1)
        i += 1
    if g > 1:
        factors *= 2
    return factors


def main():
    tc = read_int()
    for _ in xrange(tc):
        a, b = read_int_list()
        print no_of_factors(gcd(a, b))


if __name__ == '__main__':
    main()
