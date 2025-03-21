a = float(input())
if a<0:
    print("Freezing weather")
elif a>=0 and a<10:
    print("Very Cold weather")
elif a>=10 and a<20:
    print("Cold weather")
elif a>=20 and a<30:
    print("Normal")
elif a>=30 and a<40:
    print("Hot")
else:
    print("Very Hot")
