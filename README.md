# Sözlük Crawler


Ekşisözlük, itüsözlük, uludağsözlük gibi popüler sözlüklerden belirtilen başlıklardaki
tüm girdileri alıp, veritabanına yazan crawler. Akademik amaçlar ile kullanılmak üzere
geliştirildi ve dolayısıyla bütün sözlüğü crawl etme veya yeni bir google olma
gibi bir amacı yoktur.

Temel olarak bu proje, bazı popüler başlıklarda yazılan girdilerde herhangi bir örüntü (pattern) olup
olmadığı sorusunu cevaplamak üzere çıktı. Örneğin 'Recep Tayyip Erdoğan' veya 'Türkiye'den
siktir olup gitmek' başlığına hangi ay/yıl daha fazla girdi yazıldı, insanlar en çok hangi
kelimeleri kullandı, en çok girdi yazılan günlerin başka olaylar ile bağlantısı var mı gibi
sorular aklıma gelen birkaç örnek. Veri ortaya çıktıktan sonra üzerine başka analizler
yapmak da mümkün. Eğer ilginizi çekerse analiz fikirlerinizi e-posta atmaktan veya pull-request
yapmaktan çekinmeyin.

Şunu da not etmem gerekir ki lütfen bokunu çıkarmadan kullanın. Bütün sözlüğü download edeceğim,
istekler arasında hiç beklemeyeceğim ve DoS yapacağım diyenler varsa: sen kullanma ulan ayı!

Anahtar kelimeler: sözlük, crawl, scrape, ekşi, ekşisözlük, itüsözlük

# İçindekiler
* [Crawl Edilen Alanlar](#crawl-edilen-alanlar)
* [Kurulum](#kurulum)
* [Veritabanı Ayarları](#veritabanı-ayarları)
	* [SQLIte](#sqlite)
	* [MySQL](#mysql)
	* [PostgreSQL](#postgresql)
* [Kullanım](#kullanım)

## Crawl Edilen Alanlar
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


```
# ev dizinine gir
cd ~

# virtual environment olustur
virtualenv sozlukcrawler.env
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
Proje ORM olarak SQLAlchemy kullanamkta, doğal olarak SQLAlchemy'nin desteklediği bütün
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
    'drivername': 'psycopg2',
    'host': 'localhost',
    'port': '5432',
    'username': 'sozlukcrawl',
    'password': 'sozlukcrawl',
    'database': 'sozlukcrawl'
}
```

Kullanım
--------
