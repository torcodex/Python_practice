a = int(input())
b = int(input())
s = 0
c = 0
r = 1
i = 2
while(True):
    if(r%2==1):
        s=s+(a**i)
    else:
        s=s-(a**i)
    i+=2
    if(c==(b-1)):
        break
    c+=1
    r+=1
print(s)
