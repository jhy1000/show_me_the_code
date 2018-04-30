import sys
import re

def filter(input_string):
    with open('filtered_words.txt','r') as fd:
        keywords = fd.readlines()

    keywords = list(map(lambda x:x.strip(),keywords))

    for key in keywords:
        if re.search(key,input_string):
            filters = re.findall(key,input_string)

            for x in filters:
                input_string = re.sub(key,'*'*len(x),input_string)

            break

    print('input string is:{}'.format(input_string))


if __name__ == '__main__':
    input_string = sys.argv[1]
    filter(input_string)
