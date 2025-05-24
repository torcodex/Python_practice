a = int(input())
b = int(input())
s = ""
for i in range(a,b+1):
    c = 0
    for j in str(i):
        c+=(int(j)**len(str(i)))
    if(c==i):
        s = s+str(i)+" "
if(s!=""):
    print(s)
else:
    print(-1)
