'''
Created on 29-Jul-2015

@author: Venkatesh
'''

import collections


class Trie(object):
    """Trie implementation, with set-style interface"""
    def __init__(self, items=()):
        self._children = collections.defaultdict(Trie)
        self.is_terminal = False
        for item in items:
            self.add(item)

    def add(self, item):
        self.get_node(item).is_terminal = True

    def __getitem__(self, key):
        """Retrieve node at specified item, if any words exist with that prefix.
        Otherwise, throws a KeyError
        """
        current = self
        for ch in key:
            current = current._children.get(ch)
            if current is None:
                raise KeyError(key)
            elif current.is_terminal:
                return current
        return current

    def __contains__(self, key):
        try:
            self[key]
            return True
            # return item.is_terminal
        except KeyError:
            return False

    def get_node(self, key):
        """Obtain position for given prefix, creating nodes
        if it doesn't already exist"""
        current = self
        for ch in key:
            current = current._children[ch]
        return current


def read_int():
    return int(raw_input())


def main():
    tc = read_int()
    for _ in xrange(tc):
        n = read_int()
        trie_obj = Trie()
        exist = False
        for _ in xrange(n):
            cur_str = raw_input().rstrip()
            if not exist and cur_str not in trie_obj:
                trie_obj.add(cur_str)
            else:
                exist = True
        print ("NO" if exist else "YES")


if __name__ == '__main__':
    main()
