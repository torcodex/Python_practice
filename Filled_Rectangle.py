a = int(input())
b = int(input())
print("* "*b)
c = "* "+"0 "*(b-2)+"* "
for i in range(a-2):
    print(c)
print("* "*b)
