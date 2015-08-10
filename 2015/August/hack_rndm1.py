'''
Created on 06-Aug-2015

@author: Venkatesh
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def b_search(seq, t):
    low = 0
    high = len(seq) - 1
    while low <= high:
        m = (low + high) // 2
        if seq[m] < t:
            low = m + 1
        elif seq[m] > t:
            high = m - 1
        else:
            return True
    return False


def main():
    _, k = read_int_list()
    nums = read_int_list()
    nums.sort()
    cnt = 0
    for ele in nums:
        if b_search(nums, ele+k):
            cnt += 1
    print cnt

if __name__ == '__main__':
    main()
