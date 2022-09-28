# manava giden sena hanım 3 meyve türünden isteğine göre seçip kilo ve renklerin seçimine göre ne kadar
# ücret ödeyeceğini gösteren bir kod yazdım.

meyve = input('Hangi meyveyi istiyorsunuz Sena hanım : ')
kac_Kilo=int(input('Kaç kilo istiyorsunuz: '))

if meyve == 'Muz':
    hesap = kac_Kilo*5
    print(f'Ödeyeceğiniz ücret {hesap}')

elif meyve == 'Elma':
    renk = input('Elmanın rengi: ')
    hesap_1 = kac_Kilo * 2
    if renk == 'Kırmızı' :
        print(f'Ödeyeceğiniz ücret {hesap_1}')
    elif renk == 'Sarı':
        print(f'Ödeyeceğiniz ücret {hesap_1}')
    elif renk == 'Yeşil':
        print(f'Ödeyeceğiniz ücret {hesap_1}')

elif meyve == 'Üzüm':
    renk_1 = input('Üzümün rengi: ')
    if renk_1 == 'Mor':
        hesap_2 = kac_Kilo*3
        print(f'Ödeyeceğiniz ücret {hesap_2}')
    elif renk_1 == 'Yeşil':
        hesap_3 = kac_Kilo*3.5
        print(f'Ödeyeceğiniz ücret {hesap_3}')
else:
    print("Sadece Muze,Elma ve Üzüm seçeneklerimiz mevcuttur.")
