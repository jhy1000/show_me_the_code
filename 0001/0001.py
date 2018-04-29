import string
import random
import pprint


VALID_STRING = string.digits + string.ascii_uppercase

def gen_series_code():
    def gen_five_random():
        st = ''.join([random.choice(VALID_STRING) for i in range(5)])
        return st

    st = gen_five_random()
    st = '-'.join([gen_five_random() for i in range(4)])

    return st


if __name__ == '__main__':
    st = [gen_series_code() for i in range(200)]
    pprint.pprint(st)



