a = int(input())
for i in range(2*a-1,0,-2):
    sp = " " * ((2*a -1- i)//2)
    s = "*"*i
    print(sp + s)
