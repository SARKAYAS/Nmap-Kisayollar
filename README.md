
# NMAP Kısayolları ile Tarama Aracı

Bu Python uygulaması, NMAP komutlarını kullanıcı dostu bir arayüz ile kullanmanızı sağlar. Uygulama, sık kullanılan NMAP tarama işlemleri için hazır kısayollar sunar. Bu sayede IP adreslerini hızlı ve etkili bir şekilde analiz edebilirsiniz.

## Özellikler

 **Versiyon Taraması:** Servis versiyonlarını detaylı olarak tarar.
 **Bütün Taramalar:** Hedef üzerinde kapsamlı bilgi toplama.
 **Tüm Portların Taranması:** Belirli veya tüm portlar üzerinde tarama yapar.
 **MySQL Bilgi ve Brute Force Taraması:** MySQL'e özel bilgiler toplar ve brute force saldırıları düzenler.
 **SSL Versiyon Tespiti:** Açık SSL portlarındaki banner bilgilerini toplar.
 **Güvenlik Açığı Taraması:** Hedefteki bilinen güvenlik açıklarını kontrol eder.
 **Hızlı ve Belirli Port Taramaları:** Hedef üzerinde belirli veya hızlı taramalar yapar.
 **İşletim Sistemi Tespiti:** Hedefin işletim sistemini tanımlar.

## Gereksinimler

 **Python 3.x**
 NMAP yüklü olmalıdır. NMAP kurulu değilse aşağıdaki komutla yükleyebilirsiniz:
  ```bash
  sudo apt install nmap
  ```

## Kurulum

1. Bu projeyi klonlayın:
   ```bash
   git clone https://github.com/kullaniciadi/nmap-kisayol.git
   cd nmap-kisayol
   ```

2. Uygulamayı çalıştırın:
   ```bash
   python3 nmap_kisayol.py
   ```

## Kullanım

1. Program çalıştırıldığında aşağıdaki menü görüntülenir:

   ```plaintext
   --------------
   NMAP Kısayolları
   --------------
   0- Versiyon Taraması İçin                     (nmap -sV --version-all)
   1- Bütün Taramalar İçin                       (nmap -A)
   2- Tüm Portları Taramak İçin                  (nmap -p-)
   3- MySQL Hakkında Bilgi Verme                 (nmap -p3306 --script mysql-info)
   4- Veritabanına Brute Force Saldırısı         (nmap -p3306 --script mysql-brute -d)
   5- SSL Versiyon Bilgisi Bulma                 (nmap -p22 --script banner)
   6- Script Veritabanını Güncelleme             (nmap --script-updatedb)
   7- İşletim Sistemi Tespiti                    (nmap -O)
   8- Belirli Port Aralığını Taramak İçin        (nmap -p <başlangıç>-<bitiş>)
   9- Hızlı Tarama Yapmak İçin                   (nmap -T4 -F)
   10- DNS Çözümleme Yapmamak İçin               (nmap -n)
   11- Güvenlik Açığı Taraması                   (nmap --script vuln)
   99- Çıkış
   ```

2. **Adım 1:** Bir işlem numarası seçin.
3. **Adım 2:** Hedef IP adresini girin.
4. **Adım 3:** Program seçilen NMAP komutunu çalıştırır ve sonuçları terminalde gösterir.

### Örnek Kullanım

```plaintext
--------------
NMAP Kısayolları
--------------
0- Versiyon Taraması İçin                     (nmap -sV --version-all)
...
99- Çıkış
İşlem numarası giriniz: 7
IP adresi giriniz: 192.168.1.1
Komut çalıştırılıyor: nmap -O 192.168.1.1
```

Bu örnekte, hedef IP adresinin işletim sistemi tespiti yapılmıştır.

## Katkıda Bulunma

1. Projeyi fork edin.
2. Geliştirmeler yapın ve test edin.
3. Pull Request gönderin.


### Notlar
- Program, **sudo** yetkileri gerektirebilecek komutlar çalıştırabilir.
- Tarama işlemleri sırasında hedef sistemin güvenlik politikalarını ihlal etmediğinizden emin olun.

```

