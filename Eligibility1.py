m = int(input())
p = int(input())
c = int(input())
q = m+p>=100
w = m+c>=100
e = p+c>=100
r = m+p+c>=180
u = q or w or e
print(r and u)
