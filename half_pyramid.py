a = int(input())
b = int(input())
s = a
for i in range(b,0,-1):
    s = s+i
s-=1
c = s
for i in range(1,b+1):
    for j in range(i):
        print(c,end=" ")
        c-=1
    print()
