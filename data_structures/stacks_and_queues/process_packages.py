# python3
"""
You are given a series of incoming network packets, and your task is to simulate their processing

INPUT: The first line of the input contains the size S of the buffer and the number n of incoming network packets.
Each of the next n lines contains two numbers. i-th line contains the time of arrival A and
the processing time P (both in milliseconds) of the i-th packet.

OUTPUT: For each packet output either the moment of time (in milliseconds) when the processor
began processing it or −1 if the packet was dropped.
"""

import time
import sys
from collections import namedtuple, deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


def timed(f):
    def wrapper(*args):
        t0 = time.perf_counter()
        res = f(*args)
        t1 = time.perf_counter()
        print("%s performed in %.5f secs" % (f.__name__, t1 - t0))
        return res

    return wrapper


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_q = deque()

    def __enqueue_req(self, start_time, fin_time):
        self.finish_time_q.append(fin_time)
        return Response(False, start_time)

    def process(self, request):
        start_time = request.arrived_at

        if self.finish_time_q:
            # can we free up some space in a buffer?
            # if FIRST REQUEST in queue HAS FINISHED -> it is DELETED from a queue
            if self.finish_time_q[0] <= request.arrived_at:
                self.finish_time_q.popleft()

            # if we are not done with first packet -> check if the queue is full
            elif len(self.finish_time_q) == self.size:
                return Response(True, -1)

            # if new packet has arrived and some packet is still being processed -> new packet waits
            if len(self.finish_time_q) > 0:
                start_time = max(self.finish_time_q[-1], request.arrived_at)

        else:
            # it might be the case that the SIZE of BUFFER is 0, we should be able to handle this case
            if not self.size and request.time_to_process:
                return Response(True, -1)

        return self.__enqueue_req(start_time, start_time + request.time_to_process)


# @timed
def process_requests(buffer, requests):
    return [buffer.process(request) for request in requests]


def test():
    import sys
    import os

    try:
        test_files = [f for f in os.scandir("tests")]

    except FileNotFoundError as e:
        sys.exit(e)

    for file in test_files:
        with open(file) as f:
            buffer_size, _n_requests = map(int, f.readline().split())
            requests = [Request(*map(int, i.split())) for i in f.readlines()]

        buffer = Buffer(buffer_size)
        print("Test %s" % file.name)
        process_requests(buffer, requests)
        print("OK\n")


def main():
    buffer_size, _n_requests = map(int, sys.stdin.readline().split())
    requests = [Request(*map(int, line.split())) for line in sys.stdin.readlines()]
    buffer = Buffer(buffer_size)
    responses = process_requests(buffer, requests)

    for response in responses:
        print(response.started_at)


if __name__ == "__main__":
    # test()
    main()
