import datetime
import json

import requests


def getBvList(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }  # 爬虫模拟访问信息
    data = requests.get(url=url, headers=headers)

    # 只保留前十个，并标记日期信息
    data_info = {}
    data_info['time'] = datetime.datetime.now().strftime('%Y-%m-%d')
    data_info['data'] = json.loads(data.text)['data']
    del data_info['data']['list'][11: -1]

    with open('bvlist.json', 'w', encoding='utf-8') as f2:
        json.dump(data_info, f2, ensure_ascii=False, indent=2)
    return data_info


def get_online(url, vlist):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }  # 爬虫模拟访问信息
    vinfo = {}
    i = 1
    for video in vlist['data']['list']:
        # ids = {'aid': "260132618", 'cid': "822823845", 'bvid': "BV1ie411g72J"}
        ids = {'aid': video['aid'], 'cid': video['cid'], 'bvid': video['bvid']}
        r = requests.get(url, timeout=30, headers=headers, params=ids)
        r.raise_for_status()
        r.endcodding = 'utf-8'
        vinfo[i] = r.text
        i = i + 1
    return vinfo


if __name__ == '__main__':
    # 热榜前十
    url_10 = "https://api.bilibili.com/x/web-interface/popular?ps=20&pn=1"
    # 同时在线人数
    url_online = "https://api.bilibili.com/x/player/online/total"
    vlist = getBvList(url_10)
    vinfo = get_online(url_online, vlist)
    print(vinfo)
