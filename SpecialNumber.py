a = int(input())
b = int(a/10)
c = a%10
s = b+c==7
q = b==7 or c==7
r = a%7==0
if s or q or r:
    print("Special Number")
else:
    print("Normal Number")
