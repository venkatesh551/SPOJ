'''
Created on 26-Oct-2015

@author: Venkatesh
'''


d = {'m': 1000,
     'c': 100,
     'x': 10,
     'i': 1
     }


def read_int():
    return int(raw_input())


def mcxi_to_decimal(s):
    val, prev = 0, 1
    for ch in s:
        if ch.isdigit():
            prev = ord(ch) - ord('0')
        else:
            val += prev * d[ch]
            prev = 1
    # print val
    return val


def decimal_to_mcxi(num):
    result = ""
    for k in ('m', 'c', 'x', 'i'):
        v = d[k]
        q = num/v
        if q > 1:
            result += str(q) + k
            num %= v
        elif q == 1:
            result += k
            num %= v
    return result


def get_result(a, b):
    tot = mcxi_to_decimal(a) + mcxi_to_decimal(b)
    return decimal_to_mcxi(tot)


def main():
    tc = read_int()
    for _ in xrange(tc):
        a, b = raw_input().split()
        print get_result(a, b)

if __name__ == '__main__':
    main()
