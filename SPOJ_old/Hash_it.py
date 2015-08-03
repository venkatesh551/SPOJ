class HashTable:
    def __init__(self):
        self._cnt = 0
        self.A = [None] * 101

    @staticmethod
    def hash(s):
        total = 0
        for i in xrange(len(s)):
            total = (total + ord(s[i]) * (i+1)) % 101
        return (total * 19) % 101

    def insert(self, s):
        ind = HashTable.hash(s)
        if self.is_exist(s):
            return
        for j in xrange(20):
            pos = (ind + j * (j + 23)) % 101
            if self.A[pos] is None:
                self.A[pos] = s
                self._cnt += 1
                return

    def delete(self, s):
        ind = HashTable.hash(s)
        for j in xrange(20):
            pos = (ind + j * (j + 23)) % 101
            if self.A[pos] == s:
                self.A[pos] = None
                self._cnt -= 1
                return

    def is_exist(self, key):
        ind = HashTable.hash(key)
        for j in xrange(20):
            pos = (ind + j * (j + 23)) % 101
            if self.A[pos] == key:
                return True
        return False

    def count(self):
        return self._cnt

    def get(self):
        result = []
        for ind, ele in enumerate(self.A):
            if ele:
                result.append(str(ind) + ':' + ele)
        return result


def solve():
    t = int(raw_input())
    for _ in xrange(t):
        ht = HashTable()
        n = int(raw_input())
        for __ in xrange(n):
            op, key = raw_input().rstrip().split(':')
            if op == "ADD":
                ht.insert(key)
            else:
                ht.delete(key)
        print ht.count()
        for ele in ht.get():
            print ele

if __name__ == '__main__':
    solve()
