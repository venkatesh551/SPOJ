'''
Created on 24-Sep-2015

@author: Venkatesh
'''

from collections import defaultdict


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def no_of_connected_components(d, n):
    visited = [False] * n
    cnt = 0
    for v in xrange(n):
        if not visited[v]:
            dfs(d, visited, v)
            cnt += 1
    return cnt


def dfs(graph, visited, root):
    visited[root] = True
    for v in graph[root]:
        if not visited[v]:
            dfs(graph, visited, v)


def main():
    tc = read_int()
    for _ in xrange(tc):
        raw_input()  # Two blank lines
        raw_input()
        n = read_int()
        d = defaultdict(list)
        for _ in xrange(read_int()):
            x, y = read_int_list()
            d[x].append(y)
            d[y].append(x)
        print no_of_connected_components(d, n)


if __name__ == '__main__':
    main()
