age = 70
gender = "M" or "F"
family = "Y" or "N"

if gender == "F":
    print("Must work into city region.")
elif gender == "M" and 40 >= age >= 20:
    print("Can work anywhere.")
elif gender == "M" and 60 >= age >= 40:
    print("Must work into city region.")
else:
    print("Mistake")