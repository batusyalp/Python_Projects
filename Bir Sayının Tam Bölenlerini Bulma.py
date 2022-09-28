# kullanıcıdan aldığımız bir sayının tam bölenleri

sayi = int(input('sayi: '))
def tambolenleriBul(sayi):
    tamBolenler = []

    for i in range(1,sayi+1):
        if(sayi%i==0):
            tamBolenler.append(i)
        else:
            continue

    return tamBolenler

result = tambolenleriBul(sayi)
print(result)