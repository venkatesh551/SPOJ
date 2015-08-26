'''
Created on 26-Aug-2015

@author: venkatesh

EC_CONB - Even Numbers
'''


def read_int():
    return int(raw_input())


def invert_binary(num):
    if num & 1:
        return num
    bits = []
    while num % 2 == 0:
        num /= 2
    while num > 0:
        b = num % 2
        num /= 2
        bits.append(b)
    result, pw = 0, 2 ** len(bits)
    for ele in bits:
        pw /= 2
        result += ele * pw
    return result


def main():
    tc = read_int()
    for _ in xrange(tc):
        num = read_int()
        print invert_binary(num)


if __name__ == '__main__':
    main()
