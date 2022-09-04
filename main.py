from getPeople import get_html

if __name__ == '__main__':
    #此url为视频详情页的地址
    url = "https://api.bilibili.com/x/player/online/total"
    print(get_html(url))