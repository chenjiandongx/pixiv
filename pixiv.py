import requests
from bs4 import BeautifulSoup
from pprint import pprint

class Pixiv():

    def __init__(self, search, page):
        self.search = search
        self.page = page
        self.result = set()
        self.headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/56.0.2924.87 Safari/537.36'}

    @property
    def cookies(self):
        with open("cookies.txt", 'r') as f:
            _cookies = {}
            for row in f.read().split(';'):
                k, v = row.strip().split('=', 1)
                _cookies[k] = v
            return _cookies

    def run(self):
        fmt = 'https://www.pixiv.net/search.php?word={}&order=date_d&p={}'
        urls = [fmt.format(self.search, p) for p in range(1, self.page)]
        total = 1
        for url in urls:
            req = requests.get(url, headers=self.headers, cookies=self.cookies).text
            bs = BeautifulSoup(req, 'lxml').find('ul', class_="_image-items autopagerize_page_element")
            for b in bs.find_all('li', class_="image-item"):
                try:
                    href = b.find('a', class_="work _work ")['href']
                    star = b.find('ul', class_="count-list").find('li').find('a').text
                    self.result.add(("https://www.pixiv.net{}".format(href), int(star)))
                    print(total)
                    total += 1
                except:
                    pass
        pprint(sorted(self.result, key=lambda v: v[1], reverse=True))    # 按star数降序排序

if __name__ == "__main__":
    spider = Pixiv("winter", 100)
    spider.run()
