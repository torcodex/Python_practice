a = int(input())
for i in range(1,a+1):
    s = "* "*i
    s1 = " "*(2*(a-i))
    s2 = " "*(a-i)
    print(s2+s+s1+s)
