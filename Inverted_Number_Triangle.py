a = int(input())
for i in range(a,0,-1):
    sp = " "*(2*(a-i))
    s = " ".join(str(i) for _ in range(i))
    print(sp + s)
