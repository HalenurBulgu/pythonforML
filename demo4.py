ogrenciler = ["hale","nur","melisa"]

filetoappend = open("ogrenciler","a")
for ogrenci in ogrenciler:
    filetoappend.write(ogrenci)
    filetoappend.write("\n")




