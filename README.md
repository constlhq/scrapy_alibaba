# 阿里巴巴推出了数据开放平台，可以通过接口拿数据了，肯定每天有次数限制，前提是要有公司的memberId，毕竟获取memberId比获取完整信息要简单一点。
# 获取于2016年上半年的数据997254条，需要移步下载，[百度云链接_密码: 1234](https://pan.baidu.com/s/1qZdILLa)
# 爬一些就会被封ip。不用尝试了。
# 基于scrapy爬取ali巴巴[移动版](http://m.1688.com)的供货商公司信息的爬虫
*依赖包：BeautifulSoup,scrapy*

### 运行方法
```
cd ./scrapy_alibaba
scrapy crawl ali88
```
### 数据保存在本地mongdb:27017/alibaba_test数据库下,可在setting.py中修改mongo设置,更多参考[scrapy文档](https://docs.scrapy.org/en/latest/)。

![运行结果](./screenshot.png)
*注：截图中地理坐标和区域是后续地理编码处理加上的，不包含在这里*
