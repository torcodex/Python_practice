a = int(input())
b = int(input())
s = 1 
for i in range(a,b+1):
    if(i%3==0):
        s=s*i
print(s)
