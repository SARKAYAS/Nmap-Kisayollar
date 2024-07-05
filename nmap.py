#!/usr/bin/env python
# -*- coding utf-8 -*-

import os

def nmap_kisayol():
    print( """
    
    --------------
    NMAP Kısayolları
    --------------
    
    0- Versiyon Taraması İçin                   (nmap -sV --version-all)
    1- Bütün Taramalar İçin                     (nmap -A)
    2- Tüm Portları Taramak İçin                (nmap -p-)
    3- MySQL Hakkında Bilgi Verme               (nmap -p3306 --script mysql-info)
    4- Veritabanına Brute Force Saldırısı       (nmap -p3306 --script mysql-brute -d)
    5- SSL Versiyon Bilgisi Bulma               (nmap -p22 --script banner)
    6- Script Veritabanını Güncelleme           (nmap --script-updatedb)
    
    """ )

    ip = input("Ip adresi giriniz: ")
    no = input("İşlem numarası giriniz: ")
    if (no == "0"):
        os.system("nmap -sV --version-all " + ip)

    if(no=="1"):
        os.system("nmap -A "+ip)

    if(no=="2"):
        os.system("nmap -p- "+ip)

    if(no=="3"):
        os.system("nmap -p3306 --script mysql-info "+ip)

    if(no=="4"):
        os.system("nmap -p3306 --script mysql-brute -d "+ip)

    if (no == "5"):
        os.system("nmap -p22 --script banner " + ip)

    if (no == "6"):
        os.system("nmap --script-updatedb " + ip)


nmap_kisayol()