# 1) Bir müşterinin adı,soyadı,hesap bakiyesi,tc-kimlik,borç bilgisi class'a gönderilir.Sonra class bu bilgileri dict veya class çağırarak alır.
# 2) Person bilgileri alındıktan sonra atm ye giriş için 2 koşul vardır bunlar: Hesap şifresi ve tc kimlik no dur.Bunlar kontrol edilir.
# 3) Eğer bilgiler doğruysa program çalıştırılır.Bilgiler doğru değilse tekrar bilgilerin girilmesi istenir yalnız bunun için 3 hakk tanınır.3 hakkın sonunda istenen
# bilgiler yanlış girilirse kart bloke olur ve programdan çıkılır.
# 4) Bilgiler doğruysa program adlı fonksiyon çalıştırılır.her şey bu fonksiyon üzerinden işler.Programda Menü adlı fonksiyon çağrılır.Haliyle atm deyiz.Bilgileri doğru girdik
# ve hesaba giriş yaptık karşımıza yapabileceğimiz işlemler çıkması gerekiyor.Menü fonksiyonu çağrıldığında menü fonksiyonunda yaptığımız seçime göre bakiye sorgulama,kredi kartı borcu,bakiye çek,bakiye yatır
# gibi işlemleri fonksiyonlar aracılığıyla çağıracağız.
# 5) hesap bakiye sorgulama için bakiye sorgula fonksiyonu çağrılır ve classtaki bilgiler kullanılır.Şunu da unutmazsak çok iyi olur.Classta dongu adında
# bir değişken tanımlayıp bir işlem bitince programdan çıkmamak için döngü devamlı çalışsın yani while true bloğunda kodlamalıyız.
# Bunun yanında menüye dön fonksiyonu tanımladık bir atm işlemi sonunda ana menüye dönmek için bir seçim kredi kartı iade için başka bir seçim tuşu tanımladık.
# 6) Şimdi diğer işlemlere bakmamız lazım. bakiye sorgulama işlemini yaptık şimdi de para çek para yatır ve çıkış işlemleri...
# 7) para çek ve para yatır işlemlerinde olay şu;
# para çekmek isteyeceğin tutarı giriniz ve yeterli bakiyeniz varsa işleminiz başarılı şekilde gerçekleşmiştir.Eğer yeterli bakiyeniz yoksa menüye dönüp yapmak istediğiniz işlemi seçiniz.
# para yatır işleminde yine kullanıcıdan girdi isteyerek gireceği miktarı alınız ve hesap bakiyeye ekleyiniz.
# 8) çıkış işlemi için ise ana menüden çıkış tercihinde bulununuz ve exit ile programdan çıkınız.

import time
import sys


class Musteri_bilgisi:

    def __init__(self, ad, soyad, hesapsifre, anabakiye, TC_kimlik, borc, yedekbakiye):
        self.name = ad
        self.surname = soyad
        self.password = hesapsifre
        self.balance = anabakiye
        self.identity = TC_kimlik
        self.debt = borc
        self.yedekbakiye = yedekbakiye


hesap_one = Musteri_bilgisi('Doğukan', 'Sürücü', 2302, 5670, '33133409556', 1500, 2500)
hesap_two = Musteri_bilgisi('Zeynep', 'Kaya', 1357, 8279, '33455678145', 2457, 3000)
hesap_three = Musteri_bilgisi('Ali', 'Demir', 2514, 6780, '33455678145', 1200, 2600)
hesap_four = Musteri_bilgisi('Hatice', 'Cevher', 1136, 4250, '33455678145', 290, 1560)

card = hesap_one


