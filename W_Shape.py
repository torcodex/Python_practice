a = int(input())
b=0
print("* "*((2*a)-1))
for i in range(a-1,0,-1):
    s="* "*i
    s1=" "*(a-i)
    print(s1+s+(" "*b)+s)
    b+=2
