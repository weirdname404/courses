import sys


def can_be_extended_to_solution(board, current_index, n):
    diagonal = board[current_index]

    # The absence of the diagonal leads to no conflicts
    if diagonal == 0:
        return True

    # the position of the diagonal on the board
    row = current_index // n
    col = current_index % n

    # check horizontal conflicts
    # check if current diagonal has a horizontal conflict with previous diagonal
    if col > 0:
        if board[current_index - 1] not in {diagonal, 0}:
            return False

    # check vertical conflicts with previous row
    if row > 0:
        upper_cell_index = current_index - n
        # checks upper cell
        if board[upper_cell_index] not in {diagonal, 0}:
            return False

        if diagonal == 1:
            # if not first column check if diagonals have diagonal or corner conflicts
            if col > 0 and board[upper_cell_index - 1] not in {2, 0}:
                return False

        elif diagonal == 2:
            # if not last column check if diagonals on diagonal are different
            if col < n - 1 and board[upper_cell_index + 1] not in {1, 0}:
                return False
    return True


def search_solutions(board):
    # recursive base case, total amount of diagonals should be equal to m
    if board.count(1) + board.count(2) == m:
        # we found a solution
        print(board)
        return

    # if there are no empty cells -> backtrack
    if board.count(-1) == 0:
        return

    for value in range(len(board)):
        if board[value] != -1:
            continue

        for diagonal in [1, 2, 0]:
            board[value] = diagonal

            if can_be_extended_to_solution(board, value, n):
                search_solutions(board)

        # we don't have a decision for a current cell -> backtrack
        board[value] = -1
        return


if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        assert(n > 0)
        assert(m > 0)
    except:
        print('''
The input is invalid.
Input should be in the following format: cmd_name N M
Where N and M are integers > 0.
N is the size of board (N*N).
M is the required number of diagonals.
        ''')
        exit()

    """
    Initially all values of the board are -1 which means - NO DECISION

    0 - Empty
    1 - \
    2 - /
    """
    search_solutions(board=[-1 for _ in range(n*n)])
