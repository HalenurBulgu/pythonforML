sayi1 = int(input("lütfen ilk sayıyı giriniz"))
sayi2 = int(input("lütfen ikinci sayıyı giriniz"))
sayi3 = int(input("lütfen üçüncü sayıyı giriniz"))

if (sayi1>=sayi2) and (sayi1>=sayi3):
    enbüyük = sayi1
elif(sayi2>=sayi3) and (sayi2>=sayi1):
    enbüyük=sayi2
else:
    enbüyük=sayi3
print(enbüyük)
    