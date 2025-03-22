a = int(input())
for i in range(1,a+1):
    if(i<=2):
        print(" "*(a-i)+"* "*i)
    else:
        print(" "*(a-i)+"* "+"  "*(i-2)+"* ")
for i in range(a-1,0,-1):
    if(i<=2):
        print(" "*(a-i)+"* "*i)
    else:
        print(" "*(a-i)+"* "+"  "*(i-2)+"* ")
