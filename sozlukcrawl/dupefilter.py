__author__ = 'Eren Turkay <turkay.eren@gmail.com>'

from datetime import datetime

from scrapy.dupefilter import BaseDupeFilter
from scrapy import log
from scrapy.utils.request import request_fingerprint

from .models import Seen, session, create_tables
from .utils import is_request_seen


class DatabaseDupeFilter(BaseDupeFilter):
    def __init__(self):
        create_tables()

    def request_seen(self, request):
        is_seen = is_request_seen(request)

        if not is_seen:
            log.msg('New URL: %s. Adding it to seen database' % request.url, log.INFO)
            seen = Seen(fingerprint=request_fingerprint(request),
                        url=request.url,
                        last_crawl_time=datetime.now())
            try:
                session.add(seen)
                session.commit()
            except:
                session.rollback()
                raise
            finally:
                session.close()
        else:
            log.msg('[seen] "%s" is seen. Skipping.' % request.url)

        return is_seen