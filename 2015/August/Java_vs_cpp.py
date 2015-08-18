'''
Created on 17-Aug-2015

@author:  Venkatesh
'''

import sys


def translate_to_cpp(inp):
    result = ''
    for ch in inp:
        if ch.isupper():
            result += '_' + ch.lower()
        else:
            result += ch
    return result


def translate_to_java(inp):
    result = ''
    prev = 'x'
    for ch in inp:
        if ch.isupper():
            return "Error!"
        elif prev == '_':
            result += ch.upper()
        elif ch != "_":
            result += ch
        prev = ch
    return result


def translate(inp):
    if not inp[0].islower() or inp.endswith('_') or inp.find('__') >= 0:
        return "Error!"
    if inp.find('_') == -1:
        return translate_to_cpp(inp)
    else:
        return translate_to_java(inp)


def main():
    while True:
        inp = sys.stdin.readline().rstrip()
        if not inp:
            return
        print translate(inp)


if __name__ == '__main__':
    main()
