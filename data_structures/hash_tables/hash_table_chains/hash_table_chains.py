# python3
"""
Implement a map for storing strings based on a hash table with lists chaining.
Polynomial hash function for hashing a string:
h(S) = (sum(S[i]*x**i) mod p) mod m
where
S[i] - ASCII code of i-th symbol of S
p = 1000000007
x = 263

Your program should support
 - add string
 - del string
 - find string
 - check i
"""


class Chain:
    def __init__(self, value):
        self.next = None
        self.value = value


class HashTable:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, cardinality):
        self.arr = [None] * cardinality
        self.cardinality = cardinality

    def add(self, value):
        new_chain = Chain(value)
        i = self._hash(value)
        chain = self.arr[i]

        if chain:
            while chain:
                # if such value exists in hash table - ignore query
                if chain.value == value:
                    return
                else:
                    chain = chain.next

            new_chain.next = self.arr[i]

        self.arr[i] = new_chain

    def find(self, value):
        chain = self.arr[self._hash(value)]
        while chain:
            if chain.value == value:
                return "yes"

            chain = chain.next

        return "no"

    def delete(self, value):
        i = self._hash(value)
        chain = self.arr[i]
        prev_chain = None
        while chain:
            if chain.value == value:
                if prev_chain:
                    prev_chain.next = chain.next
                else:
                    self.arr[i] = chain.next

                return
            else:
                prev_chain = chain
                chain = chain.next

    def check(self, i):
        chain = self.arr[i]
        while chain:
            print(chain.value, end=" ")
            chain = chain.next

        print("")

    def _hash(self, string):
        acc = 0
        for i in range(len(string)):
            acc += ord(string[i]) * self._multiplier ** i

        return acc % self._prime % self.cardinality


def main():
    cardinality = int(input())
    n = int(input())
    ht = HashTable(cardinality)

    for _ in range(n):
        command, value = input().split()
        if command == "add":
            ht.add(value)
        elif command == "del":
            ht.delete(value)
        elif command == "find":
            print(ht.find(value))
        else:
            ht.check(int(value))


if __name__ == "__main__":
    main()
