from leaky_bucket.user_bucket_creator import UserBuckerCreator as LeakyUserBuckerCreator
from token_bucket.user_bucket_creator import UserBuckerCreator as TokenUserBuckerCreator
from sliding_window.user_bucket_creator import UserBuckerCreator as SlidingWindowUserBuckerCreator
from time import sleep

if __name__ == '__main__':
    user_id = 123
    user_bucket = SlidingWindowUserBuckerCreator(user_id)

    for i in range(13):
        if i == 11:
            sleep(2)
        user_bucket.access_application(user_id)
