'''
Created on 23-Oct-2015

@author: Venkatesh
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def is_palindrome(n):
    s = str(n)
    i, j = 0, len(s)-1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def precompute(maxn=100001):
    sum_lst = [0L]
    for n in xrange(1, maxn):
        if is_palindrome(n):
            sum_lst.append(sum_lst[-1] + n)
        else:
            sum_lst.append(sum_lst[-1])
    return sum_lst


def main():
    f = precompute()
    tc = read_int()
    for _ in xrange(tc):
        a, b = read_int_list()
        print f[b] - f[a-1]

if __name__ == '__main__':
    main()
