a = int(input())
b = int(a/500)
c = int((a%500)/50)
d = int(((a%500)%50)/10)
e = int(((a%500)%50)%10)
print("500: "+str(b)+" 50: "+str(c)+" 10: "+str(d)+" 1: "+str(e))
