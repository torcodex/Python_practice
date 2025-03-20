m = int(input())
p = int(input())
c = int(input())
s1 = m+p >= 90
s2 = p+c >= 90
s3 = m+c >= 90
print(((m>=35)and(p>=35)and(c>=35))and(s1 or s2 or s3))
