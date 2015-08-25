'''
Created on 21-Aug-2015

@author: venkatesh
'''

import heapq


class MaxHeap(object):
    def __init__(self, x):
        self.heap = [-e for e in x]
        heapq.heapify(self.heap)

    def push(self, value):
        heapq.heappush(self.heap, -value)

    def pop(self):
        return -heapq.heappop(self.heap)


def read_int():
    return int(raw_input())


def read_list(func):
    return [func(x) for x in raw_input().split()]


def get_max_elements(a_lst, n, k):
    return [max(a_lst[ind:ind+k]) for ind in xrange(0, n-k+1)]


def main():
    n = read_int()
    _ = raw_input()
    array = read_list(int)
    k = read_int()
    for x in get_max_elements(array, n, k):
        print x,


if __name__ == '__main__':
    main()
