'''
Created on 24-Jul-2015

@author: Venkatesh
'''


def read_list():
    return [x for x in raw_input().split()]


def main():
    scores = [0, 0, 0]
    strike, nonstrike = 0, 1
    for ele in read_list():
        if ele == 'W' or ele == 'N':
            pass
        elif ele == 'O':
            strike = 2
        else:
            cur_score = int(ele)
            scores[strike] += cur_score
            if cur_score % 2 != 0:
                strike, nonstrike = nonstrike, strike
    for val in scores:
        print val


if __name__ == '__main__':
    main()
