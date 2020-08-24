sozluk = { "halenur" :8, "melisa":11}
print(sozluk)

print(sozluk["halenur"])

sozluk["alenur"] = 10
print(sozluk)

sozlukk = dict(hale=4, melisa=6)
print(sozlukk)
del(sozluk["halenur"])
print(sozluk)
print(len(sozluk))