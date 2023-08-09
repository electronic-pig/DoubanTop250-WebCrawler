# coding=utf-8
# @Time: 2023/8/9 12:15
# @Author: liyang
# @File: WebCrawler.py
# @Software: PyCharm
import urllib.error
import urllib.request


def saveData(datalist, savepath):
    pass


def getData(baseurl):
    datalist = []
    for i in range(0, 10):  # 调用获取页面信息的函数，10次
        url = baseurl + str(i * 25)
        html = askURL(url)  # 保存获取到的网页源码
        # 逐一解析数据

    return datalist


def askURL(url):
    # 模拟浏览器头部信息
    head = {
        # 用户代理
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalist = getData(baseurl)
    # 2.解析数据
    savepath = ".\\豆瓣电影Top250.xls"
    # 3.保存数据
    saveData(datalist, savepath)
    askURL("https://movie.douban.com/top250?start=0")


if __name__ == "__main__":
    main()
