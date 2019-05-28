# python3
"""
TASK: convert a given array of integers into a heap
"""
import time


class MaxHeap:
    # in-place heapify
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)
        for i in range((self.size - 1) // 2, -1, -1):
            self.sift_down(i)

    def insert(self, value):
        self.arr.append(value)
        self.size += 1
        self.sift_up(self.size - 1)

    def sift_up(self, i):
        p_i = (i - 1) // 2
        while p_i >= 0 and self.arr[p_i] < self.arr[i]:
            self.arr[p_i], self.arr[i] = self.arr[i], self.arr[p_i]
            i = p_i
            p_i = (p_i - 1) // 2

    def __len__(self):
        return self.size

    def __repr__(self):
        return str(self.arr)

    def extract_max(self):
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        max_v = self.arr.pop()
        self.size -= 1

        if self.size > 1:
            self.sift_down(0)

        return max_v

    def sift_down(self, i):
        while 2 * i + 1 < self.size:
            left = 2 * i + 1
            right = 2 * i + 2
            max_i = left

            if right < self.size and self.arr[right] > self.arr[max_i]:
                max_i = right

            if self.arr[i] >= self.arr[max_i]:
                break

            self.arr[i], self.arr[max_i] = self.arr[max_i], self.arr[i]
            i = max_i

    # in-place sorting
    def heapsort(self):
        for _ in range(self.size - 1):
            self.size -= 1
            self.arr[0], self.arr[self.size] = self.arr[self.size], self.arr[0]
            self.sift_down(0)


class MinHeap(MaxHeap):
    def sift_up(self, i):
        p_i = (i - 1) // 2
        while p_i >= 0 and self.arr[p_i] > self.arr[i]:
            self.arr[p_i], self.arr[i] = self.arr[i], self.arr[p_i]
            i = p_i
            p_i = (p_i - 1) // 2

    def sift_down(self, i):
        while 2 * i + 1 < self.size:
            left = 2 * i + 1
            right = 2 * i + 2
            min_i = left

            if right < self.size and self.arr[right] < self.arr[min_i]:
                min_i = right

            if self.arr[i] <= self.arr[min_i]:
                break

            self.arr[i], self.arr[min_i] = self.arr[min_i], self.arr[i]
            i = min_i


class MinHeapCountSwaps(MinHeap):
    def __init__(self, arr):
        self.swaps = []
        super().__init__(arr)

    def sift_down(self, i):
        while 2 * i + 1 < self.size:
            left = 2 * i + 1
            right = 2 * i + 2
            min_i = left

            if right < self.size and self.arr[right] < self.arr[min_i]:
                min_i = right

            if self.arr[i] <= self.arr[min_i]:
                break

            self.arr[i], self.arr[min_i] = self.arr[min_i], self.arr[i]
            self.swaps.append((i, min_i))
            i = min_i

    def get_swaps(self):
        return self.swaps


def timed(f):
    def timer(*args):
        t0 = time.perf_counter()
        res = f(*args)
        t1 = time.perf_counter()
        print('%s performed %.6f secs' % (f.__name__, t1 - t0))
        return res

    return timer


@timed
def heapify(heap, arr):
    return heap(arr)


@timed
def get_sorted(heap):
    return heap.heapsort()


def time_test():
    import random
    random.seed(1)
    for _ in range(5):
        # test_arr = [random.randint(-50, 100) for _ in range(5)]
        test_arr = [random.random() for _ in range(10 ** 5)]
        heap_arr = test_arr.copy()
        max_h = heapify(MaxHeap, heap_arr)
        get_sorted(max_h)
        assert heap_arr == sorted(test_arr)

        heap_arr = test_arr.copy()
        min_h = heapify(MinHeap, heap_arr)
        get_sorted(min_h)
        assert heap_arr == sorted(test_arr, reverse=True)

    print("OK")


def test():
    assert MinHeapCountSwaps([5, 4, 3, 2, 1]).get_swaps() == [(1, 4), (0, 1), (1, 3)]
    assert MinHeapCountSwaps([1, 2, 3, 4, 5]).get_swaps() == []
    print("OK")


def main():
    _n = int(input())
    arr = [int(i) for i in input().split()]
    swaps = MinHeapCountSwaps(arr).get_swaps()
    print(len(swaps))
    for a, b in swaps:
        print(a, b)


if __name__ == "__main__":
    time_test()
    test()
    main()
