temp = float(input("Enter temperature in Fahrenheit:"))
celsius = (temp - 32) * 5 / 9
print(f"{temp} in Fahrenheit is equal to {celsius} in Celsius")

temp2 = float(input("Enter temperature in Celsius:"))
celsius2 = (temp2 * (9 / 5)) + 32
print(f"{temp2} in Celsius is equal to {celsius2} in Fahrenheit")