a = int(input())
if a<=40:
    print(2*a+50)
elif a>40 and a<=60:
    b = 40*2+(a-40)*4
    print(b+50)
elif a>60 and a<=120:
    b = 40*2+(20*4)+(a-60)*6
    print(b+50)
else:
    b = 40*2+(20*4)+(60*6)+(a-120)*8
    print(b+50)
