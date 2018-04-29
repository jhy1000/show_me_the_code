# coding: utf-8
import string
import random
import redis
import json
import sys

VALID_STRING = string.digits + string.ascii_uppercase

def gen_series_code():
    def gen_five_random():
        st = ''.join([random.choice(VALID_STRING) for i in range(5)])
        return st

    st = '-'.join([gen_five_random() for i in range(5)])

    return st


def insert_to_redis(st):

    #REDIS = get_redis()
    REDIS = redis.Redis(host="127.0.0.1",port=6379)

    old_count = REDIS.llen('seriescode')

    for i in st:
        REDIS.rpush('seriescode',i)

    new_count = REDIS.llen('seriescode')

    if new_count - old_count == 200:
        print("insert db success")
    else:
        print("insert db failed")


if __name__ == '__main__':
    st = [gen_series_code() for i in range(200)]

    insert_to_redis(st)



