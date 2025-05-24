a = int(input())
b = int(input())
for i in range(b,0,-1):
    s="  "*(b-i)
    e=0
    for j in range(1,i+1):
        if(i==1 or(i==b)):
            print(s+str(a),end=" ")
            a+=1
        else:
            if(e==0):
                print(s,end="")
                e=1
            if(j==1 or j==i):
                print(a,end=" ")
                a+=1
            else:
                print(" ",end=" ")
    print()
