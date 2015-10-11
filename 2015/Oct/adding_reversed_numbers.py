'''
Created on 11-Oct-2015

@author: venkat
'''


def read_list():
    return [x for x in raw_input().split()]


def read_int():
    return int(raw_input())


def main():
    tc = read_int()
    for _ in xrange(tc):
        a, b = read_list()
        tot = long(a[::-1]) + long(b[::-1])
        tot = str(tot)
        tot = tot[::-1]
        idx = 0
        while tot[idx] == '0':
            idx += 1
        print tot[idx:]

if __name__ == '__main__':
    main()
