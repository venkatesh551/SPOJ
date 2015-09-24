'''
Created on 22-Sep-2015

@author: Venkatesh
'''


def read_int():
    return int(raw_input())


def get_count(n):
    cnt = 0
    while n > 1:
        n /= 2
        cnt += 1
    return cnt


def main():
    while True:
        n = read_int()
        if n == 0:
            return
        else:
            print get_count(n)


if __name__ == '__main__':
    main()
