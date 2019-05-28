import itertools as it

"""
8 Queens puzzle BRUTE FORCE SOLUTION

DO NOT TRY TO FIND SOLUTION FOR >11 Queens

Start from "find_solution()"
"""

COUNTER = 0

# TODO: how can we optimise?
PAIR_COMBINATIONS = it.combinations(range(8), 2)

def is_solution(perm):

	"""
	EXPLANATION:

	1) it.combinations(range(8), 2) generates array of all PAIR combinations of [0, 1, 2, 3, 4, 5, 6, 7] array elements
	(all possible positions of 2 Queens standing on different COLUMNS)

	2) for every pair of X coordinates of 2Queens
		a) [i1, j1] , [i2, j2] == [x1, y1] , [x2, y2]

		b) we have all combinations, so we can compare every pair of Queens from a given permutation

		we use our X coordinates pair to extract 
		Y coordinates from given PERMUTATION array, where ORDER MATTERS

		With the help of this approach we can check almost every combination from given perm taking in account
		our rule: on 1 column and 1 row stands 1 Queen

	3) check if 2 compared Queens are on the one diagonal 
	if |i1-i2| = |j1-j2| -> 2Queens are on the one diagonal -> return False

	if we find a diagonal conflict programm will return and start checking another permutation

	WARNING! 
	it is a BRUTE FORCE APPROACH, which takes a lot of time O(n!)

        ONE MORE TIME! 
        The worst case is that every permutation which is one from 8! as default, is compared with 56 combinations of 2 numbers from given permutation =>
        8! * 56 = 2257920


	4) if all's good -> return True

	"""

	# for x1, x2 in combinations of x1 and x2 [(0, 1), (0, 2). . .]
	for (i1, i2) in it.combinations(range(len(perm)), 2):

		global COUNTER
		COUNTER += 1

		if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
			return False

	return True


def find_solution():

	solutions = []
	all_queens_pos = []

	"""
	EXPLANATION:

	1) it.permutations(range(8)) generates array of all permutations of all elements of [0, 1, 2, 3, 4, 5, 6, 7] array
	(possible positions of 8 Queens standing on different ROWS) !8

	We have all permutation for Y axis

	There MUST be only 1 Queen for 1 ROW and 1 COLUMNS -> X axis is CONSTANT and equals to [0, 1, 2, 3, 4, 5, 6, 7]

	There are 8! different positions for the Queens


	2) Check every permutation if it has a diagonal conflict (check EXPLANATION above)

	3) if NO -> All's good -> solutions.append(permutation)
	"""

	for perm in it.permutations(range(8)):

		global COUNTER
		COUNTER += 1

		if is_solution(perm):
			solutions.append(perm)


	for solution in solutions:
		queens_pos = []

		for i in range(len(solution)):
			queens_pos.append([i, solution[i]])

		all_queens_pos.append(queens_pos)


	print("\nNumber of solutions:", len(solutions), "\n")
	print("\nNumber of loop steps:", COUNTER)
	print("\n")

	for i in all_queens_pos:
		print(i)
	# for i in solutions:
	# 	print(i)

find_solution()