x = 10
print(x)
y = 20
print (y)

x = str(10)
print(x)
y = str(20)
print(y)
x = y[:1] + x[1:]
print(x)
x = int(x)
print(x)

y= int(y)
y = y + 30
print(y)

y,x = x,y
print(x)

nothing = x
x = y
y = nothing
print(x)