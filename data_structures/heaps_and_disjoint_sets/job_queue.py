# python3
"""
You have a program which is parallelized and uses n independent threads 
to process the given list of m jobs.
Determine for each job which thread will process it and when will it start processing.
"""


class PriorityQueue:
    def __init__(self, num_workers):
        # workers = [(i, start_time)]
        # initially all workers have 0 start time
        self.workers = list(enumerate([0] * num_workers))
        self.size = num_workers

    def insert(self, worker):
        self.workers.append(worker)
        self.size += 1
        self.sift_up(self.size - 1)

    def sift_up(self, i):
        p_i = (i - 1) // 2
        # comparing start time values
        while p_i >= 0 and self.workers[p_i][1] >= self.workers[i][1]:
            # if start time values are equal and worker with lower ID is in priority -> break
            if self.workers[p_i][1] == self.workers[i][1] and self.workers[p_i][0] < self.workers[i][0]:
                break

            self.workers[p_i], self.workers[i] = self.workers[i], self.workers[p_i]
            i = p_i
            p_i = (p_i - 1) // 2

    def get_worker(self):
        self.workers[0], self.workers[-1] = self.workers[-1], self.workers[0]
        worker = self.workers.pop()
        self.size -= 1

        if self.size > 1:
            self.sift_down(0)

        return worker

    def sift_down(self, i):
        workers = self.workers
        size = self.size
        while 2 * i + 1 < size:
            left = 2 * i + 1
            right = 2 * i + 2
            avail_worker = left

            if right < size:
                """
                if there is right child let's consider two cases in which it is better to choose right worker:
                a - right worker will be ready sooner than left worker
                b - both workers will be ready at the same time, but right worker has smaller ID 
                """
                a = workers[right][1] < workers[avail_worker][1]
                b = workers[right][1] == workers[avail_worker][1] and workers[right][0] < workers[avail_worker][0]
                if a or b:
                    avail_worker = right

            """
            there are two cases where it is good to stop sifting down:
            a - current worker will be ready sooner than its child
            b - current worker and its child will be ready at the same time, but current worker has smaller ID
            """
            a = workers[i][1] < workers[avail_worker][1]
            b = workers[i][1] == workers[avail_worker][1] and workers[i][0] < workers[avail_worker][0]
            if a or b:
                break

            workers[i], workers[avail_worker] = workers[avail_worker], workers[i]
            i = avail_worker


class WorkerPool:
    def __init__(self, num_workers):
        self.logs = []
        self.pq = PriorityQueue(num_workers)

    def process_jobs(self, jobs):
        for job_time in jobs:
            worker_i, worker_st = self.pq.get_worker()
            self.logs.append((worker_i, worker_st))
            self.pq.insert((worker_i, worker_st + job_time))

        return self.logs


def naive_assign_jobs(num_workers, jobs):
    assigned_workers = [None] * len(jobs)
    start_times = [None] * len(jobs)
    next_free_time = [0] * num_workers
    for i in range(len(jobs)):
        next_worker = 0
        for j in range(num_workers):
            if next_free_time[j] < next_free_time[next_worker]:
                next_worker = j
        assigned_workers[i] = next_worker
        start_times[i] = next_free_time[next_worker]
        next_free_time[next_worker] += jobs[i]

    return list(zip(assigned_workers, start_times))


def print_logs(logs):
    for thread, start_time in logs:
        print(thread, start_time)


def test():
    import sys
    import time
    import random

    jobs = [1, 2, 3, 4, 5]
    assert naive_assign_jobs(2, jobs) == WorkerPool(2).process_jobs(jobs)
    jobs = [1] * 20
    assert naive_assign_jobs(4, jobs) == WorkerPool(4).process_jobs(jobs)

    try:
        test02 = open("job_queue_tests/02")
        test08 = open("job_queue_tests/08")
    except FileNotFoundError as e:
        sys.exit(e)

    n = int(test02.readline().split()[0])
    jobs = list(map(int, test02.readline().split()))
    test02.close()
    assert naive_assign_jobs(n, jobs) == WorkerPool(n).process_jobs(jobs)

    n = int(test08.readline().split()[0])
    jobs = list(map(int, test08.readline().split()))
    test08.close()
    t0 = time.perf_counter()
    WorkerPool(n).process_jobs(jobs)
    t1 = time.perf_counter()

    for _ in range(10):
        n, m = random.randint(1, 1000), random.randint(1, 1000)
        jobs = [random.randrange(1000) for _ in range(m)]
        assert naive_assign_jobs(n, jobs) == WorkerPool(n).process_jobs(jobs)

    print("OK\nlong test took %.5f secs" % (t1 - t0))


def main():
    num_workers, _m = map(int, input().split())
    jobs = list(map(int, input().split()))
    print_logs(WorkerPool(num_workers).process_jobs(jobs))


if __name__ == "__main__":
    test()
    main()
