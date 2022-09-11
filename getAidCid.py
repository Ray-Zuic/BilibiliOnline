import json

import requests


# https://api.bilibili.com/x/web-interface/view?bvid=BV1ie411g72J
# 根据bv号获取aid，cid
def getacid(url, params, bvlist):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }  # 爬虫模拟访问信息
    data = requests.get(url=url, headers=headers, params=params)
    data_info = json.loads(data.text)
    return data_info


if __name__ == '__main__':
    ids = {'bvid': "BV1ie411g72J"}
    url_data = "https://api.bilibili.com/x/web-interface/view"
    d = getacid(url_data, ids)
    print(d['data']['aid'])
    print(d['data']['cid'])
