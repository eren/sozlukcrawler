__author__ = 'Eren Turkay <turkay.eren@gmail.com>'

from datetime import datetime

from scrapy.dupefilter import BaseDupeFilter
from scrapy.utils.request import request_fingerprint
from scrapy import log

from sqlalchemy import exists

from .models import Seen, session, create_tables


class DatabaseDupeFilter(BaseDupeFilter):
    def __init__(self):
        create_tables()

    def request_seen(self, request):
        is_seen = session.query(exists().where(Seen.fingerprint == request_fingerprint(request))).scalar()

        if not is_seen:
            log.msg('[seen] New URL: %s. Adding it to database' % request.url, log.INFO)
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