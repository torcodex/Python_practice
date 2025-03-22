a = int(input())
for i in range(a,0,-1):
    if((i<=2)or(i==a)):
        print((" "*(2*(a-i)))+("* "*i))
    else:
        print((" "*(2*(a-i)))+"* "+"  "*(i-2)+"* ")
