'''
Created on 03-Aug-2015

@author: Venkatesh
'''


def read_int():
    return int(raw_input())


def get_str(num):
    word = 'manku'
    result = ''
    while num > 0:
        num -= 1
        result = word[num % 5] + result
        num /= 5
    return result


def main():
    tc = read_int()
    for _ in xrange(tc):
        num = read_int()
        print (get_str(num))


if __name__ == '__main__':
    main()
