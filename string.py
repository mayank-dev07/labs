string = "Rahul is a college student, Rahul is doing his master degree"

x = string.count('Rahul')
print(x)

y = string.split()
print(y)
for i in range(0,len(y)):
    if(y[i] == 'Rahul'):
     print(i)

z = string.replace("R","r")
print(z)