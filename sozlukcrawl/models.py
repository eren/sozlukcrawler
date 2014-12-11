__author__ = 'Eren Turkay <turkay.eren@gmail.com>'

from scrapy.utils.project import get_project_settings

from sqlalchemy import create_engine, Column, Integer, String, Date, Time, Text
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Engine = create_engine(URL(**get_project_settings()['DATABASE']))

__SessionMaker = sessionmaker(bind=Engine)
session = __SessionMaker()


def create_tables():
    Base.metadata.create_all(Engine)


class Girdi(Base):
    """
    Girdileri tutan tablo. Scrape ettigimiz butun itemlar veritabanina yaziliyor.

    Su anda database normalization mevcut degil. Girdi icerisinde baslik direkt olarak text
    halinde tutulmakta ve tekrar etmekte. Milyonlarca kayit tutmayi ongormedigimiz icin su anda bir problem
    teskil etmeyecek. Ilerleyen zamanlarda normalization yapilabilir. TODO olarak ekleyelim
    ama buyuk ihtimalle yapilmayacagini da biliyoruz. Yine de bir kenarda dursun :P Never say never.
    """
    __tablename__ = 'girdiler'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column('id', Integer, primary_key=True)
    # TODO: source icin normalization yap. Buradaki source [itu, eksi, uludag] olabilir.
    source = Column('source', String(20))
    girdi_id = Column('girdi_id', Integer)
    baslik_id = Column('baslik_id', Integer)
    # TODO: baslik icin normalization yap, her girdi eklendiginde tekrar etme.
    baslik = Column('baslik', String(255))
    text = Column('text', Text)
    date = Column('date', Date)
    time = Column('time', Time)
    nick = Column('nick', String(255))

    def __repr__(self):
        return '<%Girdi s: %s>' % (self.girdi_id, self.text)

if __name__ == '__main__':
    print 'Connecting to db'
    engine = db_connect()

    print 'Creating tables'
    create_tables(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.close()