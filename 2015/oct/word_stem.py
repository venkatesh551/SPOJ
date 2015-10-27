'''
Created on 24-Oct-2015

@author: Venkatesh
'''


def read_str_list():
    return [x for x in raw_input().split()]


def read_int():
    return int(raw_input())


def get_stem(s_lst, n):
    fst_str = s_lst[0]
    m = len(fst_str)
    ans = ""
    all_stems = set()
    for k in xrange(1, m+1):
        for j in xrange(m-k+1):
            all_stems.add(fst_str[j:j+k])
    for stem in all_stems:
        flag = True
        for word in s_lst:
            if stem not in word:
                flag = False
                break
        if flag and (len(stem) > len(ans) or
                     (len(ans) == len(stem) and stem < ans)):
            ans = stem
    return ans


def main():
    tc = read_int()
    for _ in xrange(tc):
        n = read_int()
        s_lst = read_str_list()
        print get_stem(s_lst, n)

if __name__ == '__main__':
    main()
