'''
Created on 12-Oct-2015

@author: Venkatesh
'''


def get_no_of_groups(idx, prev_sum, s, n):
    ans, cur_sum = 0, 0
    if idx >= n:
        return 1
    for i in xrange(idx, n):
        cur_sum += ord(s[i]) - ord('0')
        if cur_sum >= prev_sum:
            ans += get_no_of_groups(i+1, cur_sum, s, n)
    return ans


def main():
    case = 0
    while True:
        s = raw_input()
        if s == "bye":
            return
        else:
            n = len(s)
            case += 1
            print str(case) + str('.'), get_no_of_groups(0, 0, s, n)


if __name__ == '__main__':
    main()
