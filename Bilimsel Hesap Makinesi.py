# Bu projemizde fonksiyonlar,modüller,control flow konuları ve veri yapılarını kullanarak gelişmiş bir hesap makinesi yaptım.

from math import *
from time import *


def Topla(a, b):
    return a + b


def Cikarma(a, b):
    return a - b


def Carpma(a, b):
    return a * b


def Bolme(a, b):
    return a / b


def usAlma(ussuAlinacakSayi, ussunDerecesi):
    islem1 = pow(ussuAlinacakSayi, ussunDerecesi)
    print("{0}'nın üssü: {1}'dir.".format(ussuAlinacakSayi, islem1))


def Karekok():
    karekokuAlinacakSayi = float(input('Karekökü alınacak sayıyı giriniz: '))
    if karekokuAlinacakSayi >= 0:
        islem2 = sqrt(karekokuAlinacakSayi)
        print("{0}'nın karekökü: {1}'dir.".format(karekokuAlinacakSayi, islem2))

    else:
        print('Negatif sayıların karekökü alınmaz.')


def logaritma():
    loguAlinacakSayi = float(input('Logaritması alınacak sayıyı giriniz: '))
    if loguAlinacakSayi >= 1:
        islem3 = float(log2(loguAlinacakSayi))
        print(f"logaritması alınacak sayı {loguAlinacakSayi}, Sonuç:{islem3} ")
    else:
        print('logaritma kuralını çiğnediniz.')


def dereceyiRadyana():
    derece = float(input('Radyanı alınacak olan dereceyi giriniz: '))
    islem4 = radians(derece)
    print(f"radyanı alınan sayı: {derece} ve sonuç: {islem4}")


def radyaniDereceye():
    radyan = float(input('derecesi alınacak olan radyanı giriniz: '))
    islem5 = degrees(radyan)
    print(f"derecesi alınan sayı: {radyan} ve sonuç: {islem5}")


def faktoriyel():
    faktoriyelAlinacaksayi = int(input('Faktöriyeli alınacak sayıyı giriniz: '))
    islem6 = factorial(faktoriyelAlinacaksayi)
    print(f"faktöriyeli alınan sayı: {faktoriyelAlinacaksayi} ve sonuç: {islem6}")


def mutlak():
    mutlakdegeriAlinacaksayi = float(input('Mutlak değeri alınacak sayıyı giriniz: '))
    islem7 = abs(mutlakdegeriAlinacaksayi)
    print(f"mutlak değeri alınan sayı: {mutlakdegeriAlinacaksayi} ve işlem sonucu {islem7}")


def hipotenus():
    ilksayi = float(input('x eksenindeki sayı: '))
    ikincisayi = float(input('y eksenindeki sayı: '))
    islem8 = pow(ilksayi, 2) + pow(ikincisayi, 2)
    islem9 = sqrt(islem8)
    print(islem9)

def ebob(a,b):
    if a>0 and b>0:
        ebob = gcd(a,b)
        print(f"{a} ve {b} nin ebobu {ebob}")
    else:
        print("Negatif sayılarda ebob hesaplanamaz.")


print("""
         [GELİŞMİŞ HESAP MAKİNESİ PROGRAMI]
                         ↓       
                         ↓ 
                         ↓  
 ********************************************************
 *      \t ----LÜTFEN İŞLEM SEÇİN----     \t        *
 *                                                      *
 *      \t\t1. İşlem = Toplama                      *
 *      \t\t2. İşlem = Çıkarma                      *
 *      \t\t3. İşlem = Çarpma                       *
 *      \t\t4. İşlem = Bölme                        *
 *      \t\t5. İşlem = usAlma                       * 
 *      \t\t6. İşlem =  Karekok                     *
 *      \t\t7. İşlem = logaritma                    *
 *      \t\t8. İşlem = dereceyiRadyana              *
 *      \t\t9. İşlem = radyaniDereceye              *
 *      \t\t10.İşlem = hipotenus                    *
 *      \t\t11.İşlem = faktoriyel                   *
 *      \t\t12.İşlem = mutlak                       *
 *      \t\t13.işlem = ebob                         *
 *      \t\t13.işlem = Çıkmak için q ya basın..."   *
 *                                                      *
 ********************************************************\n""")

while True:
    Islem = input("İşleminizi giriniz : ")

    if (Islem == "q"):
        print("işleminiz sonlandırılıyor...")
        sleep(2)
        print("tekrar bekleriz ... ")
        break

    elif (int(Islem) == 1):
        sayi1 = float(input('1.Sayıyı giriniz: '))
        sayi2 = float(input('2.Sayıyı giriniz: '))
        print("işleminiz yapılıyor...")
        sleep(1)
        print(f"sayı1: {sayi1} sayi2: {sayi2} ve sayı1+sayı2: {Topla(sayi1, sayi2)}")

    elif (int(Islem) == 2):
        sayi1 = float(input('1.Sayıyı giriniz: '))
        sayi2 = float(input('2.Sayıyı giriniz: '))
        print("işleminiz yapılıyor...")
        sleep(1)
        print(f"sayı1: {sayi1} sayi2: {sayi2} ve sayı1-sayi2 : {Cikarma(a=sayi1, b=sayi2)}")

    elif (int(Islem) == 3):
        sayi1 = float(input('1.Sayıyı giriniz: '))
        sayi2 = float(input('2.Sayıyı giriniz: '))
        print("işleminiz yapılıyor...")
        sleep(1)
        print(f"sayı1: {sayi1} sayi2: {sayi2} ve sayı1*sayı2: {Carpma(a=sayi1, b=sayi2)}")


    elif (int(Islem) == 4):
        sayi1 = float(input('1.Sayıyı giriniz: '))
        sayi2 = float(input('2.Sayıyı giriniz: '))
        print("işleminiz yapılıyor...")
        sleep(1)
        print(f"sayı1: {sayi1} sayi2: {sayi2} ve sayi1/sayi2 : {Bolme(a=sayi1, b=sayi2)}")


    elif (int(Islem) == 5):
        ussuAlinacakSayi = float(input('Üssü alınacak sayıyı giriniz: '))
        ussunDerecesi = float(input('Üssün derecesi sayıyı giriniz: '))
        print("işleminiz yapılıyor...")
        sleep(1)
        usAlma(ussuAlinacakSayi, ussunDerecesi)

    elif (int(Islem) == 6):

        print("işleminiz yapılıyor...")
        sleep(1)
        Karekok()


    elif (int(Islem) == 7):

        print("işleminiz yapılıyor...")
        sleep(1)
        logaritma()


    elif (int(Islem) == 8):
        print("işlemniz yapılıyor...")
        sleep(1)
        dereceyiRadyana()


    elif (int(Islem) == 9):
        print("işleminiz yapılıyor...")
        sleep(1)
        radyaniDereceye()


    elif (int(Islem) == 10):
        print("işleminiz yapılıyor...")
        sleep(1)
        hipotenus()


    elif (int(Islem) == 11):
        print("işleminiz yapılıyor...")
        sleep(1)
        faktoriyel()

    elif (int(Islem) == 12):
        print("işleminiz yapılıyor...")
        sleep(1)
        mutlak()

    elif (int(Islem) == 13):
        print("işleminiz ypılıyor..")
        sleep(1)
        a = int(input("1.sayı: "))
        b = int(input("2.sayı: "))
        ebob(a,b)

    else:
        print("Böyle bir işlem yok")