class Atm:
    def __init__(self, atm):
        self.AtmName = atm
        self.active_passive = True

    def useraccept(self):
        hak = 3
        sayac = 0
        while hak > 0:
            sifre = int(input('Şifrenizi giriniz: '))
            TC_NO = input('TC numaranızı giriniz: ')
            hak -= 1
            sayac += 1
            if card.password == sifre and card.identity == TC_NO:
                print(
                    f"TEBRİKLERR !! {sayac}.denemenizde İŞLEMİNİZ BAŞARILI, 3 saniye sonra menüye yönlendirileceksiniz.")
                time.sleep(3)
                self.program()
            elif (card.password != sifre or card.identity != TC_NO) and hak != 0:
                print(f"Hatalı şifre veya kimlik bilgisi girdiniz, Kalan hakkınız {hak}")
            elif hak == 0:
                print(""" şifrenizi 3 defa hatalı girdiğinizden dolayı kartınız bloke olmuştur.
                Lütfen en yakın şubemize başvurunuz.
                """)
                sys.exit()

    def program(self):
        secim = self.menu()

        if secim == 1:
            print("bakiye sorgulama seçeneğini seçtiniz.")
            time.sleep(1.5)
            self.bakiye()
        elif secim == 2:
            print("bakiye borç sorgulama seçeneğini seçtiniz.")
            time.sleep(1.5)
            self.kredikartiborc()
        elif secim == 3:
            print("bakiye çekme seçeneğini seçtiniz.")
            time.sleep(1.5)
            self.paracek()
        elif secim == 4:
            print("bakiye yatırma seçeneğini seçtiniz.")
            time.sleep(1.5)
            self.parayatir()
        elif secim == 5:
            self.CIKIS()

    def menu(self):
        print(
            f"\nMerhabalar, {self.AtmName}'a hoşgeldiniz.Sayın {card.name} {card.surname}.\nLütfen aşağıdaki menüden yapmak istediğiniz işlemi seçiniz.\n\n")
        print(' \tİ\tŞ\tL\tE\tM\t\tM\tE\tN\tÜ\tS\tÜ\t '.expandtabs(2).center(55, '*').rjust(60))
        print("""
             [1] Bakiye Sorgulama
             [2] Kredi Kartı Borç Sorgulama
             [3] Para Çekme
             [4] Para Yatırma
             [5] Kart iade """)

        secim = int(input("Seçiminiz: "))

        while secim < 1 or secim > 5:
            secim = int(input("\nLütfen 1 ve 5 arasında geçerli bir değer giriniz.\n:"))

        return secim

    def bakiye(self):
        toplamBakiye = card.balance + card.yedekbakiye
        print("Toplam Bakiyeniz: {} TL'dir.".format(toplamBakiye))
        self.active_passive = False
        self.MENUDON()

    def kredikartiborc(self):
        print("kredi kartı borcunuz {}".format(card.debt))
        self.active_passive = False
        self.MENUDON()

    def paracek(self):
        cekilecek_miktar = int(input("Lütfen çekeceğiniz miktarı giriniz:"))
        toplamBakiye = card.balance + card.yedekbakiye
        yenibakiye = toplamBakiye - cekilecek_miktar

        if card.balance >= cekilecek_miktar:
            print(f"Paranızı çekebilirsiniz. Çekilen para {cekilecek_miktar} 'dir.Kalan paranız ise {toplamBakiye - cekilecek_miktar}")
            self.MENUDON()
        else:
            accept = int(input("Ana bakiyede Yeterli miktarda para yok yedek bakiye sorgulamak ister misiniz ?\n-Evet için 1,Hayır için 2 yi tuşlayınız.\n: "))
            if accept == 1:
                print(f"Yedek bakiyenizde {card.yedekbakiye} miktar bulunmaktadır.Toplam para ise {toplamBakiye} dir.İşleminiz devam ediyor...")
                time.sleep(3)
                if toplamBakiye >= cekilecek_miktar:
                    print(f"Paranızı çekebilirsiniz. Çekilen para {cekilecek_miktar} 'dir.Kalan paranız ise {yenibakiye}")
                    self.active_passive = False
                    self.MENUDON()
                elif toplamBakiye < cekilecek_miktar:
                    print("Malesef yedek bakiye ve ana bakiyeniz toplam miktarı çekeceğiniz miktarı karşılayamıyor.Yeterli bakiye yok. ")
                    self.MENUDON()

            elif accept == 2:
                print("Yedek bakiye sorgulamak istemediniz.İşleminiz sona erdi.")
                time.sleep(1)
                self.MENUDON()

    def CIKIS(self):
        print("Bankamızı tercih ettiğiniz için teşekkür eder, İyi günler dileriz...")
        self.active_passive = False
        exit()

    def MENUDON(self):
        hak = 2
        while hak > 0:
            x = int(input("""\nAna menüye dönmek için lütfen 7 tuşuna basınız. Kart iade için 5'e basınız\nSeçimniz:"""))

            if x == 7:
                self.program()
                break
            elif x == 5:
                self.CIKIS()
                break
            else:
                print("Yanlış tuşa bastınız.Sadece 2 tuşa basabilirsiniz !!!\n")
            hak -= 1

            if hak == 0:
                print("Hakkınız bitti.")
                exit()

    def parayatir(self):
        YatirilacakBakiye = int(input("Lütfen aktaracağınız miktarı giriniz:"))
        yenibakiye_2 = card.balance + card.yedekbakiye + YatirilacakBakiye
        print(f"para yatırma işlemi başarıyla gerçekleşmişir.Hesabınızın yeni bakiyesi {yenibakiye_2} TL'dir.")
        self.MENUDON()


banka = Atm('DODO-BANK')
banka.useraccept()

while banka.active_passive:
    banka.program()