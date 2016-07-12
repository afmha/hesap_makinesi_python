print("Hoşgeldiniz. Hesap Makinesi v1.4 \n Yapımcı: AFMHA \n afmha@hotmail.com | https://www.facebook.com/afmha")

while (True):
    print("\n \n Lütfen seçim yapın:")
    secim = int(input("\n \n [1] => Toplam \n [2] => Çıkartma \n [3] => Bölme \n [4] => Kalan \n [5] => Çarpma \n [99] => Çıkış \n Seçim: "))
    if (secim == 1):
        sayi = input("Kaç kere kendini tekrar etsin: ")
        if isinstance(sayi, int):
            print("Değer alındı.")
        else:
            print("Değer bir doğal sayı girilmeliydi. Otomatik olarak '1' değeri atandı.")
            sayi = 1
        s1 = 0
        while s1 < sayi:
            sayi1 = float(input("1. Sayı: "))
            sayi2 = float(input("2. Sayı: "))
            sonuc = sayi1 + sayi2
            print(sonuc)
            s1 = s1 + 1

    elif (secim == 2):
        sayi = input("Kaç kere kendini tekrar etsin: ")
        if isinstance(sayi, int):
            print("Değer alındı.")
        else:
            print("Değer bir doğal sayı girilmeliydi. Otomatik olarak '1' değeri atandı.")
            sayi = 1
        s1 = 0
        while s1 < sayi:
            sayi1 = float(input("1. Sayı: "))
            sayi2 = float(input("2. Sayı: "))
            sonuc = sayi1 - sayi2
            print(sonuc)
            s1 = s1 + 1

    elif (secim == 3):
        sayi = input("Kaç kere kendini tekrar etsin: ")
        if isinstance(sayi, int):
            print("Değer alındı.")
        else:
            print("Değer bir doğal sayı girilmeliydi. Otomatik olarak '1' değeri atandı.")
            sayi = 1
        s1 = 0
        while s1 < sayi:
            sayi1 = float(input("1. Sayı: "))
            sayi2 = float(input("2. Sayı: "))
            sonuc = sayi1 / sayi2
            print(sonuc)
            s1 = s1 + 1

    elif (secim == 4):
        sayi = input("Kaç kere kendini tekrar etsin: ")
        if isinstance(sayi, int):
            print("Değer alındı.")
        else:
            print("Değer bir doğal sayı girilmeliydi. Otomatik olarak '1' değeri atandı.")
            sayi = 1
        s1 = 0
        while s1 < sayi:
            sayi1 = float(input("1. Sayı: "))
            sayi2 = float(input("2. Sayı: "))
            sonuc = sayi1 % sayi2
            print(sonuc)
            s1 = s1 + 1

    elif (secim == 5):
        sayi = input("Kaç kere kendini tekrar etsin: ")
        if isinstance(sayi, int):
            print("Değer alındı.")
        else:
            print("Değer bir doğal sayı girilmeliydi. Otomatik olarak '1' değeri atandı.")
            sayi = 1
        s1 = 0
        while s1 < sayi:
            sayi1 = float(input("1. Sayı: "))
            sayi2 = float(input("2. Sayı: "))
            sonuc = sayi1 * sayi2
            print(sonuc)
            s1 = s1 + 1
    elif (secim == 99):
        print("Çıkış işlemi gerçekleştiriliyor.")
        print(exit())
    else:
        print("Çıkış işlemi gerçekleştiriliyor.")
        print(exit())
