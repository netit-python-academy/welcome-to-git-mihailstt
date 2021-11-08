month = "October"
number_of_nights = 40

if month == "May" or month == "October":
    studio_may_oct = number_of_nights * 50.00
    apartment_may_oct = number_of_nights * 65.00
    if number_of_nights > 0 and number_of_nights <= 7:
            print("Apartment: {:.2f} lv.".format(apartment_may_oct))
            print("Studio: {:.2f} lv.".format(studio_may_oct))
    elif number_of_nights > 7 and number_of_nights <= 14:
        discount_studio = number_of_nights * 50.00 * 5 / 100
        print("Apartment: {:.2f} lv.".format(apartment_may_oct))
        print("Studio: {:.2f} lv.".format(studio_may_oct - discount_studio))
    elif number_of_nights > 14:
        discount_studio = number_of_nights * 50.00 * 30 / 100
        discount_apart = number_of_nights * 65.00 * 10 / 100
        print("Apartment: {:.2f} lv.".format(apartment_may_oct - discount_apart))
        print("Studio: {:.2f} lv.".format(studio_may_oct - discount_studio))
if month == "June" or month == "September":
    studio_june_sept = number_of_nights * 75.20
    apartment_june_sept = number_of_nights * 68.70
    if number_of_nights > 0 and number_of_nights <= 14:
            print("Apartment: {:.2f} lv.".format(apartment_june_sept))
            print("Studio: {:.2f} lv.".format(studio_june_sept))
    elif number_of_nights > 14:
        discount_studio = number_of_nights * 75.20 * 20 / 100
        discount_apart = number_of_nights * 68.70 * 10 / 100
        print("Apartment: {:.2f} lv.".format(apartment_june_sept))
        print("Studio: {:.2f} lv.".format(studio_june_sept - discount_studio))
if month == "July" or month ==  "August":
    studio_july_aug = number_of_nights * 76.00
    apartment_july_aug = number_of_nights * 77.00
    if number_of_nights > 0 and number_of_nights <= 14:
        print("Apartment: {:.2f} lv.".format(apartment_july_aug))
        print("Studio: {:.2f} lv.".format(studio_july_aug))
    elif number_of_nights > 14:
        discount_apart = number_of_nights * 77.00 * 10 / 100
        print("Apartment: {:.2f} lv.".format(apartment_july_aug - discount_apart))
        print("Studio: {:.2f} lv.".format(studio_july_aug))