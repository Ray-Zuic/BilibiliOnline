import requests

def get_html(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }# 爬虫模拟访问信息
    ids = {'aid':"260132618",'cid':"822823845",'bvid':"BV1ie411g72J"}
    r = requests.get(url, timeout=30,headers=headers,params=ids)
    r.raise_for_status()
    r.endcodding = 'utf-8'
    return r.text
#https://api.bilibili.com/x/player/online/total?aid=260132618&cid=822823845&bvid=BV1ie411g72J&ts=55408594
#需要aid,cid,bvid

