# -*- coding: utf-8 -*-

from scrapy import log
from .models import session, Girdi, Engine, create_tables


class DatabasePipeline(object):
    def __init__(self):
        create_tables(Engine)
    
    def process_item(self, item, spider):
        """
        Scrape edilen her girdiyi veritabanina ekle. Bu method sayfa process edildikten, icerisindeki
        bilgiler cekildikten ve Item objesi olusturulduktan sonra her seferinde cagriliyor.

        :param item: Parse edilmis nesne
        :type item: Scrapy item
        :param spider: Su anda calisan, spiders/ dizini altinda belirtilen spiderlardan herhangi biri
        :type spider: Scrapy spider
        :return: Gonderilen Item
        :rtype: Scrapy item
        """
        log.msg('[%s] PROCESSING ITEM [item no: %s, baslik: %s]' %
                (spider.name, item['girdi_id'], item['baslik']),
                level=log.INFO)

        girdi = Girdi(**item)
        try:
            session.add(girdi)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item