import re


if __name__ == '__main__':
    with open('howdoi.py','r') as fd:
        codes = fd.readlines()

    statistic = {'comment':0,'code':0,'blank':0}
    for code in codes:
        if re.match(r'#',code):
            statistic['comment'] += 1
            continue

        if re.match(r'\s*$',code):
            statistic['blank'] += 1
            continue

        statistic['code'] += 1

    print(statistic)





