'''
Created on 22-Sep-2015

@author: Venkatesh
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def get_direction(x, y):
    if x <= y:
        return 'L' if x % 2 == 0 else 'R'
    else:
        return 'U' if y % 2 == 0 else 'D'


def main():
    tc = read_int()
    for _ in xrange(tc):
        x, y = read_int_list()
        print get_direction(x, y)

if __name__ == '__main__':
    main()
