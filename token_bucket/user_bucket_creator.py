from token_bucket.token_bucket import TokenBucketRateLimiter


class UserBuckerCreator:
    bucket = {}

    def __init__(self, user_id) -> None:
        self.bucket[user_id] = TokenBucketRateLimiter(
            capacity=10, refresh_rate=1)

    def access_application(self, user_id):

        if user_id in self.bucket and self.bucket[user_id].grant_access():
            print('processing the request...')
            return True
        print('Cannot process the request...')
        return False
