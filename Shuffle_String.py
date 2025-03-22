a = input()
b = input()
c = ""
for i in range(0,len(a),2):
    if i!=(len(a)-1):
        c=c+a[i]+b[i+1]
    else:
        c=c+a[i]
print(c)
