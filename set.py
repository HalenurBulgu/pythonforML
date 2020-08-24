#her eleman eşsizdir.
#elemanlar değiştirilemez.
#sırasızdır.

myset = { "hale", "melisa", 3, 4}
print(myset)
for sets in myset:
    print(sets)
print("hale" in myset)
print("halenur" in myset)

if "hale" in myset:
    print("olala")
    
myset.add("selam")
print(myset)
myset.update(["lale", "sümbül"])
print(myset)

print(len(myset))

myset.remove("hale")
print(myset)


#kaldırılan eleman tekrar silinmeye çalışılıyorsa hata vermemesi için.
myset.discard("hale")
print(myset)

#listeden son elemanı silmek-kimin silindiğini bilemeyiz sıralama yok.
x = myset.pop()
print(myset)

#tüm seti temizlemek
x = myset.clear()
print(myset)
print(len(myset))

set2 = {1,2,3}
set2.pop()
print(set2)
set2.clear()
print(len(set2))
del(set2)


denemeset = set("hale")
print(denemeset)


