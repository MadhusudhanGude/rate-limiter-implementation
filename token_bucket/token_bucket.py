
from rate_limiter import IRateLimiter
from time import time


class TokenBucketRateLimiter(IRateLimiter):
    def __init__(self, capacity=0, refresh_rate=0) -> None:
        self.bucket_capacity = capacity
        self.refresh_rate = refresh_rate
        self.current_capacity = capacity
        self.last_updated_time = int(time())

    def grant_access(self):
        self.refresh_bucket()

        if self.current_capacity > 0:
            self.current_capacity -= 1
            return True
        return False

    def refresh_bucket(self):

        current_time = int(time())
        additional_token = int(
            (current_time - self.last_updated_time) * self.refresh_rate)

        self.current_capacity = min(
            self.current_capacity + additional_token, self.bucket_capacity)
        self.last_updated_time = current_time
