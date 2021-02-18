a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = 0
for i in range(a):
    for j in range(b):
        for k in range(c):
            print(i,j,k)
            d+=1
print(d)
