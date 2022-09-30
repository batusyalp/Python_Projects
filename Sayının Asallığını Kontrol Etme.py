#Asal mı değil mi uygulaması
#Bir sayının asal olup olmadığını asallık şartlarını göz önünde bulundurarak fonksiyon ve for yapısı yardımıyla ele aldım.

sayi = int(input("Sayıyı giriniz : "))

def Asalsayi(number):
    if number==1 :
        print('Asal değildir.')

    elif number>1:
        for i in range(2,number):
            if number%i==0:
                print(f"{number} Asal değildir.")
                break
        else:
            print(f"{number} Asaldir")
    else:
        print("pozitif olmayan sayılar asal değildir.")

Asalsayi(sayi)
