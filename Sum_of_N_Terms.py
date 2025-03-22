a = int(input())
b = int(input())
s = 0
c=0
d = 1
for i in range(b):
    if(c==0):
        s += (a**d)
        c=1
    else:
        s += ((-a)**d)
        c=0
    d+=2
print(s)
