from sliding_window.sliding_window import SlidingWindowRateLimiter


class UserBuckerCreator:
    bucket = {}

    def __init__(self, user_id) -> None:
        self.bucket[user_id] = SlidingWindowRateLimiter(
            capacity=5, time_window_in_secs=1)

    def access_application(self, user_id):

        if user_id in self.bucket and self.bucket[user_id].grant_access():
            print('processing the request...')
            return True
        print('Cannot process the request...')
        return False
