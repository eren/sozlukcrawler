# -*- coding: utf-8 -*-
__author__ = 'Eren Turkay <turkay.eren@gmail.com>'

import scrapy


class Girdi(scrapy.Item):
    source = scrapy.Field()
    girdi_id = scrapy.Field()
    baslik_id = scrapy.Field()
    baslik = scrapy.Field()
    text = scrapy.Field()
    date = scrapy.Field()
    time = scrapy.Field()
    nick = scrapy.Field()