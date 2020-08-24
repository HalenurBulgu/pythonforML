sayi = int(input("lütfen bir sayı giriniz"))
faktoriyel = 1
if sayi<0:
    print("negatif sayiların faktoriyeli olmaz")
elif sayi==0:
    print("sonuc=1")
else:
    for i in range(1,sayi+1):
        faktoriyel=faktoriyel*i
    print(faktoriyel)
    
    
    


       
    


