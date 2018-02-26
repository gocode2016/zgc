# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
from zgc.items import MongodbItem
import re
import scrapy
import time
import random
import urllib.request


class Myspider(RedisSpider):
    name = 'mongodburl'
    custom_settings = {
        'ITEM_PIPELINES':{
            'zgc.pipelines.MongodbPipeline':300,
        }
    }
    redis_key = 'zgc_spider:start_urls'


    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/603.2.5 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.5",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Mozilla/5.0 (iPad; CPU OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 Mobile/14F89 Safari/602.1",
        "Mozilla/5.0 (Windows NT 6.1; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/58.0.3029.110 Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.2.5 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.5",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36 OPR/46.0.2597.32",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/59.0.3071.109 Chrome/59.0.3071.109 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:53.0) Gecko/20100101 Firefox/53.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 OPR/45.0.2552.898",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.39",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"
        ]

    def parse(self, response):
        try:
            time.sleep(random.uniform(0.5, 3))
            header = {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                'Connection': 'Keep-Alive',
                'Referer': response.url,
                'User-Agent': random.choice(self.USER_AGENTS)
            }
            if 'bbs.zol.com.cn' not in response.url:
                for box in response.xpath('//div[@class="info-head"]'):
                    url = box.xpath('.//a/@href').extract()[0]
                    yield scrapy.Request(url,callback=self.parse_detail,headers=header)
            else:
                for box in response.xpath('//a[@class="topicurl listbook"]'):
                    url = 'http://bbs.zol.com.cn' + box.xpath('.//@href').extract()[0]
                    yield scrapy.Request(url, callback=self.parse_bbs_detail, headers=header)
        except:
            pass
    #新闻
    def parse_detail(self,response):
        item = MongodbItem()
        item['url'] = response.url
        item['content'] = self.get_content(response)
        if item['content']!='NULL' and item['content']:
            item['title'] = self.get_title(response)
            item['pubtime'] = self.get_pubtime(response)
            item['author'] = self.get_author(response)
            item['daohang'] = self.get_daohang(response)
            item['view'] = '0'
            item['reply'] = '0'
            yield item

    #论坛
    def parse_bbs_detail(self, response):
        item = MongodbItem()
        item['url'] = response.url
        item['content'] = self.get_bbs_content(response)
        if item['content'] != 'NULL' and item['content']:
            item['title'] = self.get_bbs_title(response)
            item['pubtime'] = self.get_bbs_pubtime(response)
            item['author'] = self.get_bbs_author(response)
            item['daohang'] = self.get_bbs_daohang(response)
            item['view'] = self.get_bbs_view(response)
            item['reply'] = self.get_bbs_reply(response)
            yield item

    # 新闻函数
    def get_title(self,response):
        try:
            title = re.compile('<h1>(.*?)</h1>', re.S).findall(response.text)
            for i in title:
                if len(i):
                    title = str(re.sub('<.*?>|\\n|&nbsp;|\xa0|\r|\u3000', '', str(i))).strip().replace(' ', '')
                    title = str(re.sub('<.*?>|\\n|&nbsp;|\xa0|\r|\u3000', '', str(title))).strip().replace(' ', '')
                else:
                    title = 'NULL'
                return title
            if len(title) == 0:
                return 'NULL'
        except:
            pass
    def get_pubtime(self,response):
        try:
            pubtime = response.xpath('//span[@id="pubtime_baidu"]/text()').extract()
            if pubtime:
                pubtime = str(pubtime[0]).strip()
            else:
                pubtime = 'NULL'
            return pubtime
        except:
            pass
    def get_author(self,response):
        try:
            author = response.xpath('//span[@id="author_baidu"]/a/text()').extract()
            if author:
                author = str(author[0]).strip()
            else:
                author = 'NULL'
            return author
        except:
            pass
    def get_daohang(self,response):
        try:
            li = []
            for box in response.xpath('//div[@class="step"]'):
                lei = box.xpath('.//a/text()').extract()
                for i in lei:
                    mu = str(re.sub('<.*?>|\\n|&nbsp;|&gt;', '', str(i))).strip().replace(' ', '')
                    if len(mu):
                        li.append(mu)
                        daohang = '>'.join(li)
                    else:
                        daohang = 'NULL'
                return daohang
        except:
            return 'NULL'
    def get_content(self,response):
        try:
            content = re.compile('ad_in_content">(.*?)<p class="crawl-none">',re.S).findall(response.text)
            for i in content:
                if len(i):
                    content = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;|\xa0|\r|\u3000', '', str(i))).strip().replace(' ', '')
                    content = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;|\xa0|\r|\u3000', '', str(content))).strip().replace(' ', '')
                else:
                    content = 'NULL'
                return content
            if len(content)==0:
                return 'NULL'
        except:
            pass

    #论坛函数
    def get_bbs_title(self,response):
        try:
            title = re.compile('<h1>(.*?)</h1>', re.S).findall(response.text)
            for i in title:
                if len(i):
                    title = str(re.sub('<.*?>|\\n|&nbsp;|\xa0|\r|\u3000', '', str(i))).strip().replace(' ', '')
                    title = str(re.sub('<.*?>|\\n|&nbsp;|\xa0|\r|\u3000', '', str(title))).strip().replace(' ', '')
                else:
                    title = 'NULL'
                return title
            if len(title) == 0:
                return 'NULL'
        except:
            pass
    def get_bbs_pubtime(self,response):
        try:
            pubtime = response.xpath('//span[@class="publish-time"]/text()').extract()
            if pubtime:
                pubtime = str(pubtime[0]).replace('发表于','').strip()
            else:
                pubtime = 'NULL'
            return pubtime
        except:
            pass
    def get_bbs_author(self,response):
        try:
            author = response.xpath('//a[@class="user-name"]/text()').extract()
            if author:
                author = str(author[0]).strip()
            else:
                author = 'NULL'
            return author
        except:
            pass
    def get_bbs_daohang(self,response):
        try:
            li = []
            for box in response.xpath('//div[@class="crumb"]'):
                lei = box.xpath('.//a/text()').extract()
                for i in lei:
                    mu = str(re.sub('<.*?>|\\n|&nbsp;|&gt;', '', str(i))).strip().replace(' ', '')
                    if len(mu):
                        li.append(mu)
                        daohang = '>'.join(li)
                    else:
                        daohang = 'NULL'
                return daohang
        except:
            return 'NULL'
    def get_bbs_content(self,response):
        try:
            content = re.compile('<div id="bookContent">(.*?)<div class="pro-examine"',re.S).findall(response.text)
            for i in content:
                if len(i):
                    content = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;|\xa0|\r|\u3000', '', str(i))).strip().replace(' ', '')
                    content = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;|\xa0|\r|\u3000', '', str(content))).strip().replace(' ', '')
                else:
                    content = 'NULL'
                return content
            if len(content)==0:
                return 'NULL'
        except:
            pass
    def get_bbs_view(self,response):
        try:
            view = response.xpath('//div[@class="title-else"]/em[1]/text()').extract()
            if view:
                view = str(view[0]).strip()
            else:
                view = 'NULL'
            return view
        except:
            pass
    def get_bbs_reply(self,response):
        try:
            reply = response.xpath('//div[@class="title-else"]/em[2]/text()').extract()
            if reply:
                reply = str(reply[0]).strip()
            else:
                reply = 'NULL'
            return reply
        except:
            pass
