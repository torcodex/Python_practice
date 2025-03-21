a = input()
b = int(input())
date = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
d = date.index(a)
c = date[(d+(b-1))%7]
print(c)
