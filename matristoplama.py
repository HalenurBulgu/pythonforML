x = [[1,3,5],[2,4,6],[5,6,7]]

y = [[1,6,5],[2,1,6],[5,6,2]]

sonuc = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(y)):
        sonuc[i][j] = x[i][j]+y[i][j]       
print(sonuc)