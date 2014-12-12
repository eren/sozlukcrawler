# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy import Spider
from scrapy import log
from scrapy.http import Request
from scrapy.exceptions import CloseSpider

from ..utils import is_request_seen


class GenericSozlukSpider(Spider):
    """
    Her sozluk spider'inda ortak olan isleri burada topla.

    Yeni bir sozluk eklenmesi gerektigi zaman bu class'in genisletilip parse() methodunun
    yazilmasi yeterli.
    """
    def __init__(self, **kwargs):
        super(GenericSozlukSpider, self).__init__(**kwargs)

        if 'urls' not in kwargs:
            raise CloseSpider('URL should be given to scrape')

        self.urls = kwargs['urls'].split(',')
        self.allowed_domains = []

    def start_requests(self):
        self.log('Eliminating already seen web pages. If you think crawler is not working '
                 'please check "seen" table in the database', level=log.WARNING)

        return [Request(i) for i in self.urls if not is_request_seen(Request(i))]

    def parse(self, response):
        raise NotImplementedError