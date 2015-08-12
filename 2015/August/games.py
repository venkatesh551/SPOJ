'''
Created on 11-Aug-2015

@author:  Venkatesh

GAMES - HOW MANY GAMES

'''

import fractions


def read_list(func):
    return [func(x) for x in raw_input().split()]


def read_val(func):
    return func(raw_input())


def get_min_matches(avg):
    ind = avg.find('.')
    if ind == -1:
        return 1
    else:
        fract_part = avg[ind+1:]
        pwr = len(fract_part)
        denom = 10 ** pwr
        _gcd = fractions.gcd(denom, int(fract_part))
        return denom/_gcd


def main():
    tc = read_val(int)
    for _ in xrange(tc):
        avg = read_val(str)
        print get_min_matches(avg)

if __name__ == '__main__':
    main()
