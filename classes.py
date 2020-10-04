class Matematik:
    def __init__(self):
        print("çalıştı")
    def topla(self,sayi1,sayi2):
        return sayi1+sayi2
    def cikar(self,sayi1,sayi2):
        return sayi1-sayi2
    def carp(self,sayi1,sayi2):
        return sayi1*sayi2
    def böl(self,sayi1,sayi2):
        return sayi1/sayi2
    
matematik = Matematik()
matematik2 = Matematik()
print(matematik.böl(3,2))
print("toplam=" + str(matematik.böl(3,2)))


class Matematik:
    def __init__(self,sayi1,sayi2):
        self.sayi1=sayi1
        self.sayi2=sayi2
    def topla(self):
        return self.sayi1+self.sayi2
    def cikar(self):
        return self.sayi1-self.sayi2
    def carp(self):
        return self.sayi1*self.sayi2
    def böl(self):
        return self.sayi1/self.sayi2
    
matematik = Matematik(2,78)
matematik2 = Matematik(3,76)
print("toplam=" + str(matematik2.topla()))

class Person:
    def __init__(self, firstname,lastname,age):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
person1=Person("halenur","bulgu","27")
print(person1.age) 

#inheritance
class Worker(Person):
    def __init__(self,salary):
        self.salary = salary
class Customer(Person):
    def __init__(self,creditcardNumber):
        self.creditcardNumber = creditcardNumber
ahmet=Worker()
mehmet=Customer()


