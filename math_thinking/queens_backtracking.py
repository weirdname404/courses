import sys

def can_be_extended_to_solution(perm):
    # X axis
    last_queen_indx = len(perm) - 1

    # check if the last standing queen is attacking any queen on the board
    for x_col in range(last_queen_indx):
        # check diagonals of last queen with every other queen
        if last_queen_indx - x_col == abs(perm[last_queen_indx] - perm[x_col]):
            return False
    return True


def find_all_solutions_on_board_size_of(n):
    search_solutions(perm=[], n=n)


def search_solutions(perm, n):
    if len(perm) == n:
        print(perm)
        return

    for y_row in range(n):
        # if two queens are not on the same row
        if y_row not in perm:
            # check if it is good position which can be extended
            perm.append(y_row)

            if can_be_extended_to_solution(perm):
                search_solutions(perm, n)

            perm.pop()


if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
        assert(n > 0)
    except:
        print('The input is invalid. It should be integer greater than 0')
        exit()

    find_all_solutions_on_board_size_of(n)
