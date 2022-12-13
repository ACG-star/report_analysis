"""
@File    :   report_analysis.py
@Contact :   xwz3568@163.com

@Modify Time          @Author    @Version    @Desciption
------------          --------   --------    -----------
2022/11/19 0019 11:11  FuGui      1.0         分词，聚类分析，词频统计，词云
"""

import jieba
import jieba.posseg as pseg
from wordcloud import WordCloud
import imageio    # 背景轮廓图片 词云背景图：格式png，无色区域无字  [后续有改动]
import matplotlib.pyplot as plt
import pymysql
from pyecharts.charts import Bar
plt.rcParams['font.sans-serif'] = ['Simhei']    # 解决不能显示中文的问题


# 分词：自定义词典、标注词性
def cutword(txt):
    print("开始分词……")
    # 加载本地词典
    jieba.load_userdict("report_userdict.txt")
    # words = jieba.lcut(txt)
    cut_words = pseg.cut(txt)
    print("分词结束！")
    # 结果是一个列表，首次分词后的结果会存在大量的空格、换行、标点符号、无效单字【'”', '、', '高度', '自治', '的',】
    # 时代/n 呼唤/nr 着/uz
    return cut_words


# 词频统计：词性筛选，排序、本地备份
def count():
    print("开始进行词频统计……")
    dic = {}
    for w,w_pesg in cut_words:
        if w in stopwords or len(w) == 1:
            continue
        elif w_pesg in ['n','vn']:  # 根据词性挑选名词，名动词
            # 备份
            # with open("report_cut.txt", "a") as f:
            #     f.write(w + ' ')
            dic[w] = dic.get(w, 0) + 1  # dict.get(word,0)获取字典对应键的值，如果不存在则返回0 存在则+1
    sort = sorted(zip(dic.values(), dic.keys()), reverse=True)  # 降序
    print('词频统计共{}条数据排序完成'.format(len(sort)))
    # [(218, '发展'), (150, '建设'), (118, '人民'), (102, '全面')……
    return sort


# 数据库操作
def DataBase():
    db = pymysql.connect(host='localhost',
                         user='pythonSQL',
                         password='123456wz',
                         database='report_info',
                         charset='utf8')

    # 使用 cursor()方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用execute()方法执行SQL查询,测试连接状态
    print('DB_version:{}'.format(cursor.execute("SELECT VERSION()")))
    print("数据库连接成功")

    # 创建表 id为主键
    sql = """CREATE TABLE cutword_count(
              ID INT NOT NULL,
              分词  CHAR(20),
              出现次数  INT)"""
    # 运行sql语句
    cursor.execute(sql)

    # 插入数据
    id_ = int(1)  # id_ tuple_避免歧义
    for tuple_ in sort:
        sql = "insert into cutword_count(ID,分词,出现次数) values ({},'{}',{})".format(id_, tuple_[1], tuple_[0])
        # sql = "UPDATE GDP_table SET year='{}' WHERE ID={};".format(y,id)
        cursor.execute(sql)  # 运行sql语句
        db.commit()  # update,delete,insert需要提交事务
        id_ += 1
    print("写入数据库成功")
    # 关闭游标
    cursor.close()
    # 关闭数据库连接
    db.close()


# 词云图、柱状图展示
def wc_show():
    wctxt = open('report_cut.txt','r').read()
    img = imageio.imread_v2('book.png')
    # 设置生成的词云参数 白色背景宽高800 自定义背景图
    wc = WordCloud(background_color="white",
                   width=900,
                   height=900,
                   font_path=r'E:\pycharm\font\simsun.ttc', # 中文字库
                   mask=img,
                   )
    # 传入数据，将对象赋给wcloud  调用wrodcloud库的方法保存本地
    wcloud = wc.generate(wctxt)
    wcloud.to_file('wordcloud.png')  # 保存到本地
    print("词云图片已保存")

    # 控制台展示
    plt.imshow(wcloud)  # 使用plt库显示图片
    plt.axis("off")  # 矩形图表区域内不显示xy轴
    plt.show()


# echarts柱状图展示
def echart():
    print("pyecharts可视化……")
    # sort = [(218, '发展'), (150, '建设'), (118, '人民')………………]
    x = [s[1] for s in sort[:11]]  # 使用列表推导式，取每个元组的第二个元素为横坐标，即关键词为横坐标
    y = [s[0] for s in sort[:11]]  # 取每个元组的第一个元素为纵坐标，即值为纵坐标
    bar = (
        Bar()
        .add_xaxis(x)
        .add_yaxis("关键词", y)
        .render("cutword_bar.html")
    )


if __name__ == '__main__':
    # 加载停用词词库，列表推导式
    stopwords = [line.strip() for line in open('stop_words_哈工大.txt', 'r', encoding='utf-8').readlines()]
    # 读取本地报告文件
    txt = open("report_txt.txt", "r", encoding="utf-8").read()  # 需要声明编码格式
    cut_words = cutword(txt)  # 分词
    sort = count()  # 排序
    DataBase()  # 存入数据库
    echart()  # pyecharts展示前十个关键词
    wc_show()  # 词云展示

