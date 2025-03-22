a = int(input())
for i in range(1,a+1):
    s1 = "* "*i
    s = " "*(3*(a-i))
    print(s1+s+s1)
for i in range(a-1,0,-1):
    s1 = "* "*(a-i)
    s = " "*(2*i)
    print(s1+s+s1)
