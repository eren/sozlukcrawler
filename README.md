# Sözlük Crawler

Ekşisözlük, itüsözlük, uludağsözlük gibi popüler sözlüklerden belirtilen **başlıklardaki
tüm girdileri** alıp, veritabanına yazan crawler. Akademik amaçlar ile kullanılmak üzere
geliştirildi ve dolayısıyla bütün sözlüğü taramak veya yeni bir google olma
gibi bir amacı yoktur.

Temel olarak bu proje, bazı popüler başlıklarda yazılan girdilerde herhangi bir örüntü (pattern) olup
olmadığı sorusunu cevaplamak üzere çıktı. Örneğin ``Recep Tayyip Erdoğan`` veya ``Türkiye'den
siktir olup gitmek`` başlığına hangi ay/yıl daha fazla girdi yazıldı, insanlar en çok hangi
kelimeleri kullandı, en çok girdi yazılan günlerin başka olaylar ile bağlantısı var mı gibi
sorular aklıma gelen birkaç örnek. Veri ortaya çıktıktan sonra üzerine başka analizler
yapmak da mümkün. Eğer ilginizi çekerse analiz fikirlerinizi e-posta atmaktan veya pull-request
yapmaktan çekinmeyin.

Şunu da not etmem gerekir ki lütfen **bokunu çıkarmadan** kullanın. Bütün sözlüğü download edeceğim,
istekler arasında hiç beklemeyeceğim ve bilerek/bilmeyerek [DoS](https://en.wikipedia.org/wiki/Denial-of-service_attack) yapacağım diyenler varsa: **sen kullanma ulan ayı!**

Anahtar kelimeler: sözlük, crawl, scrape, ekşi, ekşisözlük, itüsözlük

# İçindekiler
* [Desteklenen Sözlükler](#desteklenen-sözlükler)
* [Taranan Alanlar](#taranan-alanlar)
* [Kurulum](#kurulum)
* [Veritabanı Ayarları](#veritabanı-ayarları)
	* [SQLite](#sqlite)
	* [MySQL](#mysql)
	* [PostgreSQL](#postgresql)
* [Kullanım](#kullanım)

## Desteklenen Sözlükler
* [Ekşisözlük](https://www.eksisozluk.com/)
* [İtüsözlük](https://www.itusozluk.com/)
* [Uludağsözlük](https://www.uldagsozluk.com/)

## Taranan Alanlar
Veriler (girdiler) HTML taglerinden ayrılmış ve saf yazı halinde veritabanına eklenmekte. Bu alanlar şunlar:

* Girdinin yazıldığı başlık
* Yazı
* Girdi yazarı (nick)
* Tarih
* Saat
* Girdi numarası
* Başlık numarası


![Örnek](http://i.imgur.com/0jwqw3O.png)


## Kurulum
Sisteminizde öncesinde virtualenv paketinin olduğundan emin olun. Eğer yoksa başlamadan önce
`pip install virtualenv` ile kurun. Aşağıdaki açıklayıcı komutlar ile projeyi kurun. Kullanım
için bir sonraki bölüme bakın.


Not: Buradaki kurulum sadece Ubuntu 14.04 ile test edilmiştir. Ubuntunun diğer
sürümleri ile çalışma olasılığı yüksektir ancak diğer dağıtımlarda paket
isimleri değişebilir.


```
sudo apt-get install build-essential python-dev libffi-dev libmysqlclient-dev \
                     libssl-dev libxml2-dev libxslt1-dev

# ev dizinine gir
cd ~

# virtual environment olustur
virtualenv -p python2.7 sozlukcrawler.env
cd sozlukcrawler.env

# aktive et
source bin/activate

# projeyi getir
git clone https://github.com/eren/sozlukcrawler
cd sozlukcrawler

# bagimliliklari yukle
pip install -r requirements.txt
```

Kurulum yaptıktan sonra `sozlukcrawl/settings.py` dosyasından proje ayarlarını düzenleyin.

## Veritabanı Ayarları
Proje ORM olarak SQLAlchemy kullanmakta, doğal olarak SQLAlchemy'nin desteklediği bütün
veritabanları crawl edilen girdileri saklamak için tutulabilir. Geliştirme ortamında MySQL
öntanımlı olarak kullanılmakta ancak isteğinize göre aşağıdaki veritabanlarını kullanabilirsiniz.


### SQLite
Herhangi bir veritabanı sunucusu kurmak istemiyor ve girdileri dosyaya yazmak istiyorsanız
SQLite sürücüsünü kullanabilirsiniz. Bunun için `settings.py` dosyasında açıklamaları bulunan
satır yorumlarını kaldırmanız yeterli.

```
DATABASE = {
    'drivername': 'sqlite',
    'database': 'db.sqlite'
}
```

### MySQL
MySQL sunucunuzda gerekli kullanıcıyı, parolayı, ve veritabanını ekledikten sonra aşağıdaki
ayarlar ile MySQL kullanımını etkinleştirebilirsiniz.

```
DATABASE = {
    'drivername': 'mysql',
    'host': 'localhost',
    'port': '3306',
    'username': 'sozlukcrawl',
    'password': 'sozlukcrawl',
    'database': 'sozlukcrawl'
}
```

### PostgreSQL
Aynı şekilde kullanıcı adını ve veritabanını ayarladıktan sonra aşağıdaki ayarlar ile
kullanabilirsiniz.

**UYARI**: PostgreSQL kullanmaya başlamadan önce `psycopg2`paketinin kurulu olması gerekmektedir.
Bunu `pip install psycopg2`ile kurunuz.

```
DATABASE = {
    'drivername': 'postgresql+psycopg2',
    'host': 'localhost',
    'port': '5432',
    'username': 'sozlukcrawl',
    'password': 'sozlukcrawl',
    'database': 'sozlukcrawl'
}
```

## Kullanım

Ekşi, İtü veya Uludağsözlükte ilgilendiğiniz başlığın kök linkini
(sayfalama olmaksızın, birinci sayfa) crawler'a vermeniz yeterlidir. Aşağıdaki komutlar
ile crawler'ı başlatabilirsiniz.

Öntanımlı olarak konsola sadece `INFO` logları düşecektir. Eğer yeterince geek iseniz
ve debug çıktısı görmek istiyorsanız komutun sonuna `-L DEBUG` ekleyerek bu çıktıyı
görebilirsiniz.

### Ekşisözlük
`scrapy crawl eksisozluk -a baslik="https://eksisozluk.com/recep-tayyip-erdogan--95281"`

### İtüsözlük
`scrapy crawl itusozluk -a baslik="https://www.itusozluk.com/goster.php/recep+tayyip+erdo%F0an"`

### Uludağsözlük
`scrapy crawl uludagsozluk -a baslik="www.uludagsozluk.com/k/recep-tayyip-erdoğan"`

