'''
Created on 12-Sep-2015

@author: venkat
'''


def decode(s, c):
    n, result = len(s), ""
    lst = [s[i:i+c] for i in xrange(0, n, c)]
    for i in xrange(c):
        for ind, ele in enumerate(lst):
            if ind % 2 == 0:
                result += ele[i]
            else:
                result += ele[c-1-i]
    return result


def read_int():
    return int(raw_input())


def main():
    while True:
        c = read_int()
        if c == 0:
            return
        s = raw_input()
        print decode(s, c)

if __name__ == '__main__':
    main()
