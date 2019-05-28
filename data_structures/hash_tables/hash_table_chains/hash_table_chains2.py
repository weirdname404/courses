class HashTable:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, cardinality):
        self.arr = [[] for _ in range(cardinality)]
        self.cardinality = cardinality

    def add(self, value):
        chain = self.arr[self._hash(value)]

        if value in chain:
            return
        chain.append(value)

    def find(self, value):
        chain = self.arr[self._hash(value)]
        if value in chain:
            return "yes"
        return "no"

    def delete(self, value):
        chain = self.arr[self._hash(value)]
        if value in chain:
            chain.remove(value)

    def check(self, i):
        chain = self.arr[i]
        print(" ".join(reversed(chain)))

    def _hash(self, string):
        acc = 0
        for c in reversed(string):
            acc = (acc * self._multiplier + ord(c)) % self._prime

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
            i = int(value)
            if i >= cardinality:
                print("")
            else:
                ht.check(i)


if __name__ == "__main__":
    import time

    t0 = time.perf_counter()
    main()
    print(time.perf_counter() - t0)
