"""
Backtracking Approach helps to solve 8Queens problem much faster.

The main idea - is to cut dead ends of the recursive tree
"""

COUNTER = 0

def generate_permutation(perm, n):

	"""
	Let's generate all possible permutations
	Now it is a SMART generator which can cut dead ends
	"""

	if len(perm) == n:

		# Congrats! U have found a legit solution. Let me make it in [[x1, y1], [x2, y2], [x3, y3] ... [xn, yn]] format
		# queens_pos = []

		# for x in range(len(perm)):
		# 	queens_pos.append([x, perm[x]])

		# print("Final Queens positions:", queens_pos)

		global COUNTER
		COUNTER += 1
		return

	# When the for loop ends its iterations -> current instance of `generate_permutation` func also ends or RETURNS
	# That helps us to navigate among recursive tree
	for k in range(n):
		if k not in perm:
			perm.append(k)
			
			if can_be_extended_to_a_solution(perm):
				generate_permutation(perm, n)

			perm.pop()


def can_be_extended_to_a_solution(perm):

	# We check if the last generated element has a diagonal conflict with already generated elements
	# If YES -> Stop current generation and cut current branch because current permutation cannot be extended to a solution
	# If NO -> Continue current position generation 
	i = len(perm) - 1
	for j in range(i):
		if i - j == abs(perm[i] - perm[j]):
			return False
	return True


generate_permutation(perm=[], n=12)
print("\nTotal N of solutions are:", COUNTER)