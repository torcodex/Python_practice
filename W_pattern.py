a = int(input())
for i in range(1,a+1):
    ls = "* "*i
    s = " " * (a-i)
    rs = "* "*i
    print(ls + s + rs)
