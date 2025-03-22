a = int(input())
print("* "*a)
b = "* "+"  "*(a-2)+"* "
for i in range(a-2):
    print(b)
print("* "*a)
