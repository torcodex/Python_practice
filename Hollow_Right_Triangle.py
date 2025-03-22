a = int(input())
for i in range(1,a+1):
    if((i<=2)or(i==a)):
        print("* "*i)
    else:
        print("* "+"  "*(i-2)+"* ")
