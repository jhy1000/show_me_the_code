import hmac
import random

def hmac_md5(key,s):
    return hmac.new(key.encode('utf-8'),s.encode('utf-8'),'MD5').hexdigest()

class User(object):
    def __init__(self,username,password):
        self.username = username
        self.key = ''.join([chr(random.randint(48,122)) for i in range(20)])
        self.password = hmac_md5(self.key,password)

db = {
        'michael': User('michael','123456'),
        'bob': User('bob','abc999'),
        'alice': User('alice','alice2008')
}

if __name__ == '__main__':
    with open('secret.txt','w') as fd:
        for i in db:
            user = db[i]
            fd.write('user:{} salt:{} secret:{}'.format(user.username,user.key,user.password))
            fd.write('\n')

