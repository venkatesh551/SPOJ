'''
Created on 24-Sep-2015

@author: Venkatesh
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def read_str_list(h):
    pass


def main():
    h, w = read_int_list()
    read_str_list(h)

if __name__ == '__main__':
    main()
