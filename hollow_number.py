a = int(input())
for i in range(1,a+1):
    for j in range(1,a+1):
        if(i==1 or i==a):
            print(j,end=" ")
        else:
            if(j==1 or j==a):
                print(j,end=" ")
            else:
                print(" ",end=" ")
    print()
