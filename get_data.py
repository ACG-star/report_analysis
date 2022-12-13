"""
@File    :   get_data.py
@Contact :   xwz3568@163.com

@Modify Time          @Author    @Version    @Desciption
------------          --------   --------    -----------
2022/11/18 0018 20:40  FuGui      1.0        防止乱码的字符编码检测库chardet
关于编码解码：https://www.jb51.net/article/211203.htm
"""
#存储路径：r"C:\Users\Administrator\Desktop\BigData"

import chardet #字符编码检测库
import requests
from bs4 import BeautifulSoup


#获取网页源码
def get_url(url):
    header = {
        "User-Agent":"Mozilla / 5.0(Windows NT 10.0; WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36",
        "Cookie":"wdcid = 05 a5e9dc0b78960f;wdlast = 1668775329;wdses = 3 ca438a860a53b64;__asc = fe7a3a811848ac2bdd27fe0bbe9;__auc = fe7a3a811848ac2bdd27fe0bbe9"
    }
    print("开始爬取网页源码……")
    response = requests.get(url,headers=header)
    print(chardet.detect(response.content))  # 编码检测
    response.encoding = chardet.detect(response.content)['encoding']
    code = response.text
    print("源码爬取成功")
    return code
    #编码写法2
    # response.encoding = "utf-8"  #源码：charset=utf-8">
    # content = response.text
    # print(content)


#筛选出需要内容存储本地
def get_data(code):
    print("开始处理网页源码……")
    bs = BeautifulSoup(code,"html5lib")
    inf= bs.find('div', class_="article oneColumn pub_border")
    #("div", attrs={"class": "article oneColumn pub_border"}) #写法2
    info = inf.find_all('p')
    print("正在存储至本地……")
    for p in info:
        with open("report_txt.txt","a",encoding="utf-8") as w:
            w.write(p.text)
    print("处理完成")


if __name__ == '__main__':
    url = "http://www.gov.cn/xinwen/2022-10/25/content_5721685.htm"
    code = get_url(url)
    get_data(code)
