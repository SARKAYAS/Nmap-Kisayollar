#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def display_menu():
    """
    Kullanıcıya NMAP komutları menüsünü görüntüler.
    """
    print("""
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
    """)

def run_nmap_command(ip: str, choice: str):
    """
    Kullanıcının seçimine göre uygun NMAP komutunu çalıştırır.
    """
    commands = {
        "0": f"nmap -sV --version-all {ip}",
        "1": f"nmap -A {ip}",
        "2": f"nmap -p- {ip}",
        "3": f"nmap -p3306 --script mysql-info {ip}",
        "4": f"nmap -p3306 --script mysql-brute -d {ip}",
        "5": f"nmap -p22 --script banner {ip}",
        "6": "nmap --script-updatedb",
        "7": f"nmap -O {ip}",
        "8": f"nmap -p {input('Port aralığını giriniz (örn: 20-80): ')} {ip}",
        "9": f"nmap -T4 -F {ip}",
        "10": f"nmap -n {ip}",
        "11": f"nmap --script vuln {ip}",
    }

    if choice in commands:
        print(f"Komut çalıştırılıyor: {commands[choice]}")
        os.system(commands[choice])
    else:
        print("Hatalı seçim yaptınız. Lütfen geçerli bir işlem numarası girin.")

def nmap_kisayol():
    """
    NMAP komutları için kısayollar sunan bir kullanıcı arayüzü.
    """
    while True:
        display_menu()
        choice = input("İşlem numarası giriniz: ")

        if choice == "99":
            print("Çıkış yapılıyor. İyi günler!")
            break

        ip = input("IP adresi giriniz: ").strip()

        if not ip:
            print("Geçersiz IP adresi! Tekrar deneyin.")
            continue

        run_nmap_command(ip, choice)

if __name__ == "__main__":
    nmap_kisayol()
