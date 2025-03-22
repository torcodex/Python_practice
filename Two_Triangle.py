a = int(input())
for i in range(1,a):
    if(i<=2):
        b=("* "*i)
        s = " "*(4*(a-i))
    else:
        b=("* "+"  "*(i-2)+"* ")
        s = " "*(4*(a-i))
    print(b+s+b)
print("* "*(2*a))
