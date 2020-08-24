sehirler = [ "ankara", "istanbul", "izmir"]

for sehir in sehirler:
    if sehir == "ankara":
        break
    print(sehir + " için kod =" + sehir[0:3])
    print("****")
    
for sehir in sehirler:
    if sehir == "ankara":
        continue
    print(sehir + " için kod =" + sehir[0:3])
    print("****")