# bu kodumuzda private olarak tanımlanmış bir özelliği nasıl public hale getirerek
# ulaşılabilir hale getirebilirizi anlatmaya çalıştım. private durumdaki self.__age = adında yaş bilgisine
# erişebilmek için get ve set metodlarını kullanırız.

class Student:
    def __init__(self, name, age):

        self.name = name # public member
        self.__age = age # private member

    # get() method
    def get_age(self):
        return self.__age

    # set() method
    def set_age(self, age):
        self.__age = age

stud = Student('Jessa', 14)


print('Name:', stud.name, stud.get_age())

#  set() kullanarak privat haldeki değişkeninin değerini değiştiririz.
stud.set_age(16)

# get() metodunu kullanarak private haldeki değişkene erişebiliriz.
print('Name:', stud.name, stud.get_age())