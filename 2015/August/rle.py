'''
Created on 04-Aug-2015

@author: Venkatesh
'''

import sys


def rle(in_str):
    stack, cnt, buf = [], 1, ''
    result = ''
    stack.append(in_str[0])
    for c in in_str[1:]:
        # print c, result, buf
        if stack[-1] == c and cnt < 9:
            cnt += 1
            if buf:
                result += '1' + buf + '1'
                buf = ''
        else:
            char = stack.pop()
            if cnt > 1:
                result += str(cnt) + char
                cnt = 1
            else:
                if char == '1':
                    buf += '1'
                buf += char
            stack.append(c)
    if stack and cnt > 1:
        result += str(cnt) + stack[-1]
    elif stack and cnt == 1:
        if stack[-1] == '1':
            buf += '1'
        result += '1' + buf + stack[-1] + '1'
    elif buf:
        result += '1' + buf + '1'
    return result


def main():
    for line in sys.stdin:
        line = line.rstrip('\r\n')
        if line:
            print rle(line)
        else:
            print ""

if __name__ == '__main__':
    main()
