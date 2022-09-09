import requests
import json

def getBvList(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }  # 爬虫模拟访问信息
    data = requests.get(url=url, headers=headers)
    data_info = json.loads(data.text)
    return data_info


if __name__ == '__main__':
    url_date="https://api.bilibili.com/x/web-interface/popular?ps=20&pn=1"
    vlist = getBvList(url_date)['data']['list']

    print(vlist)
