a = int(input())
for i in range(1,a):
    if(2<i):
        print(". "+"0 "*(i-2)+". ")
    else:
        print(". "*i)
print(". "*a)
