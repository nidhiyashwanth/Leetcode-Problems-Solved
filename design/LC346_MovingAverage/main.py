# Given a stream of integers and a window size, calculate the moving
# average of all integers in the sliding window.

# MovingAverage m = new MovingAverage(3)
# m.next(1) = (1) --> 1
# m.next(10) = (10 + 1) --> 5.5
# m.next(3) = (3 + 10 + 1) --> 4.66667
# m.next(5) = (5 + 3 + 10) --> 6

import queue

class MovingAverage:

    def __init__(self, size):
        self.q = queue.Queue()
        self.max_size = size
        self.total_sum = 0

    def next(self, val):
        if self.q.qsize() == self.max_size:
            self.total_sum -= self.q.get()
        self.q.put(val)
        self.total_sum += val
        return self.total_sum / self.q.qsize()