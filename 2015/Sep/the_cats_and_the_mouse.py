'''
Created on 24-Sep-2015

@author: Venkatesh
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def distance(pt1, pt2):
    return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])


def is_reachable(pts, n, m):
    m_x, m_y = pts[0], pts[1]
    mouse_pos = (m_x, m_y)
    cat1_pos = (pts[2], pts[3])
    cat2_pos = (pts[4], pts[5])
    all_pts = [(m_x, 1), (m_x, m), (1, m_y), (n, m_y)]
    for pt in all_pts:
        cur_dist = distance(mouse_pos, pt)
        if cur_dist < distance(cat1_pos, pt) \
           and cur_dist < distance(cat2_pos, pt):
            return True
    return False


def main():
    n, m = read_int_list()
    tc = read_int()
    for _ in xrange(tc):
        points = read_int_list()
        print "YES" if is_reachable(points, n, m) else "NO"

if __name__ == '__main__':
    main()
