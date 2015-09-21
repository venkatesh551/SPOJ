'''
Created on 21-Sep-2015

@author: Venkatesh
'''


def read_long():
    return long(raw_input())


def main():
    tc = read_long()
    for _ in xrange(tc):
        n = read_long()
        print (n * (3 * n + 1) / 2) % 1000007

if __name__ == '__main__':
    main()
