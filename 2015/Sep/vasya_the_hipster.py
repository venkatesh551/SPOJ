'''
Created on 28-Sep-2015

@author: Venkatesh
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def main():
    a, b = read_int_list()
    c = min(a, b)
    print c, (a + b - 2 * c) / 2


if __name__ == '__main__':
    main()
