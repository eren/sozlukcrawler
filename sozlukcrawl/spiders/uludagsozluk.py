# -*- coding: utf-8 -*-
__author__ = 'Eren Turkay <turkay.eren@gmail.com>'

from scrapy import log
from scrapy.http import Request

from datetime import datetime
from urlparse import urlsplit
import re

from . import GenericSozlukSpider
from ..items import Girdi


class ItusozlukBaslikSpider(GenericSozlukSpider):
    name = 'uludagsozluk'

    def __init__(self, **kwargs):
        super(ItusozlukBaslikSpider, self).__init__(**kwargs)

        self.allowed_domains = ['uludagsozluk.com']

    def parse(self, response):
        self.log("PARSING: %s" % response.request.url, level=log.INFO)
        for sel in response.css('ol.entry-list').xpath('./li'):
            girdi_id = sel.css('span.voting').css('a.entryid_a').xpath('./span/text()').re(r'#(\d*)')[0]
            baslik_id = response.xpath('//*[@id="main"]/div/div[1]/div[1]/div/ul/li[1]/ul/li/a/@onclick').re("'(\d*)'")[0]
            baslik = response.css('h1.title').xpath('./a/text()').extract()[0]
            date = sel.xpath('.//a[@class="entry_tarih"]/small/text()').re(r'\d{2}[.]\d{2}[.]\d{4} \d{2}[:]\d{2}')[0]
            text = sel.css('div.entry-p').xpath('string(.)').extract()[0]
            nick = sel.css('span.entry-author').xpath('./a/text()').extract()[0].lower()

            item = Girdi()
            item['source'] = self.name
            item['baslik'] = baslik
            item['girdi_id'] = girdi_id
            item['baslik_id'] = baslik_id
            item['datetime'] = datetime.strptime(date, '%d.%m.%Y %H:%M')
            item['text'] = text
            item['nick'] = nick

            yield item

        current_page = int(response.css('div.pagination').css('li.active').xpath('./a/text()').extract()[0])
        page_count = int(response.xpath('//*[@id="main"]/div/div[3]/ul/li/a')[-2].xpath('text()').extract()[0])
        next_page = current_page + 1

        # Bir sonraki adimda sayfalama linkini dondurmek icin sayfalamadan onceki baslik adresini cikarmamiz gerek.
        # Adres uludagsozluk.com/k/BASLIK/10 seklinde gitmekte. Path'in sayfalamadan onceki kismini al
        url_split = urlsplit(response.request.url)
        current_baslik_url = '%s://%s%s' % (url_split.scheme, url_split.netloc, '/'.join(url_split.path.split('/')[:3]))

        if page_count >= next_page:
        # if current_page < 1:
            yield Request('%s/%s' % (current_baslik_url, next_page))