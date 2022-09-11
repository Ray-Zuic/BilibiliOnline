import json

import openpyxl
import requests


# 热门前十，从早上9点-晚上9点
# 1.获取10个视频的bv号,并保存入json
def getBvList(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }  # 爬虫模拟访问信息
    data = requests.get(url=url, headers=headers)
    data_info = json.loads(data.text)
    with open('bvlist.json', 'w', encoding='uth-8') as f2:
        json.dump(data_info, f2, ensure_ascii=False, indent=2)
    return data.text


# 2.根据bv号获取每个视频的相关信息，并保存入json
def getacid(url, params, bvlist):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }  # 爬虫模拟访问信息
    data = requests.get(url=url, headers=headers, params=params)
    data_info = json.loads(data.text)
    return data_info


# 3.根据aid cid bvid获取同时观看人数，并将其存入xlsx
def get_html(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }  # 爬虫模拟访问信息
    ids = {'aid': "260132618", 'cid': "822823845", 'bvid': "BV1ie411g72J"}
    r = requests.get(url, timeout=30, headers=headers, params=ids)
    r.raise_for_status()
    r.endcodding = 'utf-8'
    return r.text


# 4.每5分钟收集

# 固定10位日更up的视频，从早上9点-晚上9点


if __name__ == '__main__':
    # 初始化xlsx文件，准备写入
    table = ["time", "videoname", "aid", "cid",
             "bvid", "online", "region", "supplier"]

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Sheet1"
    row = 1
    for i in range(len(table)):
        sheet.cell(row, i + 1, table[i])
    workbook.save(filename="online.xlsx")
