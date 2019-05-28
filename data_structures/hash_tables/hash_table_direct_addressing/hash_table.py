# python3
# coding=utf-8

"""
In this task your goal is to implement a simple phone book manager.
It should be able to process the following types of user’s queries:
 - add num name
 - del num
 - find num

Use the direct addressing scheme.
Tel. num. has no more than 7 digits
"""


# direct addressing scheme
class HashTable:
    def __init__(self):
        self.arr = [None] * 10 ** 7

    def append(self, key, value):
        self.arr[key] = value

    def find(self, key):
        return self.arr[key] if self.arr[key] else "not found"

    def delete(self, key):
        self.arr[key] = None


def main():
    n = int(input())
    ht = HashTable()
    for _ in range(n):
        query = input().split()
        num = int(query[1])
        if query[0] == "add":
            ht.append(num, query[2])
        else:
            if query[0] == "find":
                print(ht.find(num))
            else:
                ht.delete(num)


if __name__ == "__main__":
    main()
