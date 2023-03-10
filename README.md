#Gerekli Kütüphaneler:

#-PyQt5 (PyQt6 Kullanabilirsiniz fakat sayfaları içeren .py uzantılı dosyaların hepsinde 'PyQt5' importlarını 'PyQt6' olarak değiştirmeniz gerekir.)

#-PyQt5'in içerdiği QtCore, QtGui, QtWidgets eklentileri

#-SQL3


Bu projenin amacı hastaneler ve sağlık kurumlarının kayıtlarını detaylı bir şekilde tutup, tutulan kayıtlar üzerinde işlemler yapılmasını sağlamaktır.
Bu proje CRUD işlemlerini içerir.
'main.py' dosyasını Python 3 ve üzeri bir sürümde çalıştırdığınız zaman karşınıza uygulamanın arayüzü gelecektir.
Bu arayüzdeki belirtilen buttonlar sayesinde gerekli işlemlerin yapılmasını sağlayan pencereler açılacaktır ve ilgili pencere açıldığı zaman ana menü kapanacaktır.
Ana Sayfa dışındaki tüm pencerelerde 'Ana Sayfaya Dön' buttonu kullanılarak ana sayfaya dönülebilir.

Sayfalar sırasıyla:
-Yeni Kayıt (Gerekli bilgileri girerek yeni bir hasta kaydı oluşturmanızı sağlar)
-Kayıt Görüntüle (Eklenilen kayıtların görüntülenmesini sağlar)
*WIP* -Kayıt Düzenle (Seçilen kaydın düzenlenmesini sağlar)
-Kayıt Sil (Seçilen kaydın silinmesini sağlar)

Uygulamada CRUD İşlemlerinin hepsi sıralı ve başarılı şekilde yapılmıştır.

ÖNEMLİ NOT: Proje macOS işletim sistemi üzerinde yapılmıştır bu yüzden Windows ya da Linux tabanlı bir işletim sistemi üzerinde çalıştırdığınızda görsel hatalar (Font ve Button yazılarının sığmaması gibi) oluşabilir.
Fakat belirtilen görsel hatalar uygulamanın çalışmasını engelleyen bir durum yaratmamaktadır.
