# *Budget Tracker*
Bu proje **Python + Tkinter** kullanılarak geliştirilmiş basit bir **bütçe takip uygulamasıdır**.

Gelir, gider ve birikim hedeflerinizi takip edebilir, harcama dağılımlarınızı **pasta grafiği** şeklinde görebilirsiniz.  

Proje, **Python GUI geliştirme, CSV veri depolama ve matplotlib ile veri görselleştirme** konularında kendimi geliştirmek amacıyla yapılmıştır.

## Kullanılan Araçlar ve Kütüphanleler
* **Python 3.**
* **Tkinter** → Masaüstü arayüz
* **CSV** → Veri depolama
* **Matplotlib** → Harcama grafiği çizimi
* **datetime** → Tarih/saat işlemleri
* **os** → Dosya kontrol işlemleri

## Kullanıcı İşlemleri
* Kullanıcı kaydı ve giriş yapma

* Gelir ekleme (miktar, sıklık)

* Gider ekleme (kategori bazlı)

* Bakiye hesaplama

* Birikim hedefi belirleme (tarih ile)

* Harcama dağılımını pasta grafiğinde görüntüleme

* Çıkış yapma

## Kurulum
1. **Python yükleyin (3.8 veya üzeri)** 

> [Python indir](https://www.python.org/downloads/).

2. **Gerekli kütüphaneleri yükleyin:**

> pip install matplotlib

Eğer tkinter eksik ise:

*Windows:*
>pip install tk

*Ubuntu/Debian (Linux):*
>sudo apt-get install python3-tk

3. **Proje dosyalarını indirin veya klonlayın:**

>git clone https://github.com/kullaniciadi/Budget-Tracker.git 

>cd Budget-Tracker

## Project Tree
### Budget Tracker
```
├─ budget_tracker.py   # Ana uygulama dosyası  
├─ users.csv           # Kullanıcı bilgileri     
├─ income.csv          # Gelir kayıtları   
├─ expense.csv         # Gider kayıtları   
├─ savings.csv         # Birikim hedefleri   
└─ README.md           # Proje açıklaması
```              






## Algoritma Mantığı
1. Kullanıcı giriş yapar ve kayıt olur `ùsers.csv`.
2. Gelir eklenirse `ìncome.csv` kayıt olur.
3. Gider eklenirse `expense.csv` kayıt olur.
4. Bakiye = Toplam gelir - Toplam gider.
5. Birikim hedefi eklenirse `savings.csv` kayıt olur.
6. Harcama dağılımı matplotlib ile pasta grafiği olarak gösterilir.


## Başlatma

> `python budget_tracker.py`
