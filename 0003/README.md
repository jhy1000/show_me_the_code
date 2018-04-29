# question
将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

# Attention
must open redis service

# redis 

## start server;
```
redis-service
```
## start client;
```
redis-cli
```

## list operate;
```
将一个或多个值插入到列表头部
LPUSH seriescode 'AZHJC-450UC-1267G-VY2PM-E0CM9';
获取列表长度
LLEN seriescode
对一个列表进行修剪(trim)，就是说，让列表只保留指定区间内的元素，不在指定区间之内的元素都将被删除。
LTRIM key start stop
```

## python operate;
```
import redis

r = redis.Redis(host='127.0.0.1',port=6379)

r.set('1','1234679')
r.get('1')

r.exists('2') # False
r.exists('1') # True
```


# link
- [show-me-the-code](https://github.com/Yixiaohan/show-me-the-code)  
- [RUNOOB.COM](http://www.runoob.com/redis/redis-tutorial.html)
- [redis-py](https://github.com/andymccurdy/redis-py)

