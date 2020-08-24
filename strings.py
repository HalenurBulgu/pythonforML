# -*- coding: utf-8 -*-
#index
mesaj = "merhaba dünya"
print(mesaj[4])
print(mesaj[4:6])
print(mesaj[0])
newworld="yeni" + mesaj[8:]
print(newworld)
oldworld= "hello" + mesaj[:8]
print(oldworld)
#len
print(len(mesaj))
lasta=mesaj[12:len(mesaj)]
print(lasta)
lasta=mesaj[len(mesaj)-1:len(mesaj)]
print(lasta)
smilarünye=mesaj[len(mesaj)-4:len(mesaj)]
print(smilarünye)
#upper-lower
print(mesaj.upper())
print(mesaj.lower())
print(mesaj.replace("ü","u"))
#replace
mesaj = mesaj.replace("ü","u")
print(mesaj)
mesaj=mesaj.upper()
print(mesaj)
#split-strip
bilgi = "    a1 a2 a3 a4".strip()
print(bilgi.split())
print(bilgi.split(" "))
print(bilgi.split("a"))
print(bilgi.split("a")[3])
world = "w o r l d"
print(world.split())
print(world.split()[0]+ "auw")
#input
ad = input("kimsin kardeş?")
memleket = input ("memleket nire?")
print(ad+memleket)
sayi1 = input("sayi 1 acaba nedir?")
sayi2 = input("sayi 2 acaba nedir nedir?")
print(int(sayi1) + int(sayi2))