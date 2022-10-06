class sirket():

    def __init__(self,ad):
        self.ad = ad
        self.dongu = True

    def program(self):
        secim = self.menuSecim()

        if secim == 1:
            self.calisanEkle()

        if secim == 2:
            self.calisanCikar()

        if secim == 3:
            ay_yil_secim = input("Yillik bazda görmek ister misiniz(e/h) ?")
            if ay_yil_secim == "e":
                self.verilecekMaasGoster(hesap="y")
            else:
                self.verilecekMaasGoster()

        if secim == 4:
            self.maaslariVer()


    def menuSecim(self):
        secenek = int(input(f"**** {self.ad} otomasyonununa hoş geldiniz ****\n\n1-Çalışan ekle\n2-Çalışan çıkar\n3-Verilecek Maaş Goster\n4-Maaslari Ver\nSeçiminizi giriniz: "))

        while secenek<1 or secenek>6:
            secenek = int(input("lütfen 1-6 arasında belirtilen seçeneklerden birini giriniz."))

        return secenek

    def calisanEkle(self):
        id = 1

        ad = input("Çalışanın adını giriniz: ")
        soyad = input("Çalışanın soyadını giriniz: ")
        yas = input("Çalışanın yas giriniz: ")
        cinsiyet = input("Çalışanın cinsiyet giriniz: ")
        maas= input("Çalışanın maaş giriniz: ")

        with open("calisanlar.txt","r",encoding="utf-8") as file:
            calisanListesi = file.readlines()

        if len(calisanListesi) == 0:
            id = 1
        else:
            # buradaki amaç bir veri eklemek istediğimizde txt dosyasının içi boş değilse dosyadaki son verinin sıra numarsını 1 arttırmalıyızki ekleyeceğimiz verinin numarsı o olsun.
            with open("calisanlar.txt","r",encoding ="utf-8") as file:
                id =int(file.readlines()[-1].split(")")[0])+1    #bir  liste döner ve en son verisini alır bunu da splitler..

        with open("calisanlar.txt", "a+", encoding="utf-8") as file:
            file.write("{})-{}-{}-{}-{}-{}\n".format(id,ad,soyad,yas,cinsiyet,maas))


    def calisanCikar(self):
        with open("calisanlar.txt","r",encoding="utf-8") as file:
            calisanlar = file.readlines()


        calisanlar_listesi = []

        for calisan in calisanlar:
            calisanlar_listesi.append(" ".join(calisan[:-1].split("-")))

        for calisan in calisanlar_listesi:
            print(calisan)

        secim = int(input("lütfen çıkarmak istedğiniz çalışanın numarasını giriniz(1-{}:".format(len(calisanlar_listesi))))
        while secim<1 or secim>len(calisanlar_listesi):
            secim = int(input("lütfen (1-{}) arasında numara giriniz: ".format(len(calisanlar_listesi))))

        calisanlar.pop(secim-1)

        sayac = 1

        calisanlar_listesi = []
        for calisan in calisanlar:
            calisanlar_listesi.append(str(sayac)+ ")" + calisan.split(")")[1])
            sayac+=1

        with open("calisanlar.txt","w",encoding="utf-8") as file:
            file.writelines(calisanlar_listesi)


    def verilecekMaasGoster(self,hesap = "a"):
        """
        hesap :
            a ise aylik,
            y ise yillik hesap

        """

        with open("calisanlar.txt","r",encoding="utf-8") as file:
            calisanlistesi = file.readlines()

        maaslistesi = []

        for calisan in calisanlistesi:
            maaslistesi.append(int(calisan.split("-")[-1]))

        if hesap == "a":
            print("Bu ay toplam vermeniz gereken maaş: {}".format(sum(maaslistesi)))
        else:
            print("Bu yıl toplam vermeniz gereken maaş: {}".format(sum(maaslistesi)*12))


    def maaslariVer(self):

        with open("calisanlar.txt", "r", encoding="utf-8") as file:
            calisanlistesi = file.readlines()

        maaslistesi = []

        for calisan in calisanlistesi:
            maaslistesi.append(int(calisan.split("-")[-1]))

        toplamMaas = sum(maaslistesi)

        ## bütçeden maaşı alma ##

        with open("butce.txt","r",encoding="utf-8") as file:
            tbutce = int(file.readlines()[0])

        toplambutce = tbutce - toplamMaas

        with open("butce.txt","w",encoding="utf-8") as file:
            file.write(str(toplambutce))


sirket = sirket("doğukansrc")


while sirket.dongu:
    sirket.program()
