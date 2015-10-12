'''
Created on 04-Oct-2015

@author: Venkatesh
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def get_max_score(correct_ans, chef_ans, score, n):
    cnt = 0
    for idx in xrange(n):
        if correct_ans[idx] == chef_ans[idx]:
            cnt += 1
    if cnt == n:
        return score[n]
    else:
        return max(score[0:cnt+1])


def main():
    tc = read_int()
    for _ in xrange(tc):
        n = read_int()
        correct_ans = raw_input()
        chef_ans = raw_input()
        score = read_int_list()
        print get_max_score(correct_ans, chef_ans, score, n)

if __name__ == '__main__':
    main()
