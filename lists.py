# -*- coding: utf-8 -*-
#lists
lists = ["ogrenci1", "ogrenci2", "ogrenci3"]
print(lists)
#append
lists.append("hale")
print(lists)
print(lists[2])
#remove
lists.remove(lists[3])
print(lists)
lists[0] = "halenur"
print(lists)
ülkeler = list(("amerika", "almanya", "italya"))
print(ülkeler)
#len
print(len(ülkeler))
print(ülkeler.clear())
print(ülkeler)
#count
çiçekler = ["lale", "sümbül"]
print(çiçekler.count("lale"))
print("lalelerin sayısı=" + str(çiçekler.count("lale")))
print("sümbülün indexi=" + str(çiçekler.index("sümbül")))
çiçekler.pop(1)
print(çiçekler)
çiçekler.insert(1, "zambak")
print(çiçekler)
çiçekler.reverse()
print(çiçekler)
çiçekler3 = çiçekler.copy()
çiçekler2 = çiçekler
çiçekler2[1] = "yasemin"
print(çiçekler)
print(çiçekler3)
çiçekler.extend(çiçekler3)
print(çiçekler)
çiçekler.sort()
print(çiçekler)
çiçekler.reverse()
print(çiçekler)

