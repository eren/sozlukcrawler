# Sözlük Analiz

Veritabanından istenilen bilgileri çıkarıp highchart verisi olarak döndüren araçları
barındırır. Direkt olarak highcharts uyumlu javascript kodu çıkardığı için highchart
kullanırken `series` kısmına kopyalanıp yapıştırılabilir.

Daha genel olarak JSON ya da CSV çıktısı döndürebilir ancak ilk aşamada hızlı biçimde
veriyi görselleştirmek için bununla uğraşmadım. JSON ve CSV çıktıları üretip bunu
işleyen ve highchart kullanan javascript kodu yazabilecek olan varsa pull request
yapmaktan çekinmesin.

## Kullanım
Proje dizini içerisindeyken analiz araçlarını`python analysis/dosya_ismi.py --help`
ile çalıştırabilirsiniz. Bu size yardım bilgisi getirecektir. İçerisindeki yönergeleri
takip ederek çeşitli analizler gerçekleştirebilirsiniz.