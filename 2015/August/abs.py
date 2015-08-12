'''
Created on 12-Aug-2015

@author:  Venkatesh

ABSP1 - abs(a-b) I

'''


def read_list(func):
    return [func(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def get_abs_diff(nums):
    total = sum(nums)
    n, ans = len(nums), 0
    for ind in xrange(n-1, 0, -1):
        total -= nums[ind]
        ans += nums[ind] * ind - total
    return ans


def main():
    tc = read_int()
    for _ in xrange(tc):
        _ = read_int()
        nums = read_list(int)
        print get_abs_diff(nums)

if __name__ == '__main__':
    main()
