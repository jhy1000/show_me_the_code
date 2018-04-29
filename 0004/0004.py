import collections
import re


def most_common(txt,num):

    with open(txt,'r') as fd:
        pep8 = fd.read()

    li = re.findall(r'\b\w+\b',pep8)

    li = collections.Counter(li)

    li = li.most_common(num)

    print(li)


if __name__ == '__main__':
    most_common('pep8.txt',10)
