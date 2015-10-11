'''
Created on 11-Oct-2015

@author: venkat
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def main():
    while True:
        a, b, c = read_int_list()
        if a == 0 and b == 0 and c == 0:
            return
        d = b - a
        if d == c - b:
            print "AP", a + 3 * d
        else:
            r = b / a
            print "GP", a * r ** 3

if __name__ == '__main__':
    main()
