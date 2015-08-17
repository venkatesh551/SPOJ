'''
Created on 17-Aug-2015

@author:  Venkatesh
'''

import sys


def translate_to_cpp(inp):
    


def translate(inp):
    if inp.find('_') == -1:
        translate_to_cpp(inp)
    else:
        translate_to_java(inp)


def main():
    while True:
        inp = sys.stdin.readline()
        if not inp:
            return
        print translate(inp)


if __name__ == '__main__':
    main()
