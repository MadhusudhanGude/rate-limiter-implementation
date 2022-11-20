
from rate_limiter import IRateLimiter
from queue import Queue
from time import time


class SlidingWindowRateLimiter(IRateLimiter):
    def __init__(self, capacity=0, time_window_in_secs=0) -> None:
        self.time_window_in_secs = time_window_in_secs
        self.bucket_capacity = capacity
        self.sliding_window = Queue()

    def grant_access(self):
        current_time = int(time())
        self.check_and_update_queue()
        if self.sliding_window.qsize() < self.bucket_capacity:
            self.sliding_window.put(current_time)
            return True
        return False

    def check_and_update_queue(self):
        if self.sliding_window.empty():
            return
        current_time = int(time())
        calculate_time = current_time - self.sliding_window.queue[0]
        while calculate_time > self.time_window_in_secs:
            self.sliding_window.get()
            if self.sliding_window.empty():
                break
            calculate_time = current_time - self.sliding_window.queue[0]
