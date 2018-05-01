# question
通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。
阅读资料 [用户密码的存储与 Python 示例](http://zhuoqiang.me/password-storage-and-python-example.html)  
阅读资料 [Hashing Strings with Python](https://www.pythoncentral.io/hashing-strings-with-python/)
阅读资料 [Python's safest method to store and retrieve passwords from a database](https://stackoverflow.com/questions/2572099/pythons-safest-method-to-store-and-retrieve-passwords-from-a-database)


# example
store in secret.txt
```
user:michael salt:UeYI5R`OpIEVLq^AJTfJ secret:23f92028354185b6564a829e87d8521d
user:bob salt:mhwt;tEH;N53As\I<=N: secret:f2b80d9d08478a78cc5681c04e1ca426
user:alice salt:ShnW0T\a4I]vM[PPXCDp secret:b30b284bada9b510e344532432a2b0a0
```
origin secret
```
db = {
        'michael': User('michael','123456'),
        'bob': User('bob','abc999'),
        'alice': User('alice','alice2008')
}
```

```
>>> hmac.new('UeYI5R`OpIEVLq^AJTfJ'.encode('utf-8'),'123456'.encode('utf-8'),'MD5').hexdigest()
'23f92028354185b6564a829e87d8521d'
```

# link
[show-me-the-code](https://github.com/Yixiaohan/show-me-the-code)


