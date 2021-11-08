#problem3
a, b, c = 10, 7, 3
if a != b and b != c and a != c:
    if a > b and b > c:
        print("a")
    elif a < b and b < c:
        print("c")
    else:
        print("none")
else:
    print("Cant")

