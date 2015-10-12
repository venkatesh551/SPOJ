'''
Created on 11-Oct-2015

@author: venkat
'''


def read_int_list(n):
    return [read_int() for _ in xrange(n)]


def read_int():
    return int(raw_input())


def main():
    while True:
        n = read_int()
        if n < 0:
            return
        nums = read_int_list(n)
        total = sum(nums)
        if total % n != 0:
            print "-1"
        else:
            cnt = 0
            q = total / n
            for x in nums:
                if x < q:
                    cnt += q-x
            print cnt


if __name__ == '__main__':
    main()
