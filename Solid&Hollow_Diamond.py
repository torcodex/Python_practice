a = int(input())
for i in range(1,a+1):
    s="* "*i
    s1=" "*(a-i)
    print(s1+s)
for i in range(a-1,0,-1):
    if(i<=2):
        b = "* "*i
    else:
        b = "* "+"  "*(i-2)+"* "
    b1=" "*(a-i)
    print(b1+b)
