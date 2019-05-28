# python3

"""
Priority queue uses array heap (max -> min)

Program responds to 2 commands (Insert X and ExtractMax)
When program is started, please enter how many commands will be there.
After that you can enter commands.
"""
import sys
import time


def timed(f):
    def timer(*args):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        print('%.6f secs' % (t1 - t0))

    return timer


class Heap:
    def __init__(self):
        self.q = []
        self.size = 0

    def __repr__(self):
        return f'Heap-Array {self.q}'

    def push(self, v):
        self.q.append(v)
        self.size += 1
        self.__old_shift_up(self.size - 1)

    # O(logn)
    def __shift_up(self, i):
        p_i = (i - 1) // 2
        while self.q[i] > self.q[p_i]:
            self.q[i], self.q[p_i] = self.q[p_i], self.q[i]
            i, p_i = p_i, (p_i - 1) // 2 if p_i != 0 else 0

    def __old_shift_up(self, i):
        if self.size > 1:
            c = self.q[i]
            c_i = i
            p_i = self.__get_parent_index_of(c_i)

            while self.q[p_i] < c:
                tmp = self.q[p_i]
                self.q[p_i] = c
                self.q[c_i] = tmp
                c_i, p_i = p_i, self.__get_parent_index_of(p_i)

    @staticmethod
    def __get_parent_index_of(i):
        return i // 2 - 1 if i % 2 == 0 and i != 0 else i // 2

    def pop_max(self):
        try:
            max_v = self.q[0]
            min_v = self.q.pop()
            self.size -= 1
            if self.size > 0:
                self.q[0] = min_v
                self.__shift_down(0)

            return max_v

        except IndexError:
            return 'Insert value first'

    # we add indexes of node's children if their indexes are not out of range
    def __get_children_below(self, i):
        return [c for c in [i * 2 + 1, i * 2 + 2] if c <= self.size - 1]

    # O(logn)
    def __shift_down(self, i):
        while 2 * i + 1 < self.size:
            left = 2 * i + 1
            right = 2 * i + 2
            c_i = left

            if right < self.size and self.q[right] > self.q[left]:
                c_i = right

            if self.q[i] >= self.q[c_i]:
                break

            self.q[i], self.q[c_i] = self.q[c_i], self.q[i]
            i = c_i

    def __old_shift_down(self, i):
        children = self.__get_children_below(i)

        while children:
            pushed_el = self.q[i]
            max_c_i = max(children, key=lambda x: self.q[x])
            max_c_v = self.q[max_c_i]

            if pushed_el >= max_c_v:
                break

            self.q[i] = max_c_v
            self.q[max_c_i] = pushed_el
            i = max_c_i
            children = self.__get_children_below(i)

    # recursive
    def __rec_shift_down(self, i):
        children = self.__get_children_below(i)

        if not children:
            return

        max_c_i = max(children, key=lambda x: self.q[x])
        max_c_v = self.q[max_c_i]
        pushed_el = self.q[i]

        if pushed_el < max_c_v:
            self.q[i] = max_c_v
            self.q[max_c_i] = pushed_el
            i = max_c_i
            self.__rec_shift_down(i)


@timed
def main():
    p_q = Heap()
    cmd_dict = {
        'Insert': p_q.push,
        'ExtractMax': p_q.pop_max
    }

    n = int(input())

    for _ in range(n):
        cmd, *args = input().split()
        try:
            cmd = cmd_dict[cmd]
        except:
            cmd_l = " ".join(cmd_dict.keys())
            sys.exit(f'Unknown command!\nI know only: {cmd_l}')

        if args:
            args = map(int, args)
            for a in args:
                cmd(a)
            # print(p_q)
        else:
            # print(cmd())
            cmd()
            # print(p_q)


if __name__ == "__main__":
    main()
