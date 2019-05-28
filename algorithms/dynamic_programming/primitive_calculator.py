# python3

"""
Given an integer n, compute the minimum number of operations needed to obtain the number n
starting from the number 1
"""
from collections import deque


def get_optimal_sequence(n):
    # due to the fact that we count opt. n of calculations for every number up to N
    # every index of actions_arr is a number
    # array contains tuples, every tuple represents
    # number of needed calculations for number or index, previous number used in calculations
    actions_arr = [(0, None), (0, None)]
    operations = (lambda x: x / 3, lambda x: x / 2, lambda x: x - 1)
    optimal_seq = deque([n])

    def count_seq(num):
        if num >= len(actions_arr):
            # we have info for 0 and 1, t.w. we start to count from 2
            for number in range(2, num + 1):
                actions_arr.append((float("inf"), None))
                for operation in operations:
                    res = operation(number)
                    if res == int(res):
                        res = int(res)
                        actions_n, _prev_num = count_seq(res)
                        actions_n += 1
                        if actions_n < actions_arr[number][0]:
                            actions_arr[number] = (actions_n, res)

        return actions_arr[num]

    count_seq(n)

    i = -1
    while actions_arr[i][1]:
        optimal_seq.appendleft(actions_arr[i][1])
        i = actions_arr[i][1]

    return optimal_seq


def main():
    n = int(input())
    seq = get_optimal_sequence(n)
    print(len(seq) - 1)
    for i in seq:
        print(i, end=' ')


if __name__ == "__main__":
    main()
