a = int(input())
for i in range(1,a+1):
    s = "* "*i
    s1 = " "*(a-i)
    print(s1+s)
for i in range(a-1,0,-1):
    s = "* "*i
    s1 = " "*(a-i)
    print(s1+s)
