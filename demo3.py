# =============================================================================
# asal sayıları bulma========================================================================

sayi = int(input("bir sayı giriniz"))

asalmi = True

for i in range(2, sayi):
    if sayi%i == 0:
        asalmi = False
        break
if asalmi:
    print ("asaldır")
else:
    print("asal değil")