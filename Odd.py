a = int(input())
b = int(input())
c=""
while(b>=a):
    if((b%2)==1):
        c = c+str(b)+" "
    b=b-1
print(c)
