import datetime
import json
import time

import requests


def sleeptime(hour, min, sec):
    return hour * 3600 + min * 60 + sec


def getBvList(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Connection': 'close'
    }  # 爬虫模拟访问信息
    data = requests.get(url=url, headers=headers)

    # 只保留前十个，并标记日期信息
    data_info = {}
    data_info['time'] = datetime.datetime.now().strftime('%Y-%m-%d')
    data_info['data'] = json.loads(data.text)['data']
    del data_info['data']['list'][10: -1]

    with open('bvlist.json', 'w', encoding='utf-8') as f2:
        json.dump(data_info, f2, ensure_ascii=False, indent=2)
    return data_info


def get_online(url, vlist):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Connection': 'close'
    }  # 爬虫模拟访问信息
    vinfo = {}
    i = 1
    for video in vlist['data']['list']:
        # ids = {'aid': "260132618", 'cid': "822823845", 'bvid': "BV1ie411g72J"}
        ids = {'aid': video['aid'], 'cid': video['cid'], 'bvid': video['bvid']}
        r = requests.get(url, timeout=30, headers=headers, params=ids)
        r.raise_for_status()
        r.endcodding = 'utf-8'
        try:
            vinfo[i] = {}
            vinfo[i]['time'] = datetime.datetime.now().strftime('%Y-%m-%d')
            vinfo[i]['title'] = video['title']
            vinfo[i]['aid'] = video['aid']
            vinfo[i]['cid'] = video['cid']
            vinfo[i]['bvid'] = video['bvid']
            vinfo[i]['owner'] = video['owner']['name']
            vinfo[i]['count'] = json.loads(r.text)['data']['count']
            vinfo[i]['log'] = 'success'
            i = i + 1
        except(TypeError):
            vinfo[i]['log'] = 'TypeError'
    with open('online.json', 'a', encoding='utf-8') as f2:
        json.dump(vinfo, f2, ensure_ascii=False, indent=2)

    return vinfo


def job():
    # 热榜前十
    url_10 = "https://api.bilibili.com/x/web-interface/popular?ps=20&pn=1"
    # 同时在线人数
    url_online = "https://api.bilibili.com/x/player/online/total"
    # 整个mian是每天9点执行一次
    # 其中的同时在线人数是没5分钟更新一次
    mint = sleeptime(0, 1, 0)
    while 1 == 1:
        try:
            vlist = getBvList(url_10)
        except:
            print("获取视频列表失败，1分钟后重试")
            time.sleep(mint)
            continue
        second = sleeptime(0, 5, 0)
        row = 1
        while 1 == 1:
            try:
                vinfo = get_online(url_online, vlist)
                print("时间：" + datetime.datetime.now().strftime('%Y.%m.%d %H:%M:%S') + "已收集同时在线人数")
            except:
                print("获取同时在线人数失败，5分钟后重试")
            time.sleep(second)


if __name__ == '__main__':
    job()
    # schedule.every().day.at("11:05").do(job)  # 部署在每天的10:30执行job()函数的任务
    # schedule.every().hours.until(datetime.timedelta(hours=12)).do(job)
    # while True:
    #     print("开始执行任务，时间：" + datetime.datetime.now().strftime('%Y.%m.%d %H:%M:%S'))
    #     schedule.run_pending()
