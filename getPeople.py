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

#该方法用于获取当天热门前10的视频

#根据视频的信息查找对应的完整信息，并存入

#https://api.bilibili.com/x/player/v2?aid=260132618&cid=822823845该接口包含视频和访问端信息
#或者通过播放量的差值来计算，播放量数据来自页面本身，
#查询出来的数据存入excel文件