import random

while True:
    print("Taş Kağıt Makas oyununa hoş geldiniz!")
    print("1. Taş")
    print("2. Kağıt")
    print("3. Makas")
    print("4. Çıkış")

    # Kullanıcının seçimini alınır
    user_choice = int(input("Lütfen seçiminizi yapın (1-4): "))

    if user_choice == 4:
        break

    # Bilgisayarın seçimini rastgele belirleyin
    computer_choice = random.randint(1, 3)

    # Seçimler karşılaştırılır
    if user_choice == computer_choice:
        print("Berabere!")
    elif user_choice == 1 and computer_choice == 3:
        print("Tebrikler, kazandınız! Taş Makası kırar.")
    elif user_choice == 2 and computer_choice == 1:
        print("Tebrikler, kazandınız! Kağıt Taşı sarar.")
    elif user_choice == 3 and computer_choice == 2:
        print("Tebrikler, kazandınız! Makas Kağıdı keser.")
    else:
        print("Üzgünüm, kaybettiniz. Tekrar deneyin.")
