
'''
@File    :   test.py    
@Contact :   xwz3568@163.com

@Modify Time          @Author    @Version    @Desciption
------------          --------   --------    -----------
2022/11/18 0018 20:40  FuGui      1.0         None
'''

# from bs4 import BeautifulSoup
# code = code.encode("utf-8")
# def get_data(code):
#     bs = BeautifulSoup(code,"html5lib")
#     inf= bs.find('div', class_="article oneColumn pub_border")
#     #("div", attrs={"class": "article oneColumn pub_border"})
#     info = inf.find_all('p')
#     for p in info:
#         print(p.text)
#
# get_data(code)

# import jieba.posseg as pseg
# import jieba.analyse
#
# test_txt = "坚持中国共产党的绝对领导地位，坚定不移的走中国特色社会主义道路"
# # word =jieba.analyse.extract_tags(test_txt,topK)
# words =pseg.cut(test_txt)
#
# for w in words:
#     print(w.word,w.flag)
#
# sort = [(218, '发展'), (150, '建设'), (118, '人民'), (102, '全面')]
# cut_word = [s[1] for s in sort]
# print(cut_word)
import jieba
from wordcloud import WordCloud
import imageio    # 背景轮廓图片 词云背景图：格式png，无色区域无字  [后续有改动]
import matplotlib.pyplot as plt

import pymysql

# #数据库操作
# def DataBase():
#     db = pymysql.connect(host='localhost',
#                          user='pythonSQL',
#                          password='123456wz',
#                          database='report_info',
#                          charset='utf8')
#
#     # 使用 cursor()方法创建一个游标对象 cursor
#     cursor = db.cursor()
#
#     # 使用execute()方法执行SQL查询,测试连接状态
#     print('DBversion:{}'.format(cursor.execute("SELECT VERSION()")))
#     print("数据库连接成功！")
#
#     # # 创建表
#     # sql = """CREATE TABLE cutword_count(
#     #           ID INT NOT NULL,
#     #           分词  CHAR(20),
#     #           出现次数  INT)"""
#     # # 运行sql语句
#     # cursor.execute(sql)
#
#     # 插入数据
#     id_ = int(1)  # id_ tuple_避免歧义
#     for tuple_ in sort:
#         sql = "insert into cutword_count(ID,分词,出现次数) values ({},'{}',{})".format(id_, tuple_[1], tuple_[0])
#         # sql = "UPDATE GDP_table SET year='{}' WHERE ID={};".format(y,id)
#         cursor.execute(sql)  # 运行sql语句
#         db.commit()  # update,delete,insert需要提交事务
#         id_ += 1
#     print("写入成功！")
#     # 关闭游标
#     cursor.close()
#     # 关闭数据库连接
#     db.close()
#
#
# sort =[(218, '发展'), (150, '建设'), (118, '人民'), (102, '全面')]
# DataBase()

# id =1
# for tuple_ in sort:
#     sql = "insert into cutword_count(ID,分词,出现次数) values ({},'{}',{})".format(id,tuple_[1],tuple_[0])
# print(sql)

from pyecharts.charts import Bar
# from pyecharts import options as opts

attr = ['数学','语文','化学','生物','英语','物理']  #标签属性
vl = [123,112,78,56,67,45]   #属性的值

# a = attr[:6]
# v = vl[:6]

sort = [(218, '发展'), (150, '建设'), (118, '人民'), (150, '建设'), (118, '人民'), (150, '建设'), (118, '人民'), (150, '建设'), (118, '人民'), (150, '建设'), (118, '人民')]
x = [s[1] for s in sort[:6]]
print(x)
# sx = sort[:11]
# x = sx[1]
# sy = sort[:11]
# y = sy[0]
# c = (
#     Bar()
#     .add_xaxis(a)
#     .add_yaxis("商家A", v)
#     .render("bar_test.html")
# )

