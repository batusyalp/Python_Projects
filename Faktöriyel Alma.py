#Kullanıcıdan alınan bir sayının faktöriyeli gösteren kod

sayi_3 = int(input("Bir sayı giriniz: "))
sayac_1 = 1

if sayi_3==0:
    print("0 sayısının faktöriyeli 1 dir.")

if sayi_3>0:
    for i in range(1,sayi_3+1):
        sayac_1=sayac_1*i
    print(f"{sayi_3} sayısının faktöriyeli: {sayac_1} dir.")

elif sayi_3<0:
    print("Negatif sayıların faktöriyeli alınmaz.")