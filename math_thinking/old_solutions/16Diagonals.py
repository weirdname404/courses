"""
16 Diagonals problem solved by Backtracking Approach

-1 stands for WE DIDN'T MAKE A CHOICE YET
0 - empty
1 - \
2 - /
"""

import sys


def find_solution(board_size, n):
    # made a board list and populated it with -1 value
    board = [-1] * board_size * board_size
    print("\nhttp://dm.compsciclub.ru/app/quiz-n-diagonals")
    print("\nMain Rules:\n-1 stands for WE DIDN'T MAKE A CHOICE YET\n0 - empty\n1 - \\\n2 - /\n")
    print("The solutions for", n, "Diagonals on", len(board), "cells Square Board are following:\n")

    generate_diagonals(board_size, board, n)


def generate_diagonals(board_size, board, n):
    if board.count(1) + board.count(2) == n:
        print(board)

    if board.count(-1) == 0:
        return False

    for i in range(len(board)):
        if board[i] == 1 or board[i] == 2 or board[i] == 0:
            continue

        # the strategy is to put 1 or 2 and check if there are any conflicts
        board[i] = 1
        if can_be_extented_to_solution(board_size, board, i):
            generate_diagonals(board_size, board, n)

        board[i] = 2
        if can_be_extented_to_solution(board_size, board, i):
            generate_diagonals(board_size, board, n)

        board[i] = 0
        generate_diagonals(board_size, board, n)

        board[i] = -1
        return False


def can_be_extented_to_solution(board_size, board, comparable_element_index):
    compared_element = board[comparable_element_index]

    # we cannot compare first element -> skip
    if comparable_element_index - 1 == -1:
        return True

    # elements are on one ROW -> check if there are some conflicts
    if comparable_element_index < board_size:
        if board[comparable_element_index - 1] == compared_element or board[comparable_element_index - 1] == 0:
            return True

        else:
            return False

    # if board is 5x5 and index is 6 -> we know that element is on 6//5 = 1 ROW
    compared_element_index_row = comparable_element_index // board_size

    """
    MAIN RULES WHICH HELP TO AVOID CONFLICT

    1) if compared_element and the_element_before are on 1 ROW:
        check if In == In-1 or In-1 == 0
       else: skip

    2) In == In-board_size or In-board_size == 0

    3) if element is not on the side of the board check:
        a) if In-board_size == 1: In-board_size != In-board_size - 1
        b) if In-board_size == 2: In-board_size != In-board_size + 1

       else:
           if right_side_element: check 3.a
           if left_side_element: check 3.b
    """

    # if the element_before is on 1 row with compared_element -> we check RULE №1
    if (comparable_element_index - 1) // board_size == compared_element_index_row:
        # if RULE №1 is not satisfied -> return
        if compared_element != board[comparable_element_index - 1]:
            if board[comparable_element_index - 1] != 0:
                return False

    # RULE №2
    if compared_element != board[comparable_element_index - board_size]:
        if  board[comparable_element_index - board_size] != 0:
            return False

    # check if compared_element is a right_side_element
    if (comparable_element_index - board_size + 1) // board_size == compared_element_index_row:

        # RULE №3.a
        if compared_element == 1:
            if board[comparable_element_index - board_size - 1] == compared_element or board[
                                comparable_element_index - board_size - 1] != 0:
                return False

        # if there are other cases
        return True

    # check if compared_element is a left_side_element
    if (comparable_element_index - board_size - 1) // board_size != compared_element_index_row - 1:

        # RULE №3.b
        if compared_element == 2:
            if board[comparable_element_index - board_size + 1] == compared_element or board[
                                comparable_element_index - board_size - 1] != 0:
                return False

        # if there are other cases
        return True

    # if compared_element is a center_element -> check if it still has any diagonal conflicts
    if ((compared_element == 1 and compared_element == board[comparable_element_index - board_size - 1]) or
            (compared_element == 2 and compared_element == board[comparable_element_index - board_size + 1])):
        return False

    return True


find_solution(5, 16)
