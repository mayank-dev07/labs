string = input("enter string")
a = []
for i in string:
    print(i, end=' ')
    a.append(ord(i)) 
print(a)
# for i in a:
#     print(ord(i))