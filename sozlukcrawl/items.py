# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Girdi(scrapy.Item):
    girdi_id = scrapy.Field()
    baslik_id = scrapy.Field()
    text = scrapy.Field()
    date = scrapy.Field()
    time = scrapy.Field()
    nick = scrapy.Field()