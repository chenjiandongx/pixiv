from concurrent import futures
import threading

from pprint import pprint
import requests
from bs4 import BeautifulSoup

headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/56.0.2924.87 Safari/537.36'
}


def get_cookies():
    with open("cookies.txt", 'r') as f:
        _cookies = {}
        for row in f.read().split(';'):
            k, v = row.strip().split('=', 1)
            _cookies[k] = v
        return _cookies

cookies = get_cookies()
result = set()
lock = threading.Lock()     # 多线程全局资源锁
total = 1

def crawl(url):
    global total
    req = requests.get(url, headers=headers, cookies=cookies).text
    bs = BeautifulSoup(req, 'lxml').find('ul', class_="_image-items autopagerize_page_element")
    for b in bs.find_all('li', class_="image-item"):
        try:
            with lock:
                href = b.find('a', class_="work _work ")['href']
                star = b.find('ul', class_="count-list").find('li').find('a').text
                result.add(("https://www.pixiv.net" + href, int(star)))
                print(total)
                total += 1
        except:
            pass


def get_urls(search, page):
    fmt = 'https://www.pixiv.net/search.php?word={}&order=date_d&p={}'
    return [fmt.format(search, p) for p in range(1, page)]


if __name__ == "__main__":
    urls = get_urls("summer", 500)
    with futures.ThreadPoolExecutor(32) as executor:
        executor.map(crawl, urls)
    pprint(sorted(result, key=lambda v: v[1], reverse=True))    # 按star数降序排序
