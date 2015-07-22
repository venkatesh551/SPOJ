'''
Created on 02-Jul-2015

@author: Venkatesh
'''


def min_cnt_stable(in_str):
    open_paren, cnt = 0, 0
    for ch in in_str:
        if ch == '{':
            open_paren += 1
        elif open_paren > 0:
            open_paren -= 1
        else:
            open_paren += 1
            cnt += 1
    cnt += open_paren/2
    return cnt


def main():
    tc = 0
    while True:
        in_str = raw_input().rstrip('\r\n')
        tc += 1
        if in_str.startswith('-'):
            return
        else:
            print str(tc) + ".", min_cnt_stable(in_str)


if __name__ == '__main__':
    main()
