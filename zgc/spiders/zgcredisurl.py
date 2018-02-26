# -*- coding: utf-8 -*-
import scrapy
from zgc.items import RedisItem
from scrapy.spider import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor


class Ecspider(CrawlSpider):
    name = 'zgcspider'
    custom_settings = {
        'ITEM_PIPELINES':{
            'zgc.pipelines.RedisPipeline':300,
        }
    }

    start_urls = ['http://mobile.zol.com.cn/','http://bbs.zol.com.cn/sjbbs/p1.html#c']
    page_link_a = LinkExtractor(allow=(r'/detail_\d+/'))
    link_b = LinkExtractor(allow=(r'/more/\d+_\d+.shtml'))
    page_link_c = LinkExtractor(allow=(r'/sjbbs/p\d+.html#c'))
    page_link_b = LinkExtractor(allow=(r'/more/\d+_\d+_\d+.shtml'))

    rules = (
        Rule(page_link_a,callback="parse_item",follow=True),
        Rule(link_b),
        Rule(page_link_b, callback="parse_item", follow=True),
        Rule(page_link_c, callback="parse_item", follow=True),
    )

    def parse_item(self, response):
        item = RedisItem()
        item['url'] = response.url
        yield item





