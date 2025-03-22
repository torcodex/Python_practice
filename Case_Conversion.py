a = input()
b = a[0].lower()
for i in range(1,len(a)):
    if a[i]==a[i].upper():
        b = b+"-"+a[i].lower()
    else:
        b = b+a[i]
print(b)
