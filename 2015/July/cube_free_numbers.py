'''
Created on 21-Jul-2015

@author: Venkatesh
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


class cube_free_num:
    """Store all the cube free numbers
    """
    MAX_VAL = 1000001

    def __init__(self):
        self.num = [0 for _ in xrange(self.MAX_VAL)]
        for ind_i in xrange(2, 100):
            cube = ind_i ** 3
            for ind_j in xrange(cube, self.MAX_VAL, cube):
                self.num[ind_j] = -1
        counter = 1
        for ind in xrange(1, self.MAX_VAL):
            if self.num[ind] == 0:
                self.num[ind] = counter
                counter += 1

    def get_pos(self, val):
        if self.num[val] == -1:
            return "Not Cube Free"
        else:
            return self.num[val]


def main():
    tc = read_int()
    obj = cube_free_num()
    for ind in xrange(1, tc+1):
        num = read_int()
        print "Case " + str(ind) + ": " + str(obj.get_pos(num))


if __name__ == '__main__':
    main()
