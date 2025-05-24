a = int(input())
for i in range(1,a+1):
    c = ""
    for j in range(1,i+1):
        s = " "*(a-i)
        c = c+str(j)+" "
    print(s+c)
for i in range(a-1,0,-1):
    c=""
    for j in range(1,i+1):
        s = " "*(a-i)
        c = c+str(j)+" "
    print(s+c)
