k=open("musteriler.txt")
#print(k.read())

print(k.readline())
print(k.readline())

for l in k:
    print(l)
    
k.close()


#write
#f=open("musteriler.txt","w")
#oku ve ekleme yapılacak
#f=open("musteriler2.txt","a")
#print(f.read())
#olustur
#f=open("musteriler4.txt","x")
#print(f.read())
#read
#f=open("musteriler2.txt","r")
#print(f.read())

fileToAppend = open("ogrenciler.txt","a")
fileToAppend.write("derya")
fileToAppend.write("\n")
fileToAppend.write("selen")
fileToAppend.close()

fileToAppend = open("ogrenciler.txt","w")
fileToAppend.write("seray")
fileToAppend.write("\n")
fileToAppend.write("selen")
fileToAppend.close()
import os
os.remove("ogrenciler.txt")
if os.path.exists("ogrenciler.txt"):
    os.remove("ogrenciler.txt")
else:
    print("dosya kaldırılmıs")
    
os.rmdir("empty")