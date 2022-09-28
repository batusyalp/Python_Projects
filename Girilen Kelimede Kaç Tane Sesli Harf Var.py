# kullanıcının girdiği bir kelimedeki sesli harfleri sayan bir kod parçacığı
# Sesli harfler a,e,ı,i,o,ö,u,ü harfleridir ve biz kullanıcıdan bir kelime istediğimizde bu kelimede kaç tane sesli harf
# olduğunu bulan bir program yazdım.Yalnız bizim yazdığımız kelimeler büyük harf küçük harf ile yazılmış da olabilir. Bunun için büyük harfleri de string
# içine dahil ettik ve kelimedeki hangi harfler sesli ise yanına kaçıncı sesli harf olduğunu yazdırmış olacağız.Sonuç olarak kaç tane sesli harf olduğunu görmüş olacağız.


sesli_harfler = 'aeıioöuüAEIİOÖUÜ'
sayac = 0

kelime = input('Bir kelime girin: ')

for harf in kelime:

    if harf in sesli_harfler:
        sayac += 1
        print(f"{harf} , {sayac}")

mesaj = '{} kelimesinde {} sesli harf var.'
print(mesaj.format(kelime, sayac))