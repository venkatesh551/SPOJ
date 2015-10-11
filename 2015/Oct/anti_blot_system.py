'''
Created on 11-Oct-2015

@author: venkat
'''


def read_list():
    return [x for x in raw_input().split()]


def read_int():
    return int(raw_input())


def print_result(nums):
    if nums[0].isdigit() and nums[2].isdigit():
        tot = long(nums[0]) + long(nums[2])
        print nums[0] + " + " + nums[2] + " = " + str(tot)
    elif nums[0].isdigit() and nums[4].isdigit():
        diff = long(nums[4]) - long(nums[0])
        print nums[0] + " + " + str(diff) + " = " + nums[4]
    else:
        diff = long(nums[4]) - long(nums[2])
        print str(diff) + " + " + nums[2] + " = " + nums[4]


def main():
    tc = read_int()
    for _ in xrange(tc):
        # read blank line
        raw_input()
        nums = read_list()
        print_result(nums)


if __name__ == '__main__':
    main()
