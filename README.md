# report_analysis
基于网页的二十大报告分析


get_data：依托requests爬虫与beautifulsoup库爬取网页二十大报告原文，编码使用chardet自动处理，结果保存本地文本文档

report_analysis：使用结巴库，添加用户自定义词典与哈工大停用词进行分词；使用wordcloud库对结果做词云可视化；除此之外可视化使用pyecharts

对关键词词频统计结果存至mysql数据库中

cutword_bar：图表的网页可视化

其他为过程性文件
