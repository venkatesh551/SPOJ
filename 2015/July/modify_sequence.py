'''
Created on 22-Jul-2015

NITK06 - MODIFY SEQUENCE

@author: Venkatesh
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def is_possible_to_make_all_zeros(nums, n):
    for ind in xrange(n-1):
        if nums[ind] > nums[ind+1]:
            return False
        else:
            nums[ind+1] -= nums[ind]
    return nums[n-1] == 0


def main():
    tc = read_int()
    for _ in xrange(tc):
        n = read_int()
        nums = read_int_list()
        if is_possible_to_make_all_zeros(nums, n):
            print "YES"
        else:
            print "NO"


if __name__ == '__main__':
    main()
