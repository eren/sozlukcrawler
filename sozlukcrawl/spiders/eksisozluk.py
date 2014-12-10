# -*- coding: utf-8 -*-

from scrapy import Spider
from scrapy import log
from scrapy.http import Request

from ..items import Girdi


class EksisozlukBaslikSpider(Spider):
    name = "eksibaslik"
    
    def __init__(self, **kwargs):
        super(EksisozlukBaslikSpider, self).__init__(**kwargs)

        assert('urls' in kwargs)
        self.start_urls = kwargs['urls'].split(',')
        self.allowed_domains = ["eksisozluk.com"]

    def parse(self, response):
        log.msg('PARSING', log.DEBUG)

        for sel in response.xpath('//*[@id="entry-list"]/li/article'):
            girdi_id = sel.xpath('./footer/@data-id').extract()[0]
            baslik_id = response.xpath('//*[@id="title"]/a/@href').re(r'--(\d*)')[0]
            date = sel.xpath('./footer/div[2]/span/time/text()').re(r'\d{2}[.]\d{2}[.]\d{4}')[0]
            time = sel.xpath('./footer/div[2]/span/time/text()').re(r'\d{2}[:]\d{2}')[0]
            text = sel.xpath('string(./div)').extract()[0]
            nick = sel.xpath('./footer/div[2]/address/a/span/text()').extract()[0]

            item = Girdi()#
            item['girdi_id'] = girdi_id
            item['baslik_id'] = baslik_id
            item['date'] = date
            item['time'] = time
            item['text'] = text
            item['nick'] = nick

            yield item

        # Sozluk sayfalamayi javascript ile yapiyor, dolayisi ile sayfa linkini XPath ile alamiyoruz ancak kacinci
        # sayfada oldugumuz ve son sayfa html icerisinde yer aliyor. Bu bilgileri kullanarak crawl edilecek bir
        # sonraki sayfanin adresini belirle. SSG degistirmez umarim :(
        current_page = int(response.xpath('//*[@id="topic"]/div[2]/@data-currentpage').extract()[0])
        page_count = int(response.xpath('//*[@id="topic"]/div[2]/@data-pagecount').extract()[0])

        current_url = response.request.url.split('?p')[0]

        next_page = current_page + 1
        # if page_count >= next_page:
        if current_page < 3:
            yield Request('%s?p=%s' % (current_url, next_page))