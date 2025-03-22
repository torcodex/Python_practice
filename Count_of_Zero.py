a = int(input())
b =str(a)
c = 0
for i in b:
    if int(i) == 0:
        c+=1
if c>3:
    print("Count of zeroes is greater than three")
else:
    print("Count of zeroes is not greater than three")
