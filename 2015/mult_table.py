'''
Created on 13-Sep-2015

@author: venkat
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def main():
    n, x = read_int_list()
    cnt = 0
    for i in xrange(1, n+1):
        if x % i == 0 and x / i <= n:
            cnt += 1
    print cnt

if __name__ == '__main__':
    main()
