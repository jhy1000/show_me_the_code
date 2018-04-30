import re
import requests
import os

URL = 'http://tieba.baidu.com/p/2166231880?traceid='
PATTERN = 'img pic_type="0" class="BDE_Image" src="(.*?)"'

if __name__ == '__main__':

    html = requests.get(URL)

    img_urls = []
    if html.status_code == 200:
        img_urls = re.findall(PATTERN,html.text)

    if img_urls:
        try:
            os.mkdir("./image")
        except:
            pass

        os.chdir("./image")

        for img in img_urls:
            os.system('wget -q {} '.format(img))

        os.chdir("../")

        os.system('tree -h')

