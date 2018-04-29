# question
将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

# mysql 

## connect database;
```
mysql -u root -p
```
## create database;
```
CREATE DATABASE testDB DEFAULT CHARACTER SET utf8;
```

## create table;
```
CREATE TABLE series (code VARCHAR(255) NOT NULL) DEFAULT CHARSET=utf8;
```

## insert data;
```
INSERT INTO series(code) VALUES ('TIM13-EQ0OQ-WKXR5-MDCB1-GPE6O');
```

## select database;
```
use testDB;
```

## delete data;
```
DELETE FROM series;
```

## query data;
```
SELECT * FROM series;
```

## modify data;
```
UPDATE series SET code=REPLACE(code,'LFBF4-IK05C-A38WB-YKV19-1J9NQ','LFBF4-IK05C-A38WB-YKV19-00000');
```


# link
- [show-me-the-code](https://github.com/Yixiaohan/show-me-the-code)  
- [RUNOOB.COM](http://www.runoob.com/mysql/mysql-tutorial.html)

