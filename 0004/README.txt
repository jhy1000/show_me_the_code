# question
任一个英文的纯文本文件，统计其中的单词出现的个数。

# Counter
```python
from collections import Counter
import re

# Find the ten most common words in Hamlet
words = re.findall(r'\w+', open('hamlet.txt').read().lower())
Counter(words).most_common(10)

#[('the', 1143), ('and', 966), ('to', 762), ('of', 669), ('i', 631),
# ('you', 554),  ('a', 546), ('my', 514), ('hamlet', 471), ('in', 451)]
```

# link
- [show-me-the-code](https://github.com/Yixiaohan/show-me-the-code)
- [collections](https://docs.python.org/3/library/collections.html)

