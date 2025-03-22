a = int(input())
for i in range(1,a):
    s1 = " "*(a-i)
    if(i<2):
        s = "* "*i
        print(s1+s)
    else:
        s = "* "+"  "*(i-2)+"* "
        print(s1+s)
print("* "*a)
