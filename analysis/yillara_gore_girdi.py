#-*- coding: UTF-8 -*-
__author__ = 'Eren Turkay <turkay.eren@gmail.com>'

from utils import set_app_root, get_logger
set_app_root()

import sys
import argparse

from sqlalchemy import text

from sozlukcrawler.sozlukcrawl.models import session

log = get_logger('yillara-gore')


class Analysis(object):
    def __init__(self, source, baslik_id):
        self.source = source
        self.baslik_id = baslik_id

    def get_distinct_years(self):
        log.debug('Getting distinct years')
        sql = text("SELECT DISTINCT(YEAR(datetime)) FROM girdiler WHERE source=:s AND baslik_id=:b GROUP BY datetime")

        result = session.execute(sql, params=dict(s=self.source, b=self.baslik_id)).fetchall()

        # Convert the result into ints
        return map(lambda x: int(x[0]), result)

    def entry_numbers_in_years(self):
        years = self.get_distinct_years()

        out = []
        for year in years:
            sql = text("SELECT COUNT(girdi_id) FROM girdiler WHERE source=:s AND baslik_id=:b AND YEAR(datetime)=:y")
            result = session.execute(sql, params=dict(s=self.source, b=self.baslik_id, y=year)).fetchone()

            out.append({'year': year, 'month': 1, 'number_of_entires': int(result[0])})

        return out

    def entry_numbers_in_months(self):
        years = self.get_distinct_years()

        out = []
        for year in years:
            for month in xrange(1, 13):
                sql = text("SELECT COUNT(girdi_id) FROM girdiler WHERE source=:s AND baslik_id=:b AND YEAR(datetime)=:y AND MONTH(datetime)=:m")
                result = session.execute(sql, params=dict(s=self.source, b=self.baslik_id, y=year, m=month)).fetchone()

                # Highcharts ile gosterirken Date.UTF 0 indexinden basliyor. Bu
                # yuzden -1 yazmak durumundayiz. Ornegin 2012 yilinin 0. ayi
                # highchart ile cizdirildiginde 2012-1 seklinde gozukmekte
                out.append({'year': year, 'month': month-1, 'number_of_entires': int(result[0])})

        return out


    def total_entries(self):
        sql = text("SELECT COUNT(*) FROM girdiler WHERE source=:s AND baslik_id=:b")
        result = session.execute(sql, params=dict(s=self.source, b=self.baslik_id)).fetchone()

        out = "// toplam girdi sayisi\n"
        out += "[%s, %s]" % (self.source, int(result[0]))

        return out

    def to_js(self, result):
        out = '// %s icin yillara gore girdi dagilimi\n' % self.source
        for item in result:
            out += ("[Date.UTC(%s, %s), %s],\n" % (item['year'], item['month'], item['number_of_entires']))

        return out

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Yillara gore girdi sayisini getir',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-b', '--baslik-id',
                        action='store', type=int,
                        help='Baslik numarasi',
                        required=True)
    parser.add_argument('-s', '--source',
                        action='store', type=str,
                        help='Kaynak (ornegin: eksisozluk, itusozluk, uludagsozluk)',
                        required=True)
    # parser.add_argument('-o', '--output',
    #                     action='store', type=str,
    #                     help='Cikti dosyasi. (ornegin: data.js). Eger verilmezse konsola yazar',
    #                     required=False)
    # parser.add_argument('-d', '--debug',
    #                     action='store', type=bool,
    #                     default='False',
    #                     required=False)

    if len(sys.argv) == 1:
            parser.print_help()
            sys.exit(0)
    elif len(sys.argv) == 2 and (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    analysis = Analysis(args.source, args.baslik_id)
    m = analysis.entry_numbers_in_months()
    print analysis.to_js(m)

    # r = analysis.entry_numbers_in_years()
    # print analysis.to_js(r)
    # print analysis.total_entries()
