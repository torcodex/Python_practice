s = int(input())
a = [1,7,13,19,25]
b = [2,8,14,20,26]
c = [3,4,15,21,27]
d = [4,10,16,22,28]
e = [5,11,17,23,29]
f = [6,12,18,24,30]
for i in range(len(a)):
    if s == a[i]:
        print("Group 1")
for i in range(len(b)):
    if s == b[i]:
        print("Group 2")
for i in range(len(c)):
    if s == c[i]:
        print("Group 3")
for i in range(len(d)):
    if s == d[i]:
        print("Group 4")
for i in range(len(e)):
    if s == e[i]:
        print("Group 5")
for i in range(len(f)):
    if s == f[i]:
        print("Group 6")
