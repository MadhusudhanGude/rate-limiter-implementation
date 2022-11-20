
from rate_limiter import IRateLimiter
from queue import Queue


class LeakyBucketRateLimiter(IRateLimiter):

    def __init__(self, capacity=0) -> None:
        self.queue = Queue(capacity)
        # self.capacity = capacity

    def grant_access(self):
        # if self.capacity - self.queue.qsize() > 0:
        if not self.queue.full():
            self.queue.put(1)
            return True
        return False
