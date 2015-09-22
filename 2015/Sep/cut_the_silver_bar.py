'''
Created on 22-Sep-2015

@author: Venkatesh
'''


def read_int():
    return int(raw_input())


def main():
    while True:
        n = read_int()
        if n == 0:
            return
        cnt = 0
        while n > 1:
            n /= 2
            cnt += 1
        print cnt


if __name__ == '__main__':
    main()
