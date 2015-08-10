'''
Created on 05-Aug-2015

@author: Venkatesh
'''


def read_int_list():
    return [long(x) for x in raw_input().split()]


def main():
    _, k = read_int_list()
    nums = set(read_int_list())
    cnt = 0L
    for ele in nums:
        ele += k
        if ele in nums:
            cnt += 1
    print cnt

if __name__ == '__main__':
    main()
