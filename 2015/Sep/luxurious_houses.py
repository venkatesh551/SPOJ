'''
Created on 28-Sep-2015

@author: Venkatesh
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def print_next_max_num(houses):
    last_max = houses[-1]
    result = [0]
    houses.pop()
    for ele in houses[::-1]:
        if ele <= last_max:
            result.append(last_max - ele + 1)
        else:
            result.append(0)
        last_max = max(last_max, ele)
    for ele in result[::-1]:
        print ele,


def main():
    _ = read_int()
    houses = read_int_list()
    print_next_max_num(houses)

if __name__ == '__main__':
    main()
