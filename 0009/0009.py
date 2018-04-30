import re
import pprint


if __name__ == '__main__':
    with open('python_history.html','r',encoding='utf8') as fd:
        html = fd.readlines()

    links = []
    for line in html:
        hrefs = re.findall(r'href="(http.*?)"',line)
        if hrefs:
            links.extend(hrefs)

    pprint.pprint(links)

    with open('links.txt','w') as fd:
        for link in links:
            fd.write(link+"\n")

