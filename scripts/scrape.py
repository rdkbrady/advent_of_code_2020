import requests
import re
from lxml import html
from io import StringIO

headers = {
'authority': 'adventofcode.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document',
'referer': 'https://adventofcode.com/2020/day/2',
'accept-language': 'en-US,en;q=0.9',
'cookie': '_ga=GA1.2.805595945.1606803955; _gid=GA1.2.748889626.1606803955; session=53616c7465645f5f6d8cff0a87776eab1e5f75ed23e6ddaf9eb0c7fb9aab9dcb1de53c3476516643c2744ddc818805ce'
}

def get_data(day, split='\n'):
    r = requests.get("https://adventofcode.com/2020/day/{}/input".format(day), headers = headers)
    return r.text[:-1].split(split)

def get_test_data(day, split = '\n'):
    r = requests.get("https://adventofcode.com/2020/day/{}".format(day), headers=headers)
    return([str(l)[:-1].split(split) for l in html.parse(StringIO(r.text)).xpath('//pre/code/text()')])