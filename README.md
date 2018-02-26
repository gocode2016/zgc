# zgc
中关村手机新闻+论坛爬虫（Scrapy、Redis）

基于Python+scrapy+redis+mongodb的分布式爬虫实现框架

scrapy runspider zgcredisurl.py 主要功能是抓取种子url，保存到redis

scrapy runspider zgcmongodb.py 主要是从redis里面读url，解析数据保存到mongodb （拓展到其他机器,修改REDIS_HOST = "主机ip"，都是从redis里面读url,MONGODB_HOST = "存储服务器ip"）

middlewares.ProxyMiddleware 使用阿布云代理服务器轮换请求IP

                                          中关村手机新闻+论坛mongodb图示
![中关村手机新闻+论坛](https://github.com/renqian520/zgc/blob/master/%E4%B8%AD%E5%85%B3%E6%9D%91%E6%89%8B%E6%9C%BA%E6%96%B0%E9%97%BB%2B%E8%AE%BA%E5%9D%9B.jpg)
