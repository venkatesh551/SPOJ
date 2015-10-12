'''
Created on 04-Oct-2015

@author: Venkatesh
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def no_of_non_decreasing_subarrays(nums):
    prev, cnt = 0, 0
    ans = 0
    f_sum = lambda x: (x - 1) * x / 2
    for ele in nums:
        if ele >= prev:
            cnt += 1
        else:
            ans += f_sum(cnt)
            cnt = 1
        prev = ele
    return ans + f_sum(cnt)


def main():
    tc = read_int()
    for _ in xrange(tc):
        n = read_int()
        nums = read_int_list()
        print n + no_of_non_decreasing_subarrays(nums)

if __name__ == '__main__':
    main()
