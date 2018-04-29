import string
import random
import pymysql

VALID_STRING = string.digits + string.ascii_uppercase

def gen_series_code():
    def gen_five_random():
        st = ''.join([random.choice(VALID_STRING) for i in range(5)])
        return st

    st = '-'.join([gen_five_random() for i in range(5)])

    return st

def insert_to_db(st):
    db = pymysql.connect(host='127.0.0.1',user='root',password='shanghai',port=3306)
    cursor = db.cursor()
    try:
        cursor.execute('CREATE DATABASE testDB DEFAULT CHARACTER SET utf8')
        cursor.execute('USE testDB')
        try:
            cursor.execute('CREATE TABLE series (code VARCHAR(255) NOT NULL) DEFAULT CHARSET=utf8')
        except:
            print("table 'series' exists")
    except:
        cursor.execute('USE testDB')
        print("database 'testDB' exists")

    old_count = cursor.execute("SELECT * FROM series")

    for i in st:
        cursor.execute("INSERT INTO series(code) VALUES ('{}')".format(i))

    db.commit()

    new_count = cursor.execute("SELECT * FROM series")

    if new_count - old_count == 200:
        print("insert db success")
    else:
        print("insert db failed")

if __name__ == '__main__':
    st = [gen_series_code() for i in range(200)]
    insert_to_db(st)



