a = int(input())
b = int(a/100)
c = int((a%100)/10)
d = a%10
s = b**3 + c**3 + d**3
if s == a:
    print("True")
else:
    print("False")
