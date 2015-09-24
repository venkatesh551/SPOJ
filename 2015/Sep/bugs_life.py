'''
Created on 23-Sep-2015

@author: Venkatesh
'''


def read_int():
    return int(raw_input())


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_graph(n, no_of_pairs):
    graph = [[False] * n for _ in xrange(n)]
    for _ in xrange(no_of_pairs):
        x, y = read_int_list()
        graph[x-1][y-1] = graph[y-1][x-1] = True
    return graph


class Graph(object):

    def __init__(self, n, no_of_pairs):
        self.v_count = n
        self.graph = read_graph(n, no_of_pairs)
        self.visited = [False] * n
        self.color = [-1] * n
        self.status = True

    def is_bipartitie(self):
        v = 0
        while v < self.v_count and self.status:
            if not self.visited[v]:
                self.dfs(v, 0)
            v += 1
        return self.status

    def dfs(self, v, p):
        self.visited[v] = True
        self.color[v] = p
        for w in xrange(self.v_count):
            if self.graph[v][w]:
                if not self.visited[w]:
                    self.dfs(w, 1-p)
                elif self.color[v] == self.color[w]:
                    self.status = False
                    return


def main():
    tc = read_int()
    for case in xrange(tc):
        n, no_of_pairs = read_int_list()
        g_obj = Graph(n, no_of_pairs)
        print "Scenario #" + str(case + 1) + ":"
        if g_obj.is_bipartitie():
            print "No suspicious bugs found!"
        else:
            print "Suspicious bugs found!"


if __name__ == '__main__':
    main()
