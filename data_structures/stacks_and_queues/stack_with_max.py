# python3
"""
Implement a stack supporting the operations Push(),Pop(), andMax().

INPUT: The first line of the input contains the number q of queries.
Each of the following q lines specifies a query of one of the following formats: push v, pop, or max

OUTPUT: For each max query, output (on a separate line) the maximum value of the stack
"""
import sys


class StackWithMax():
    def __init__(self):
        self.stack = []
        self.auxiliary_stack = []

    def push(self, a):
        self.stack.append(a)

        if len(self.auxiliary_stack) == 0:
            self.auxiliary_stack.append(a)
        else:
            last_symbol = self.auxiliary_stack[-1]
            if a > last_symbol:
                self.auxiliary_stack.append(a)
            else:
                self.auxiliary_stack.append(last_symbol)

    def pop(self):
        assert (len(self.stack)) > 0
        self.stack.pop()
        self.auxiliary_stack.pop()

    def max(self):
        assert (len(self.stack)) > 0
        return self.auxiliary_stack[-1]


if __name__ == '__main__':
    stack = StackWithMax()
    _num_queries = sys.stdin.readline()

    for line in sys.stdin.readlines():
        command, *value = line.split()

        if command == "push":
            stack.push(int(*value))

        elif command == "pop":
            stack.pop()

        elif command == "max":
            print(stack.max())
