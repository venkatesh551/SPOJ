'''
Created on 15-Oct-2015

@author: Venkatesh
'''


def read_int():
    return int(raw_input())


def print_subtraction(a, b):
    b = '-' + b
    m, n = len(a), len(b)
    result = long(a) + long(b)
    len_diff = m-n
    if len_diff >= 0:
        b = len_diff * ' ' + b
    else:
        a = ' ' + a
    result = str(result)
    dashes_length = max(len(result), n)
    dashes = (len(b) - dashes_length) * ' ' + dashes_length * '-'
    print a
    print b
    print dashes
    print (len(dashes) - len(result)) * ' ' + result


def main():
    tc = read_int()
    for _ in xrange(tc):
        a, b = raw_input().split('-')
        print_subtraction(a, b)

if __name__ == '__main__':
    main()
