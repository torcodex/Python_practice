a = int(input())
b = int(input())
s=0
for i in range(1,b+1):
    c=str(a)*i
    d=int(c)**2
    s=s+d
print(s)
