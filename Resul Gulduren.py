import random #Bilgisayardan random tercih yapmasını isteyeceğimiz için random modülünü başlangıçta ekliyoruz.

secenek = ["taş", "kağıt", "makas"] #Random modülünün seçim yapabileceği listemizi oluştuyoruz.
taş = secenek[0] #Oyuncunun seçim yapabileceği taş, kağıt ve makası string olarak oluştuyoruz.
kağıt = secenek[1]
makas = secenek[2]
senin_skorun = 0 #Skor hesabı yapalım ve oyun belli bir sayıya ulaşınca bitsin istiyorum.
bilg_skor = 0

#Oyunun kuralları ve oyun ile ilgili bilgileri kullanıcının öğrenmesini hedefliyoruz.
print("Taş,kağıt,makas oyununa hoş geldiniz. Oyunun kuralları basittir:")
print("-Taş makası ezer, kağıt taşı örter ve makas kağıdı keser.")
print("-Başlamak için taş, kağıt veya makas yazıp ENTER tuşuna basmalısınız.")
print("-Oyunu yeniden başlatmak için r + ENTER tuşuna basınız.")
print("-Oyundan çıkmak için q + ENTER tuşuna basınız.\n-5 skoruna ilk ulaşan kazanır. Bol şans!!!\n")

while True:
    bilg_secim = random.choice(secenek) #Bilgisayar secenek kümesinin içinden bir tanesini sececek ve bu bilg_secim olarak tanınacak.
    secim = input("Sezgilerine güven. Taş mı kağıt mı makas mı? ") #Kullanıcının seçimini yapması gerekiyor.
    #Seçimler taş, kağıt, makas, q ve r harfleri olabilir. Aksi halde while döngümüz çalışmaz.

    if secim == taş: #Kullanıcı seçimleri için her ihtimali göz önüne almalıyız. Bunu if döngüsü kullanarak yapıyoruz.
        if bilg_secim == taş: #Kullanıcı seçimi sonrasında bilgisayarın seçimine göre kazananı ve kaybedeni belirliyoruz.
            print("Bilgisayar da taş seçti. Sonuç: Berabere\n")
        elif bilg_secim == makas:
            senin_skorun += 1 #Kazanan hangi tarafsa onun skorunu bir artırıyoruz.
            if senin_skorun == 5:
                print("Bilgisayar makas seçti. Sonuç: Kazandınız")
                print("Senin puanın: {} , Bilgisayarın puanı: {}\n".format(senin_skorun, bilg_skor))
                #format fonksiyonu ile skor hesaplamasını daha kolay yapabiliyoruz.
                print("Oyun bitti. Tebrikler, oyunu kazandınız!!!")
                break
            else:
                print("Bilgisayar makas seçti. Sonuç: Kazandınız")
                print("Senin puanın: {} , Bilgisayarın puanı: {}\n".format(senin_skorun, bilg_skor))

        else:
            bilg_skor += 1
            if bilg_skor == 5:
                print("Bilgisayar kağıt seçti. Sonuç: Kaybettiniz")
                print("Senin puanın: {} , Bilgisayarın puanı: {}\n".format(senin_skorun, bilg_skor))
                print("Oyun bitti. Oyunu maalesef kaybettiniz...")
                break
            else:
                print("Bilgisayar kağıt seçti. Sonuç: Kaybettiniz")
                print("Senin puanın: {} , Bilgisayarın puanı: {}\n".format(senin_skorun, bilg_skor))

    elif secim == kağıt:
        if bilg_secim == kağıt:
            print("Bilgisayar da kağıt seçti. Sonuç: Berabere\n")
        elif bilg_secim == taş:
            senin_skorun += 1
            if senin_skorun == 5:
                print("Bilgisayar taş seçti. Sonuç: Kazandınız")
                print("Senin puanın: {} , Bilgisayarın puanı: {}\n".format(senin_skorun, bilg_skor))
                print("Oyun bitti. Tebrikler, oyunu kazandınız!!!")
                break
            else:
                print("Bilgisayar taş seçti. Sonuç: Kazandınız")
                print("Senin puanın: {} , Bilgisayarın puanı: {}\n".format(senin_skorun, bilg_skor))

        else:
            bilg_skor += 1
            if bilg_skor == 5:
                print("Bilgisayar makas seçti. Sonuç: Kaybettiniz")
                print("Senin puanın: {} , Bilgisayarın puanı: {}\n".format(senin_skorun, bilg_skor))
                print("Oyun bitti. Oyunu maalesef kaybettiniz...")
                break
            else:
                print("Bilgisayar makas seçti. Sonuç: Kaybettiniz")
                print("Senin puanın: {} , Bilgisayarın puanı: {}\n".format(senin_skorun, bilg_skor))

    elif secim == makas:
        if bilg_secim == makas:
            print("Bilgisayar da makas seçti. Sonuç: Berabere\n")
        elif bilg_secim == kağıt:
            senin_skorun += 1
            if senin_skorun == 5:
                print("Bilgisayar kağıt seçti. Sonuç: Kazandınız")
                print("Senin puanın: {} , Bilgisayarın puanı: {}\n".format(senin_skorun, bilg_skor))
                print("Oyun bitti. Tebrikler, oyunu kazandınız!!!")
                break
            else:
                print("Bilgisayar kağıt seçti. Sonuç: Kazandınız")
                print("Senin puanın: {} , Bilgisayarın puanı: {}\n".format(senin_skorun, bilg_skor))
        else:
            bilg_skor += 1
            if bilg_skor == 5:
                print("Bilgisayar taş seçti. Sonuç: Kaybettiniz")
                print("Senin puanın: {} , Bilgisayarın puanı: {}\n".format(senin_skorun, bilg_skor))
                print("Oyun bitti. Oyunu maalesef kaybettiniz...")
                break
            else:
                print("Bilgisayar taş seçti. Sonuç: Kaybettiniz")
                print("Senin puanın: {} , Bilgisayarın puanı: {}\n".format(senin_skorun, bilg_skor))

    elif secim == "r": #Oyunu yeniden başlatmak istediğimizde skorları da sıfırlayarak yeniden başlayabiliriz.
        senin_skorun = 0
        bilg_skor = 0
        print ("Oyun yeniden başlatıldı.")
        continue
    else:
        if secim == "q": #Oyundan çıkmak istediğimizde q tuşu ile çıkabiliyoruz.
            print("Oyundan Çıkıldı.")
            break