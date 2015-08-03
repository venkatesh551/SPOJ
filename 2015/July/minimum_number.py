'''
Created on 23-Jul-2015

@author: Venkatesh
'''


def read_int():
    return int(raw_input())


def min_no_of_digits(n):
    if n % 9 == 0:
        return n/9
    else:
        return n/9 + 1


def main():
    while True:
        n = read_int()
        if n == -1:
            return
        else:
            print min_no_of_digits(n)


if __name__ == '__main__':
    main()
