#problem5
import math
a, b, c = 5, 6, 1
d = (b ** 2) - (4 * a * c)
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"x1={x1}, x2={x2}")
elif d == 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    print(f"x={x1}")
else:
    print("no solutions")

