a = int(input())

if a <= 50:
    s = a*2
elif a> 50 and a<=150:
    s = (2*50)+(3*(a-50))
elif a> 150 and a<=250:
    s = (2*50)+(3*100)+(5*(a-150))
elif a>250:
    s = (2*50)+(3*100)+(5*100)+(8*(a-250))
sb = s*0.2
s=s+sb
print(s)
