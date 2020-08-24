sehirler = [ "ankara", "istanbul", "izmir"]

for sehir in sehirler:
    if sehir == "ankara":
        print(sehir + " için kod =" + "esb")
    else:
        print(sehir + " için kod =" + sehir[0:3])
    print("****")
    
    
for sehir in sehirler:
    if sehir != "istanbul":
        print(sehir + " için kod =" + sehir[0:3])