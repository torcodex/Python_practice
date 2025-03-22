a  = input()
if a.isdigit():
    print("Digit")
elif a.upper()==a and a.isalpha():
    print("Uppercase Letter")
elif a.lower()==a and a.isalpha():
    print("Lowercase Letter")
else:
    print("Special Character")
