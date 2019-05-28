import itertools as it
import sys


def is_solution(perm):
    # for all possible poitions of 2 quenss standing in different columns (axis X) (col0 and col1, col0 and col2, etc...)
    for (x1, x2) in it.combinations(range(len(perm)), 2):
        """
        we compare columns

        if |x1 - x2| == |y1 - y2| => two figures are on one diagonal

        combinations of (x1, x2) allows us to compare columns
        due to the fact that axis X is our array indices => we can extract Y1 values by perm[X1]
        and simply get (X1, Y1) figure pos

        that's how we can simply get 2 queen positions that are on different columns and rows
        """

        if abs(x1 - x2) == abs(perm[x1] - perm[x2]):
            return False
    return True


# basically we iter through all possible permutations and include only valid solutions
def find_all_solutions_on_board_size_of(n):
    for perm in it.permutations(range(n)):
        if is_solution(perm):
            print(perm)


if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
        assert(n > 0)
    except:
        print('The input is invalid. It should be integer greater than 0')
        exit()

    find_all_solutions_on_board_size_of(n)
