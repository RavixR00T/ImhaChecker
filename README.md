# ImhaChecker - Netflix Hesap Kontrol Aracı

**ImhaChecker.py** Python aracı, Netflix hesaplarını doğrulamak için kullanılır. Hesapların giriş bilgilerini girip, çalışıp çalışmadığını kontrol eder. Çalışan hesaplar bir dosyaya yazılır, çalışmayanlar ise başka bir dosyaya kaydedilir.

## Özellikler
- Netflix hesaplarını hızlı bir şekilde kontrol eder.
- Çalışan hesapları `calisanhesaplar.txt` dosyasına kaydeder.
- Çalışmayan hesapları `calismayanhesaplar.txt` dosyasına kaydeder.
- İşlem sonuçları `islem_durumu.txt` dosyasına yazılır.

## Gereksinimler
Bu programı çalıştırmak için aşağıdaki kütüphanelerin yüklü olması gerekmektedir:
- **mechanize**
- **selenium**
- **webdriver_manager**
- **VPN ANONSURF 4NOMIZER**

Program başında gerekli kütüphaneler otomatik olarak yüklenecektir.

## Kullanım

1. Hesap bilgilerinizi `hesaplistesi.txt` dosyasına şu formatta ekleyin:
kullanici@mail.com:password123
kullanici@mail.com:password123
kullanici@mail.com:password123
Her satırda bir hesap bilgisi olmalıdır.

2. Programı çalıştırın:

python3 ImhaChecker.py


3. Hesapların doğrulama sonuçları:

    Çalışan hesaplar: calisanhesaplar.txt
    Çalışmayan hesaplar: calismayanhesaplar.txt
    İşlem durumu: islem_durumu.txt
    
    
Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için LICENSE dosyasına bakabilirsiniz.
