import random
import time

import requests
import re

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',

    'referer': 'https://www.mzitu.com',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1'
}


def get_html(url):
    html = requests.get(url, headers=headers).content.decode('utf-8')
    return html


def parse_html(html):

    content = html
    pattern = re.compile(r'<div class="main-image">.*?<img.*?src="(.*?)".*?</div>', re.S)
    img = re.findall(pattern, content)

    return img


def save_img():
    pass


def main():
    img_urls = []
    page = 10
    for i in range(1, page + 1):
        url = 'https://www.mzitu.com/245158/{}'.format(i)
        time.sleep(random.randint(2, 5))
        html = get_html(url)
        # print(html)
        img_url = parse_html(html)
        img_urls.append(img_url[0])
    print(img_urls)


if __name__ == '__main__':
    main()
