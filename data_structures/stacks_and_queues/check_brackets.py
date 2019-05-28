# python3
"""
INPUT: Input contains one string S which consists of big and small latin letters, digits,
punctuation marks and brackets from the set[]{}()

OUTPUT: If the code in S uses brackets correctly, output “Success" (without the quotes).
Otherwise,output the 1-based index of the first unmatched closing bracket, and if there are
no unmatched closing brackets, output the 1-based index of the first unmatched opening bracket.
"""
from collections import namedtuple

Bracket = namedtuple("Bracket", ["position", "char"])


def find_mismatch(text):
    brackets_stack = []
    opening_brackets = {"(", "[", "{"}
    closing_brackets = {")", "]", "}"}

    for i, char in enumerate(text):
        if char in opening_brackets:
            brackets_stack.append(Bracket(position=i, char=char))

        elif char in closing_brackets:
            if not brackets_stack or brackets_stack.pop().char + char not in {"()", "[]", "{}"}:
                return i + 1

    return "Success" if not brackets_stack else brackets_stack.pop().position + 1


def test():
    import sys
    import os

    assert find_mismatch("foo(bar[i);") == 10
    assert find_mismatch("foo(bar);") == "Success"
    assert find_mismatch("{[}") == 3
    assert find_mismatch("{[]}()") == "Success"
    assert find_mismatch("{") == 1

    try:
        tests = [t for t in os.scandir("tests")]
    except FileNotFoundError as e:
        sys.exit(e)

    for t in tests:
        with open(t) as f:
            test_case = f.readline()

        find_mismatch(test_case)

    print("TESTS PASSED")


def main():
    text = input()
    print(find_mismatch(text))


if __name__ == "__main__":
    # test()
    main()
