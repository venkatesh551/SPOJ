'''
Created on 18-Jun-2015

@author: Venkatesh
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def no_of_triples(num_lst, n):
    num_lst.sort()
    cnt = 0
    for i in xrange(n-1, 1, -1):
        j, k = 0, i-1
        while j < k:
            total = num_lst[j] + num_lst[k]
            if num_lst[i] > total:
                cnt += k - j
                j += 1
            else:
                k -= 1
    return cnt


def main():
    while True:
        n = read_int()
        if n == 0:
            return
        num_lst = read_int_list()
        print no_of_triples(num_lst, n)

if __name__ == '__main__':
    main()
