# question
一个HTML文件，找出里面的链接。

# re模块findall()详解
```python
import re

string="abcdefg  acbdgef  abcdgfe  cadbgfe"

#带括号与不带括号的区别
#带括号
regex=re.compile("((\w+)\s+\w+)")
print(regex.findall(string))
#输出：[('abcdefg  acbdgef', 'abcdefg'), ('abcdgfe  cadbgfe', 'abcdgfe')]

regex1=re.compile("(\w+)\s+\w+")
print(regex1.findall(string))
#输出：['abcdefg', 'abcdgfe']

#不带括号
regex2=re.compile("\w+\s+\w+")
print(regex2.findall(string))
#输出：['abcdefg  acbdgef', 'abcdgfe  cadbgfe']
```
第一个 regex 中是带有2个括号的，我们可以看到其输出是一个list 中包含2个 tuple 

第二个 regex 中带有1个括号，其输出的内容就是括号匹配到的内容，而不是整个表达式所匹配到的结果。

第三个 regex 中不带有括号,其输出的内容就是整个表达式所匹配到的内容。


结论：findall()返回的是括号所匹配到的结果（如regex1），多个括号就会返回多个括号分别匹配到的结果（如regex），如果没有括号就返回就返回整条语句所匹配到的结果(如regex2)。所以在提取数据的时候就需要注意这个坑。

实际上是由其并不是python特有的，这是正则所特有的，任何一门高级语言使用正则都满足这个特点：有括号时只能匹配到括号中的内容，没有括号[相当于在最外层增加了一个括号]。在正则里面 “()” 代表的是分组的意思，一个括号代表一个分组，你只能匹配到"()"中的内容

# link
[show-me-the-code](https://github.com/Yixiaohan/show-me-the-code)

