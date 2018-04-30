import sys

def filter(input):
    with open('filtered_words.txt','r') as fd:
        keywords = fd.readlines()

    keywords = map(lambda x:x.strip(),keywords)

    if input in keywords:
        print('Freedom')
    else:
        print('Human Rights')

if __name__ == '__main__':
    input = sys.argv[1]
    filter(input)
