'''
Created on 02-Jun-2015

@author: Venkatesh
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def main():
    while True:
        N, D = read_int_list()
        if N == 0 and D == 0:
            return
        print N**D


if __name__ == '__main__':
    main()
