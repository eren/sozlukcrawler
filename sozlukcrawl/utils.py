__author__ = 'Eren Turkay <turkay.eren@gmail.com>'

from sqlalchemy import exists
from scrapy.utils.request import request_fingerprint
from .models import Seen, session


def is_request_seen(request):
    return session.query(exists().where(Seen.fingerprint == request_fingerprint(request))).scalar()