#problem2
a = 3
b = 5
if (a > 0 and b > 0) or (a < 0 and b < 0):
    print("+")
elif (a > 0 and b < 0) or (a < 0 and b > 0):
    print("-")
elif (a == 0 and b == 0):
    print("cannot divide by 0")

