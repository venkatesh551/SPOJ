'''
Created on 20-Jul-2015

@author: Venkatesh
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def get_max_turns(h, a):
    cnt = 1
    h += 3
    a += 2
    while True:
        if h > 5 and a > 10:
            h -= 2
            a -= 8
            cnt += 2
        elif h > 20:
            h -= 17
            a += 7
            cnt += 2
        else:
            return cnt


def main():
    tc = read_int()
    for _ in xrange(tc):
        h, a = read_int_list()
        print get_max_turns(h, a)

if __name__ == '__main__':
    main()
