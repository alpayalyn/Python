print("Selamlar, hoşgeldiniz.")

min_Sayi_1 = input("Lütfen minimum sayı giriniz.")
min_Sayi_1 = int(min_Sayi_1)
max_sayi_2 = input("Lütfen maximum sayı giriniz.")
max_sayi_2 = int(max_sayi_2)
bolunecek_sayi_3 = input("Lütfen bölüm için sayı giriniz.")
bolunecek_sayi_3 = int(bolunecek_sayi_3)

def bolum(min_Sayi_1, max_sayi_2, bolunecek_sayi_3):

    tum_sayilar = list(range(min_Sayi_1, max_sayi_2 +1))
    print(tum_sayilar)
    tam_bolunen_sayilar = []

    i = 0
    j = 0
    for e in tum_sayilar:

        sifirmi = tum_sayilar[j] % bolunecek_sayi_3

        if (sifirmi == 0):

            print(tum_sayilar[j])
            tam_bolunen_sayilar.append(tum_sayilar[j])
            i += 1

        j = j + 1

    return tam_bolunen_sayilar

son_durum = []
son_durum = bolum(min_Sayi_1, max_sayi_2, bolunecek_sayi_3)
print(son_durum)
