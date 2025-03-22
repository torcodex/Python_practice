a = input()
b = input()
c = a[:len(b)]
d = a[len(a)-(len(b)):len(a):1]
if c==b or d==b:
    print(True)
else:
    print(False)
